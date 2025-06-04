from collections import deque
from typing import List, Tuple, Optional, Iterator, Set

class GridPoint:
    def __init__(self, x: int, y: int, terrain: str):
        self.x = x
        self.y = y
        self.terrain = terrain  # '.', '#', '&'
    def is_moat(self) -> bool:
        return self.terrain == '#'
    def is_goal(self) -> bool:
        return self.terrain == '&'
    def __repr__(self):
        return f"GridPoint({self.x},{self.y},'{self.terrain}')"

class CastleMap:
    def __init__(self, width: int, height: int, grid_lines: List[str]):
        self.width = width
        self.height = height
        self.grid: List[List[GridPoint]] = [
            [GridPoint(x, y, grid_lines[y][x]) for x in range(width)]
            for y in range(height)
        ]
        self.goal_position: Optional[Tuple[int, int]] = self._locate_goal()
    def _locate_goal(self) -> Optional[Tuple[int,int]]:
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x].is_goal():
                    return (x,y)
        return None
    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height
    def neighbors(self, x: int, y: int) -> Iterator[Tuple[int,int]]:
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x + dx, y + dy
            if self.in_bounds(nx, ny):
                yield nx, ny
    def point(self, x: int, y: int) -> GridPoint:
        return self.grid[y][x]

class NinjaPathfinder:
    """
    A sophisticated class to find minimal times ninja must crawl out of moat (#) when traveling from outside
    (any non-castle perimeter edge cell not in moat) to goal (&).
    Anticipates subclasses or different terrains or movement costs.
    """
    def __init__(self, castle_map: CastleMap):
        self.castle_map = castle_map
        self.width = castle_map.width
        self.height = castle_map.height
        self.goal = castle_map.goal_position
        if self.goal is None:
            raise ValueError("Goal (&) not found in the map.")
        # We'll think of outside as any cell on edges that is not in moat or goal.
        # The ninja starts outside and can start from any such cell.
        self.outside_cells = self._detect_outside_cells()
    def _detect_outside_cells(self) -> List[Tuple[int,int]]:
        outside = []
        for x in range(self.width):
            for y in [0, self.height-1]:
                pt = self.castle_map.point(x,y)
                if not pt.is_moat() and not pt.is_goal():
                    outside.append((x,y))
        for y in range(self.height):
            for x in [0, self.width-1]:
                pt = self.castle_map.point(x,y)
                if not pt.is_moat() and not pt.is_goal():
                    outside.append((x,y))
        # Remove duplicates if corners were added twice
        return list(set(outside))
    def minimum_climbs(self) -> int:
        """
        Compute minimum number of times ninja must climb out of moat (#).
        Ninja can swim or run inside moat or non-moat cells.
        Climbing out means going from a moat cell to a non-moat cell.
        We want minimal such transitions to reach goal.
        """
        # Weight of edges:
        # transitions from non-moat->non-moat or moat->moat or moat->non-moat = 0 if not climbing up,
        # climbing up means moat->non-moat transition, cost = 1
        # non-moat->moat has cost 0, entering moat first time costs nothing except next climbing up.
        # So climbing up = transitions from '#' cell to '.' or '&' cell.
        
        # Perform Dijkstra or 0-1 BFS with weights 0 or 1 on edges.
        from collections import deque
        
        # dist[y][x] = minimal number of climbs to reach (x,y)
        dist = [[float('inf')] * self.width for _ in range(self.height)]
        
        dq = deque()
        # Initialize deque with all outside starting cells with cost 0
        for (sx, sy) in self.outside_cells:
            dist[sy][sx] = 0
            dq.appendleft((sx, sy))
        
        while dq:
            x,y = dq.popleft()
            current_point = self.castle_map.point(x,y)
            current_dist = dist[y][x]
            for nx, ny in self.castle_map.neighbors(x,y):
                neighbor_point = self.castle_map.point(nx,ny)
                # Determine if climbing out = from moat to non-moat
                climb_cost = 0
                if current_point.is_moat() and not neighbor_point.is_moat():
                    climb_cost = 1
                nd = current_dist + climb_cost
                if dist[ny][nx] > nd:
                    dist[ny][nx] = nd
                    # 0-1 BFS: if climb_cost=0 add to left, else right.
                    if climb_cost == 0:
                        dq.appendleft((nx,ny))
                    else:
                        dq.append((nx,ny))
        
        goal_x, goal_y = self.goal
        res = dist[goal_y][goal_x]
        return int(res) if res != float('inf') else 0

class InputParser:
    def __init__(self):
        self.datasets: List[Tuple[int,int,List[str]]] = []
    def parse(self, lines: Iterator[str]) -> None:
        while True:
            try:
                line = next(lines)
                if line.strip() == "0 0":
                    break
                n, m = map(int, line.split())
                grid_lines = []
                for _ in range(m):
                    grid_lines.append(next(lines).rstrip('\n'))
                self.datasets.append((n,m,grid_lines))
            except StopIteration:
                break

class NinjaSolutionRunner:
    def __init__(self, datasets: List[Tuple[int,int,List[str]]]):
        self.datasets = datasets
    def run(self) -> List[int]:
        results = []
        for n,m,grid_lines in self.datasets:
            castle_map = CastleMap(n,m,grid_lines)
            pathfinder = NinjaPathfinder(castle_map)
            results.append(pathfinder.minimum_climbs())
        return results

def main():
    import sys
    parser = InputParser()
    parser.parse(iter(sys.stdin))
    runner = NinjaSolutionRunner(parser.datasets)
    results = runner.run()
    for r in results:
        print(r)

if __name__=="__main__":
    main()