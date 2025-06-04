class Door:
    def __init__(self, id_):
        self.id = id_
    def __repr__(self):
        return f"Door({self.id})"

class Wall:
    def __init__(self, has_door: bool, door=None):
        self.has_door = has_door
        self.door = door  # None if no door
    def can_pass(self):
        return self.has_door
    def __repr__(self):
        return f"Wall(door={self.door})" if self.has_door else "Wall(no door)"

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbors = {}  # direction -> (neighbor_cell, wall)
    def add_neighbor(self, direction, neighbor_cell, wall):
        self.neighbors[direction] = (neighbor_cell, wall)
    def __repr__(self):
        return f"Cell({self.x},{self.y})"

class Maze:
    def __init__(self, height, width, h_doors_map, v_doors_map):
        self.height = height
        self.width = width
        self.grid = [[Cell(r,c) for c in range(width)] for r in range(height)]
        self.doors = []
        self._build_maze(h_doors_map, v_doors_map)

    def _build_maze(self, h_map, v_map):
        # The doors are represented by 0 according to problem statement.
        # We create doors with unique IDs when a door exists (0).
        door_id = 0
        # horizontal connections: between (r,c) and (r,c+1)
        for r in range(self.height):
            for c in range(self.width - 1):
                # h_map has rows = height, cols = width-1
                has_door = h_map[r][c] == 0
                door_ref = None
                if has_door:
                    door_ref = Door(door_id)
                    self.doors.append(door_ref)
                    door_id += 1
                wall = Wall(has_door, door_ref)
                self.grid[r][c].add_neighbor('R', self.grid[r][c+1], wall)
                self.grid[r][c+1].add_neighbor('L', self.grid[r][c], wall)
        # vertical connections: between (r,c) and (r+1,c)
        for r in range(self.height - 1):
            for c in range(self.width):
                has_door = v_map[r][c] == 0
                door_ref = None
                if has_door:
                    door_ref = Door(door_id)
                    self.doors.append(door_ref)
                    door_id += 1
                wall = Wall(has_door, door_ref)
                self.grid[r][c].add_neighbor('D', self.grid[r+1][c], wall)
                self.grid[r+1][c].add_neighbor('U', self.grid[r][c], wall)

    def get_entry_cell(self):
        # Entry is at top left cell but through its upper side (open)
        # So we can start at cell(0,0) effectively.
        return self.grid[0][0]

    def get_exit_cell(self):
        # Exit is at bottom right cell through its right side (open)
        return self.grid[self.height-1][self.width-1]

    def all_doors(self):
        return self.doors[:]

class State:
    def __init__(self, cell, broken_door=None):
        self.cell = cell
        self.broken_door = broken_door  # None or Door object
    def __hash__(self):
        return hash((self.cell.x, self.cell.y, self.broken_door.id if self.broken_door else None))
    def __eq__(self, other):
        return (self.cell.x == other.cell.x and self.cell.y == other.cell.y and
                ((self.broken_door is None and other.broken_door is None) or
                 (self.broken_door is not None and other.broken_door is not None and self.broken_door.id == other.broken_door.id)))
    def __repr__(self):
        return f"State(Cell({self.cell.x},{self.cell.y}), broken_door={self.broken_door})"

from collections import deque

