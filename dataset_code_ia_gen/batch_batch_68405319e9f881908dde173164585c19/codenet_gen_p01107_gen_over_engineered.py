from typing import List, Tuple, Set, Dict
from collections import deque, namedtuple
import sys

# Abstract base class for the labyrinth representation
class Labyrinth:
    def __init__(self, grid: List[str]):
        self.grid = grid
        self.N = len(grid)
        self.M = len(grid[0]) if self.N > 0 else 0
        self.entrance = (0,0)
        self.treasures = [(self.N-1,0), (self.N-1,self.M-1), (0,self.M-1)]
    
    def is_enterable(self, pos: Tuple[int,int]) -> bool:
        r, c = pos
        return 0 <= r < self.N and 0 <= c < self.M and self.grid[r][c] == '.'
    
    def neighbors(self, pos: Tuple[int,int]) -> List[Tuple[int,int]]:
        r, c = pos
        candidates = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
        return [p for p in candidates if self.is_enterable(p)]

# Abstract path state to be extended by the solver
class PathState:
    def __init__(self, position: Tuple[int,int], visited_treasures: Set[int], fragile_map: Set[Tuple[int,int]]):
        self.position = position        # Current position of Taro
        self.visited_treasures = frozenset(visited_treasures)  # Immutable for hashability
        self.fragile_map = fragile_map  # Set of positions that have collapsed
    
    def __hash__(self):
        return hash((self.position, self.visited_treasures, tuple(sorted(self.fragile_map))))
    
    def __eq__(self, other):
        return (self.position == other.position and
                self.visited_treasures == other.visited_treasures and
                self.fragile_map == other.fragile_map)

# Customized labyrinthe that supports collapse logic
class FragileLabyrinth(Labyrinth):
    def __init__(self, grid: List[str]):
        super().__init__(grid)
    
    def start_state(self) -> PathState:
        # At start no treasure visited, no floor collapsed except entrance is stable
        # Entrance floor never collapses
        fragile_map = set()
        return PathState(self.entrance, set(), fragile_map)
    
    def is_treasure_pos(self, pos: Tuple[int,int]) -> int:
        # Returns index of treasure if pos is a treasure location, else -1
        try:
            return self.treasures.index(pos)
        except ValueError:
            return -1

    def can_step(self, pos: Tuple[int,int], fragile_map: Set[Tuple[int,int]]) -> bool:
        # Entrance never collapses, others not in fragile_map and enterable
        if pos == self.entrance:
            return self.is_enterable(pos)
        if pos in fragile_map:
            return False
        return self.is_enterable(pos)
    
    def next_states(self, state: PathState) -> List[PathState]:
        results = []
        for npos in self.neighbors(state.position):
            if self.can_step(npos, state.fragile_map):
                # Calculate new treasures visited
                treasures_visited = set(state.visited_treasures)
                idx = self.is_treasure_pos(npos)
                if idx != -1:
                    treasures_visited.add(idx)
                # Calculate new fragile map:
                # If current position is not entrance, it collapses after leaving
                new_fragile_map = set(state.fragile_map)
                if state.position != self.entrance:
                    new_fragile_map.add(state.position)
                results.append(PathState(npos, treasures_visited, new_fragile_map))
        return results

# A generic graph search interface to solve the labyrinth challenge
class LabyrinthSolver:
    def __init__(self, labyrinth: FragileLabyrinth):
        self.labyrinth = labyrinth
        self.total_treasures = set(range(len(self.labyrinth.treasures)))
    
    def can_collect_all_and_return(self) -> bool:
        start_state = self.labyrinth.start_state()
        queue = deque([start_state])
        visited = set([start_state])
        
        while queue:
            current = queue.popleft()
            # Check success conditions:
            # Collected all treasures and currently at entrance
            if current.position == self.labyrinth.entrance and current.visited_treasures == self.total_treasures:
                return True
            for next_state in self.labyrinth.next_states(current):
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append(next_state)
        return False

# Factory to parse input into labyrinth objects
class LabyrinthFactory:
    @staticmethod
    def from_input(N: int, M: int, grid_lines: List[str]) -> FragileLabyrinth:
        # Build labyrinth, validate entrance and treasure rooms are enterable
        labyrinth = FragileLabyrinth(grid_lines)
        assert labyrinth.is_enterable(labyrinth.entrance), "Entrance must be enterable"
        for tpos in labyrinth.treasures:
            assert labyrinth.is_enterable(tpos), "Treasure room must be enterable"
        return labyrinth

# Main processing pipeline
def process_datasets(inputs: List[Tuple[int,int,List[str]]]) -> List[str]:
    results = []
    for (N, M, grid_lines) in inputs:
        labyrinth = LabyrinthFactory.from_input(N, M, grid_lines)
        solver = LabyrinthSolver(labyrinth)
        can_complete = solver.can_collect_all_and_return()
        results.append("YES" if can_complete else "NO")
    return results

def main():
    inputs = []
    input_iter = iter(sys.stdin.read().strip().split('\n'))
    while True:
        try:
            line = next(input_iter)
        except StopIteration:
            break
        if line.strip() == '':
            continue
        N, M = map(int, line.split())
        if N == 0 and M == 0:
            break
        grid_lines = []
        for _ in range(N):
            grid_lines.append(next(input_iter))
        inputs.append((N, M, grid_lines))
    results = process_datasets(inputs)
    for r in results:
        print(r)

if __name__ == "__main__":
    main()