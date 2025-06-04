import sys
import math
from abc import ABC, abstractmethod
from typing import List, Tuple

# Constants
GRAVITY = 1.0

# ======= Core Physics Abstractions =======

class ParabolicTrajectory:
    """Represents a single parabolic flight segment of the bullet."""
    def __init__(self, horizontal_distance: float, initial_vx: float, initial_vy: float):
        self.l = horizontal_distance
        self.vx = initial_vx
        self.vy = initial_vy
        # For given vx, vy, l must satisfy l = 2 * vx * vy / g
        # Parabola equation: y = -(g/(2 vx^2)) x^2 + (vy/vx) x
    
    def height_at(self, x: float) -> float:
        """Return the height of bullet at horizontal distance x."""
        if x < 0 or x > self.l:
            return float('-inf')  # outside flight segment
        return -(GRAVITY / (2 * self.vx ** 2)) * (x ** 2) + (self.vy / self.vx) * x

    def is_clear_of_obstacle(self, obstacles: List['Obstacle']) -> bool:
        """Check trajectory does not hit obstacles in [0, l]."""
        for obs in obstacles:
            if 0 < obs.position < self.l:
                h = self.height_at(obs.position)
                if h <= obs.height + 1e-14:  # touch or below obstacle height means fail
                    return False
        return True


class VelocityComponents:
    """Utility class for velocity components calculation and magnitude."""
    def __init__(self, vx: float, vy: float):
        self.vx = vx
        self.vy = vy
    
    @property
    def magnitude(self) -> float:
        return math.sqrt(self.vx ** 2 + self.vy ** 2)


# ======= Input Data Abstractions =======

class Obstacle:
    def __init__(self, position: int, height: int):
        self.position = position
        self.height = height
    
    def __repr__(self):
        return f"Obstacle(pos={self.position}, h={self.height})"

class ProblemInput:
    def __init__(self, distance: int, obstacles: List[Obstacle], max_bounces: int):
        self.distance = distance
        self.obstacles = obstacles
        self.max_bounces = max_bounces


# ======= Strategy Pattern for Bounce Splitting =======

class BounceSplitter(ABC):
    """Abstract strategy that determines how to split total distance into segments."""
    @abstractmethod
    def generate_splits(self, total_distance: int, bounces: int) -> List[List[int]]:
        pass

class SimpleSplitGenerator(BounceSplitter):
    """
    Generate all b-splits of total_distance into b+1 segments with positions increasing
    This enumerative approach supports future extension (dynamic obstacle avoidance)
    """
    def generate_splits(self, total_distance: int, bounces: int) -> List[List[int]]:
        if bounces == 0:
            return [[total_distance]]
        # Generate all possible sorted tuples of bounce positions between 0 and total_distance
        results = []
        def backtrack(start: int, depth: int, path: List[int]):
            if depth == bounces:
                # last segment length from last bounce to target
                last_segment = total_distance - path[-1]
                if last_segment > 0:
                    results.append([path[0]] + [path[i] - path[i-1] for i in range(1, len(path))] + [last_segment])
                return
            for next_pos in range(start + 1, total_distance):
                backtrack(next_pos, depth + 1, path + [next_pos])
        if bounces > 0:
            backtrack(0,0,[])
        else:
            results.append([total_distance])
        return results

# ======= Core Solver Logic =======