class MazeSolver:
    def __init__(self, maze: Maze):
        self.maze = maze
        # Precompute shortest distances with no broken door
        self.dist_all_doors_normal = self._compute_shortest_distances()
        # For each broken door scenario we will compute shortest distances to exit excluding that door
        self.single_door_dist_cache = {}

    def _compute_shortest_distances(self, exclude_door=None, start=None):
        # Dijkstra over the graph of cells.
        # Cost to move through a door == 1 card, no door means no move
        # If exclude_door is specified, cannot use that door.
        # If start is None, start at entry cell.
        import heapq
        if start is None:
            start = self.maze.get_entry_cell()
        dist = [[float('inf')] * self.maze.width for _ in range(self.maze.height)]
        dist[start.x][start.y] = 0
        hq = [(0, start.x, start.y)]
        while hq:
            cur_cost, x, y = heapq.heappop(hq)
            if dist[x][y] < cur_cost:
                continue
            current_cell = self.maze.grid[x][y]
            for dir_, (neighbor, wall) in current_cell.neighbors.items():
                if not wall.can_pass():
                    continue
                if exclude_door is not None and wall.door == exclude_door:
                    # Can't pass broken door
                    continue
                nxt_cost = cur_cost + 1  # passing a door consumes 1 card
                if dist[neighbor.x][neighbor.y] > nxt_cost:
                    dist[neighbor.x][neighbor.y] = nxt_cost
                    heapq.heappush(hq, (nxt_cost, neighbor.x, neighbor.y))
        return dist

    def solve(self):
        # The problem requires the minimum number of cards to pass the maze whichever door is broken.
        # Strategy: for all doors that can be broken
        # Check that there is some path useful.
        # If for some broken door no path exists => output -1.

        # We try a BFS with state = (cell, broken_door)
        # Transition:
        # - if no broken_door known, whenever we use a door, we can either guess it's broken, or it's not broken.
        # We try to model the strategy described:
        # Start with no broken_door known.
        # Once broken_door is found (allowed to re-route), the path is shortest excluding broken_door.

        # To do so efficiently, we precompute shortest distance from entry to every cell having no broken door.
        # And shortest distance from every cell to exit excluding broken door d, for all d.

        # Steps:
        # 1) shortest dist from entry to all cells with no broken door
        dist_start = self.dist_all_doors_normal

        # 2) For every door, shortest dist from all cells to exit avoiding that door, cached
        # We'll need distances from any cell, so compute from exit backward, reversing edges is complicated:
        # Instead, compute a dist array from cells to exit is equivalent to shortest path from exit to cell using reversed edges.
        # We do normal forward distances from any start cell, but we want distance from any to exit.
        # We'll compute dist_exit[d] for excluding door d:
        # We'll compute from exit cell going backwards:
        #
        # Since the graph is undirected with doors on edges, we can treat edges symmetrically.
        # We'll just do shortest path from exit cell ignoring door d.

        # Since the maze is undirected, the shortest distance from exit to cell is same as from cell to exit.
        # So compute dist from exit to all cells excluding broken door

        dist_exit_cache = {}
        exit_cell = self.maze.get_exit_cell()

        for door in self.maze.all_doors():
            dist_exit_cache[door.id] = self._compute_shortest_distances(exclude_door=door, start=exit_cell)

        # For no broken door, dist_exit distance is minimal path from exit to cell (equiv to cell to exit)
        dist_exit_cache[None] = self._compute_shortest_distances(exclude_door=None, start=exit_cell)

        # We will do a Dijkstra-like BFS over state (cell, broken_door_found)
        # cost meaning the total cards used so far
        import heapq
        start_state = State(self.maze.get_entry_cell(), None)
        dist_state = {}
        dist_state[start_state] = 0
        pq = [(0, start_state)]

        while pq:
            cost, state = heapq.heappop(pq)
            if state in dist_state and dist_state[state] < cost:
                continue
            # If reached exit cell, return cost
            if state.cell == self.maze.get_exit_cell():
                return cost

            ccell = state.cell
            bdoor = state.broken_door

            # For each neighbor try going through door
            for dir_, (next_cell, wall) in ccell.neighbors.items():
                if not wall.can_pass():
                    continue
                door = wall.door
                # If broken door known, cannot pass wall if it is broken door
                if bdoor is not None:
                    if door == bdoor:
                        # Can't pass broken door
                        continue
                    # cost to move: +1 card for any door
                    next_cost = cost + 1
                    nxt_state = State(next_cell, bdoor)
                    if nxt_state not in dist_state or dist_state[nxt_state] > next_cost:
                        dist_state[nxt_state] = next_cost
                        heapq.heappush(pq, (next_cost, nxt_state))
                else:
                    # broken door unknown
                    # move costs 1 card + broken door detection if door is broken or not

                    # Two possibilities:
                    # 1) Door is not broken: use 1 card, broken_door still None
                    next_cost_normal = cost + 1
                    nxt_state_normal = State(next_cell, None)
                    if nxt_state_normal not in dist_state or dist_state[nxt_state_normal] > next_cost_normal:
                        dist_state[nxt_state_normal] = next_cost_normal
                        heapq.heappush(pq, (next_cost_normal, nxt_state_normal))

                    # 2) Door is broken: can't pass, card not lost, but broken door detected => break broken door identified
                    # Actually can't pass, so we can't move to neighbor through broken door
                    # But we detect broken door, so we "stay in place" but update broken door discovered
                    # This means from current cell, with broken door known now.
                    # Path broken door door.id is detected, so broken_door known, and after detection we must find alternate path.

                    # If we have never discovered broken door door.door before:
                    # We must explore from this current cell, broken door known now
                    # Cost for detection is 0 cards here because card is returned if broken door.

                    nxt_state_broken = State(ccell, door)
                    if nxt_state_broken not in dist_state or dist_state[nxt_state_broken] > cost:
                        dist_state[nxt_state_broken] = cost
                        heapq.heappush(pq, (cost, nxt_state_broken))

        # If exhausted all states without reaching exit, no solution:
        return -1

def parse_input():
    import sys
    input_data = sys.stdin.read().strip().split('\n')
    idx = 0
    datasets = []
    while True:
        if idx >= len(input_data):
            break
        line = input_data[idx].strip()
        if line == '':
            idx += 1
            continue
        h_w = line.split()
        if len(h_w) < 2:
            idx += 1
            continue
        h, w = map(int, h_w)
        if h == 0 and w == 0:
            break
        idx += 1
        # Reading 2*h-1 lines for doors
        h_doors_map = [] # horizontal doors: 1=no door,0=door in input but store as bool has_door: True == door
        v_doors_map = [] # vertical doors
        # The input lines alternate:
        # line 0: ' ' + w-1 integers, horizontal doors row 0
        # line 1: w integers no leading space, vertical doors row 0 (between row 0 and 1)
        # and so on alternating horizontal/vertical doors

        # We'll read 2*h-1 lines and split into horizontal and vertical maps by rows numbers
        lines = input_data[idx:idx+2*h-1]
        idx += 2*h-1
        # Parse lines:
        # horizontal lines: 0,2,4,... (h lines)
        # vertical lines: 1,3,5,... (h-1 lines)
        # We convert 0->door, 1->no door by the problem statement, so to has_door boolean we do (val == 0)
        for line_i in range(2*h-1):
            line_str = lines[line_i].strip()
            vals = list(map(int, line_str.split()))
            if line_i % 2 == 0:
                # horizontal line
                # Must have w-1 values
                # We store True if door exists (0 means door)
                h_doors_map.append(vals)
            else:
                # vertical line
                # must have w values
                v_doors_map.append(vals)

        datasets.append((h, w, h_doors_map, v_doors_map))
    return datasets

def main():
    datasets = parse_input()
    for (h, w, h_map, v_map) in datasets:
        maze = Maze(h, w, h_map, v_map)
        solver = MazeSolver(maze)
        ans = solver.solve()
        print(ans)

if __name__ == "__main__":
    main()