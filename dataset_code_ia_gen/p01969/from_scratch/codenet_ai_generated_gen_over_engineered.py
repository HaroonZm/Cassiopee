from collections import deque
from typing import Dict, Tuple, List, Set, Optional


class Position:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def neighbors4(self) -> List['Position']:
        return [Position(self.row - 1, self.col),
                Position(self.row + 1, self.col),
                Position(self.row, self.col - 1),
                Position(self.row, self.col + 1)]

    def __eq__(self, other):
        return isinstance(other, Position) and (self.row, self.col) == (other.row, other.col)

    def __hash__(self):
        return hash((self.row, self.col))

    def __repr__(self):
        return f"Pos({self.row},{self.col})"


class Vertex:
    def __init__(self, label: str, position: Position):
        self.label = label
        self.position = position
        # adjacency list neighbors by Vertex label
        self.neighbors: Set[str] = set()

    def __repr__(self):
        return f"Vertex({self.label}, {self.position}, neighbors={self.neighbors})"


class AA_Graph:
    def __init__(self, grid: List[str]):
        self.grid = grid
        self.H = len(grid)
        self.W = len(grid[0]) if self.H > 0 else 0
        self.vertices: Dict[str, Vertex] = {}
        # map from position to vertex label
        self.pos_to_label: Dict[Position, str] = {}

    def in_bounds(self, pos: Position) -> bool:
        return 0 <= pos.row < self.H and 0 <= pos.col < self.W

    def char_at(self, pos: Position) -> str:
        if not self.in_bounds(pos):
            return ''
        return self.grid[pos.row][pos.col]

    def find_vertices(self) -> None:
        # Vertex: uppercase char 'A'..'Z' with 'o' surrounding 8 neighs in 8 directions
        # We confirm it with the pattern:
        # ooo
        # oAo
        # ooo
        for r in range(self.H):
            for c in range(self.W):
                ch = self.grid[r][c]
                if 'A' <= ch <= 'Z':
                    center = Position(r, c)
                    if self._check_surrounding_o(center):
                        v = Vertex(ch, center)
                        self.vertices[ch] = v
                        self.pos_to_label[center] = ch

    def _check_surrounding_o(self, center: Position) -> bool:
        # positions of 8 neighbors around center
        neighbors8 = [Position(center.row + dr, center.col + dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1)
                      if not (dr == 0 and dc == 0)]
        for pos in neighbors8:
            if not self.in_bounds(pos):  # Out of bounds means no 'o'
                return False
            if self.grid[pos.row][pos.col] != 'o':
                return False
        return True

    def build_graph(self) -> None:
        # For each vertex, check the 4 directions where edges can extend.
        # Edges are indicated by '-' horizontally and '|' vertically
        # Every edge is connected to a symbol o adjacent to the vertex.
        # For each direction from a vertex, we find the 'o' next to it, then follow along
        # continuous '-' or '|' until next vertex is reached with format oAo
        # We'll try to find edges with length 1 (no matter edge length of symbols)
        for label, vertex in self.vertices.items():
            r, c = vertex.position.row, vertex.position.col
            # Check each of 4 directions: up, down, left, right
            # For each direction, start from the vertex and locate the 'o' neighbor
            directions = {
                'up': Position(r - 1, c),
                'down': Position(r + 1, c),
                'left': Position(r, c - 1),
                'right': Position(r, c + 1),
            }
            for dname, pos_o in directions.items():
                if self.in_bounds(pos_o) and self.char_at(pos_o) == 'o':
                    # Follow edge along this direction until next vertex found
                    neighbor_label = self._follow_edge(pos_o, dname, label)
                    if neighbor_label is not None:
                        vertex.neighbors.add(neighbor_label)

    def _follow_edge(self, start_o: Position, direction: str, from_label: str) -> Optional[str]:
        # direction indicates where to advance next: up, down, left, right
        # Invariant: edges use only - or | symbols
        # We walk starting from start_o along the direction:
        # pattern to detect is that final vertex position is uppercase char surrounded by o's.
        # The immediate neighbor to that vertex must be 'o' gettable from walking

        delta = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }
        dr, dc = delta[direction]
        pos = start_o
        last_pos = pos
        while True:
            next_row = pos.row + dr
            next_col = pos.col + dc
            next_pos = Position(next_row, next_col)
            if not self.in_bounds(next_pos):
                return None
            ch = self.char_at(next_pos)

            if ch == '.':
                return None  # no edge here
            if 'A' <= ch <= 'Z':
                # Check if this is a vertex with well-formed surrounding o's
                if self._check_surrounding_o(next_pos):
                    label_found = self.pos_to_label.get(next_pos, None)
                    if label_found and label_found != from_label:
                        return label_found
                    return None

            # if next position is 'o', continue along
            if ch == 'o':
                pos = next_pos
                continue
            # Must be edge symbol compatible ('-' for horizontal, '|' for vertical)
            if direction in ('left', 'right'):
                if ch != '-':
                    return None
            else:  # up, down
                if ch != '|':
                    return None

            pos = next_pos

    def shortest_path_length(self, start_label: str, end_label: str) -> int:
        # BFS on vertices
        if start_label == end_label:
            return 0
        visited: Set[str] = set()
        queue = deque([(start_label, 0)])
        visited.add(start_label)
        while queue:
            curr_label, dist = queue.popleft()
            curr_vertex = self.vertices[curr_label]
            for nxt_label in curr_vertex.neighbors:
                if nxt_label == end_label:
                    return dist + 1
                if nxt_label not in visited:
                    visited.add(nxt_label)
                    queue.append((nxt_label, dist + 1))
        return -1  # no path, but problem states graph connected so shouldn't happen


class AA_Graph_Solver:
    def __init__(self, H: int, W: int, s: str, t: str, ascii_art: List[str]):
        self.H = H
        self.W = W
        self.s = s
        self.t = t
        self.ascii_art = ascii_art
        self.graph = AA_Graph(ascii_art)

    def solve(self) -> int:
        self.graph.find_vertices()
        self.graph.build_graph()
        return self.graph.shortest_path_length(self.s, self.t)


def main():
    import sys
    input = sys.stdin.readline
    H, W, s, t = input().strip().split()
    H, W = int(H), int(W)
    ascii_art = [input().rstrip('\n') for _ in range(H)]
    solver = AA_Graph_Solver(H, W, s, t, ascii_art)
    ans = solver.solve()
    print(ans)


if __name__ == '__main__':
    main()