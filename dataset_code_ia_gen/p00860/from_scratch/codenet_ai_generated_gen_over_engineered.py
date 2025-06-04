from collections import deque
from typing import List, Tuple, Set, Dict, Optional, Iterator
import sys

class Position:
    __slots__ = ('x', 'y')
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def neighbors(self, max_x: int, max_y: int) -> Iterator['Position']:
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = self.x+dx, self.y+dy
            if 0 <= nx < max_x and 0 <= ny < max_y:
                yield Position(nx, ny)
    
    def __eq__(self, other):
        return isinstance(other, Position) and self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __lt__(self, other):
        return (self.y, self.x) < (other.y, other.x)
    
    def __repr__(self):
        return f"Pos({self.x},{self.y})"

class FloorMap:
    def __init__(self, width: int, height: int, grid: List[List[str]]):
        self.width = width
        self.height = height
        self.grid = grid
        self.walls = set()
        self.corridors = set()
        self._analyze()
    
    def _analyze(self):
        for y in range(self.height):
            for x in range(self.width):
                c = self.grid[y][x]
                if c == '#':
                    self.walls.add(Position(x,y))
                else:
                    self.corridors.add(Position(x,y))
    
    def is_corridor(self, pos: Position) -> bool:
        return pos in self.corridors
    
    def is_wall(self, pos: Position) -> bool:
        return pos in self.walls

class Ghost:
    def __init__(self, name: str, start_pos: Position, goal_pos: Position):
        self.name = name
        self.start_pos = start_pos
        self.goal_pos = goal_pos

class State:
    __slots__ = ('positions',)
    
    def __init__(self, positions: Tuple[Position, ...]):
        self.positions = positions
    
    def __hash__(self):
        return hash(self.positions)
    
    def __eq__(self, other):
        return isinstance(other, State) and self.positions == other.positions
    
    def __repr__(self):
        return f"State({self.positions})"

class MovementGenerator:
    # Generates all possible next states given current ghost positions and floor map.
    
    def __init__(self, floor_map: FloorMap, ghosts: List[Ghost]):
        self.floor_map = floor_map
        self.num_ghosts = len(ghosts)
        self.max_x = floor_map.width
        self.max_y = floor_map.height
    
    def generate(self, current_state: State) -> Iterator[State]:
        positions = current_state.positions
        
        # For each ghost, possible moves: current pos or neighbors that are corridor and not walls
        candidate_moves = []
        for pos in positions:
            moves = [pos]
            for n in pos.neighbors(self.max_x, self.max_y):
                if self.floor_map.is_corridor(n):
                    moves.append(n)
            candidate_moves.append(moves)
        
        # We'll generate all combinations of moves (ghost 0 move x ghost1 move x ...)
        # Prune invalid moves:
        # - No two ghosts in same cell after move
        # - No two ghosts swap positions in one step
        
        def backtrack(index: int, chosen: List[Position], used: Set[Position]) -> Iterator[State]:
            if index == self.num_ghosts:
                # Check no position swapping:
                # For every pair i<j, forbid positions[i] == chosen[j] and positions[j] == chosen[i]
                for i in range(self.num_ghosts):
                    for j in range(i+1, self.num_ghosts):
                        if positions[i] == chosen[j] and positions[j] == chosen[i]:
                            return
                yield State(tuple(chosen))
                return
            for move_pos in candidate_moves[index]:
                if move_pos not in used:
                    used.add(move_pos)
                    chosen.append(move_pos)
                    yield from backtrack(index+1, chosen, used)
                    chosen.pop()
                    used.remove(move_pos)
        
        yield from backtrack(0, [], set())

class GhostsRestorer:
    def __init__(self, floor_map: FloorMap, ghosts: List[Ghost]):
        self.floor_map = floor_map
        self.ghosts = ghosts
        self.movement_generator = MovementGenerator(floor_map, ghosts)
        self.start_state = State(tuple(g.start_pos for g in ghosts))
        self.goal_state = State(tuple(g.goal_pos for g in ghosts))
    
    def minimum_steps(self) -> int:
        # BFS over states to find minimum steps from start_state to goal_state
        queue = deque([self.start_state])
        visited = set([self.start_state])
        dist = {self.start_state: 0}
        while queue:
            current = queue.popleft()
            if current == self.goal_state:
                return dist[current]
            for nxt in self.movement_generator.generate(current):
                if nxt not in visited:
                    visited.add(nxt)
                    dist[nxt] = dist[current] + 1
                    queue.append(nxt)
        # According to problem guarantee, reachable, no need else
        return -1

class InputParser:
    @staticmethod
    def parse_dataset(lines: List[str]) -> Optional[Tuple[FloorMap, List[Ghost]]]:
        if not lines:
            return None
        first_line = lines[0].strip()
        if first_line == "0 0 0":
            return None
        
        w, h, n = map(int, first_line.split())
        grid = [list(lines[i+1]) for i in range(h)]
        
        # Parse positions of ghosts and goals
        # ghosts: first n letters from 'a' for start, first n uppercase letter for goal
        ghost_starts: Dict[str, Position] = {}
        ghost_goals: Dict[str, Position] = {}
        
        for y in range(h):
            for x in range(w):
                c = grid[y][x]
                if c.islower():
                    # ghost start
                    ghost_starts[c] = Position(x, y)
                elif c.isupper():
                    ghost_goals[c.lower()] = Position(x, y)
        
        ghosts = []
        # Important: order ghosts by 'a','b','c' strictly first n letters
        for i in range(n):
            ch = chr(ord('a')+i)
            ghosts.append(Ghost(ch, ghost_starts[ch], ghost_goals[ch]))
        
        floor_map = FloorMap(w, h, grid)
        return floor_map, ghosts

def main():
    input_lines = sys.stdin.read().splitlines()
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        line = input_lines[idx]
        if line.strip() == '0 0 0':
            break
        # parse current dataset lines count = h+1
        w, h, n = map(int, line.split())
        dataset_lines = input_lines[idx:idx+h+1]
        parsed = InputParser.parse_dataset(dataset_lines)
        idx += h+1
        if parsed is None:
            break
        floor_map, ghosts = parsed
        restorer = GhostsRestorer(floor_map, ghosts)
        print(restorer.minimum_steps())

if __name__ == "__main__":
    main()