class TrajectoryPlanner:
    def __init__(self, problem_input: ProblemInput):
        self.d = problem_input.distance
        self.max_bounces = problem_input.max_bounces
        self.obstacles = problem_input.obstacles
        # Speed precision control
        self.epsilon = 1e-7
    
    def obstacles_in_segment(self, start: int, end: int) -> List[Obstacle]:
        return [o for o in self.obstacles if start < o.position < end]

    def can_make_segment(self, length: int, initial_speed: float, obstacles: List[Obstacle]) -> bool:
        """
        Check if possible to make a parabolic shot over segment length under initial_speed avoiding obstacles.
        We want to find if exists (vx, vy) with sqrt(vx^2 + vy^2) <= initial_speed with
        length = 2 * vx * vy, and all obstacles are cleared.
        """
        # Let the parabola parameters vx, vy >= 0 satisfy 2 vx vy = length.
        # Also vx^2 + vy^2 <= initial_speed^2.
        # For given length and initial_speed, vx must satisfy:
        # vx^2 + (length / (2 vx))^2 <= initial_speed^2
        # Rewrite as vx^2 + length^2 / (4 vx^2) <= initial_speed^2
        # Define f(vx) = vx^2 + length^2 / (4 vx^2)
        # We want to find vx > 0 such that f(vx) <= initial_speed^2
        
        # To solve, binary search vx in (0, initial_speed] to find a feasible parabola
        left, right = 1e-10, initial_speed
        feasible_found = False
        
        def check_vx(vx):
            vy = length / (2 * vx)
            if vy < 0:
                return False
            if vx**2 + vy**2 > initial_speed**2 + 1e-14:
                return False
            traj = ParabolicTrajectory(length, vx, vy)
            return traj.is_clear_of_obstacle(obstacles)
        
        # Because parabola shape changes with vx, do a binary search to find if any vx makes trajectory clear
        for _ in range(60):
            mid = (left + right) / 2
            if check_vx(mid):
                feasible_found = True
                right = mid
            else:
                left = mid
        return feasible_found

    def feasible(self, initial_speed: float) -> bool:
        """
        Check if there exists a way to break flight into segments (bounces+1 parts),
        each segment flyable with initial_speed avoiding obstacles,
        so bullet reaches target position hitting ground at last.
        """
        # Dynamic programming approach:
        # dp[bounce][pos] = True if can reach pos with bounce bounces within initial_speed
        # But we do not have many discrete positions; need logic friendlier.
        #
        # Instead, we try all bounce splits (positions of bounce points)
        # Because number of bounces max 15, and distance max 10000, enumerating all splits is huge.
        #
        # Instead, we try recursive DFS with memoization on bounce count and last position:
        # Since obstacles <= 10 and bounces <= 15, let's memo on bounce count and last bounce position
        
        cache = {}
        obstacles_positions = [o.position for o in self.obstacles]
        
        def dfs(remaining_bounces: int, from_pos: int, to_pos: int, obstacles_section: List[Obstacle]) -> bool:
            # Base: if no bounces left, check can make from_pos->to_pos segment flight
            segment_length = to_pos - from_pos
            return self.can_make_segment(segment_length, initial_speed, obstacles_section)
        
        # Since bounces can be up to 15, and obstacles fixed, naive complete enumeration is huge.
        # We'll perform a binary-search on number of splits positions only up to bounces allowed
        # We instead use a BFS with states: position and bounces left
        
        # Positions important to check bounces: obstacle positions and target position
        # To allow bounces only at integer positions, we choose bounces at positions between launcher and target.
        # We search bounce placements only at obstacle positions (since between obstacles no need for bounces)
        # Actually, the problem states bounces anywhere on surface, but for minimal initial speed,
        # bounces should be on ground, so can be anywhere between 0 and d.
        #
        # For complexity, we try all bounce partitions with bounces inserted only at obstacles positions or zero/distance.
        
        # We create candidate bounce positions list = [0] + obstacle positions + [d]
        points = [0] + obstacles_positions + [self.d]
        
        from collections import deque
        queue = deque()
        # tuple: (bounce used, current position index in points)
        queue.append((0, 0))  # start at launcher, no bounce used
        visited = set()
        
        while queue:
            bounces_used, idx = queue.popleft()
            if (bounces_used, idx) in visited:
                continue
            visited.add((bounces_used, idx))
            
            current_pos = points[idx]
            # Try jumping to all further points (simulate bounces)
            for next_idx in range(idx + 1, len(points)):
                next_pos = points[next_idx]
                if next_pos <= current_pos:
                    continue
                if bounces_used + 1 > self.max_bounces + 1:
                    break  # no more bounces allowed

                # Get obstacles between current_pos and next_pos
                obstacles_section = self.obstacles_in_segment(current_pos, next_pos)
                length = next_pos - current_pos
                if not self.can_make_segment(length, initial_speed, obstacles_section):
                    continue
                # If next_pos == target(d), we can succeed
                if next_pos == self.d:
                    return True
                # Otherwise we can bounce here if not exceed bounces allowed
                # bounces_used counts starting from zero, but max bounces exclude last bounce at target
                if bounces_used < self.max_bounces + 1:
                    queue.append((bounces_used + 1, next_idx))
        return False

    def solve(self) -> float:
        left = 0.0
        right = 1e5  # large upper bound for speed guess
        for _ in range(100):
            mid = (left + right) / 2
            if self.feasible(mid):
                right = mid
            else:
                left = mid
        return right


def parse_input() -> ProblemInput:
    d, n, b = map(int, sys.stdin.readline().split())
    obstacles = []
    for _ in range(n):
        p, h = map(int, sys.stdin.readline().split())
        obstacles.append(Obstacle(p, h))
    return ProblemInput(d, obstacles, b)

def main():
    problem = parse_input()
    planner = TrajectoryPlanner(problem)
    ans = planner.solve()
    print(f"{ans:.5f}")

if __name__ == "__main__":
    main()