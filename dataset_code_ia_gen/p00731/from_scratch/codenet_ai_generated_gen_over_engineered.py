class Cliff:
    def __init__(self, width, height, grid):
        self.width = width
        self.height = height
        self.grid = grid
        self.starts = [(x, height - 1) for x in range(width) if grid[height - 1][x] == 'S']
        self.targets = [(x, 0) for x in range(width) if grid[0][x] == 'T']

    def block_cost(self, x, y):
        cell = self.grid[y][x]
        if cell == 'S' or cell == 'T':
            return 0
        if cell == 'X':
            return None
        return int(cell)

    def is_block_walkable(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height and self.grid[y][x] != 'X'

    def is_target(self, x, y):
        return self.grid[y][x] == 'T'

    def is_start(self, x, y):
        return self.grid[y][x] == 'S'

    def neighbors_for_next_foot(self, lx, ly, rx, ry, next_is_left):
        # Generate all valid next positions for the moving foot
        current_foot = (lx, ly) if next_is_left else (rx, ry)
        other_foot = (rx, ry) if next_is_left else (lx, ly)

        candidates = []
        for nx in range(self.width):
            for ny in range(self.height):
                if not self.is_block_walkable(nx, ny):
                    continue
                # Check constraints: left foot < right foot by x
                if next_is_left:
                    # next is left foot
                    if not (nx < other_foot[0]): 
                        continue
                else:
                    # next is right foot
                    if not (other_foot[0] < nx):
                        continue
                # Distance constraints
                dist = abs(nx - other_foot[0]) + abs(ny - other_foot[1])
                if dist > 3:
                    continue
                candidates.append((nx, ny))
        return candidates


class State:
    # State to store positions of left and right foot and whose turn it is next
    __slots__ = ['lx', 'ly', 'rx', 'ry', 'next_left']

    def __init__(self, lx, ly, rx, ry, next_left):
        self.lx = lx
        self.ly = ly
        self.rx = rx
        self.ry = ry
        self.next_left = next_left

    def __hash__(self):
        return hash((self.lx, self.ly, self.rx, self.ry, self.next_left))

    def __eq__(self, other):
        return (self.lx, self.ly, self.rx, self.ry, self.next_left) == (other.lx, other.ly, other.rx, other.ry, other.next_left)


class PriorityQueue:
    # A minimal wrapper for a priority queue used for Dijkstra
    def __init__(self):
        self._data = []
        self._entry_finder = {}
        self._counter = 0

    def push(self, priority, item):
        import heapq
        # Only push item if either not present or priority better
        if item in self._entry_finder:
            old_priority = self._entry_finder[item]
            if priority >= old_priority:
                return
        self._entry_finder[item] = priority
        heapq.heappush(self._data, (priority, self._counter, item))
        self._counter += 1

    def pop(self):
        import heapq
        while self._data:
            priority, _, item = heapq.heappop(self._data)
            if self._entry_finder.get(item, None) == priority:
                del self._entry_finder[item]
                return priority, item
        raise KeyError('pop from empty priority queue')

    def empty(self):
        return not bool(self._entry_finder)


def cliff_climbing_solver(cliff: Cliff) -> int:
    import sys

    # Initially, Jack stands on one foot on any start block, other foot somewhere??
    # The problem states Jack starts from the ground below cliff,
    # by stepping left or right foot on one start block at bottom row (y=h-1).
    # This means initially he only places one foot on a start block, and other foot is off.
    # However, the constraints imply states track both feet positions.
    # To simplify, we'll assume initial states have one foot on a start block,
    # the other foot on an imaginary position off the cliff (-1,-1).
    # But the problem mentions the left foot must be strictly left of right foot.
    # To match the constraints, we try all pairs of starts for left and right foot that satisfy lx<rx.
    # So we initialize pairs of start blocks with left foot < right foot, so both foot are on starts.
    # Because input shows 'S S ...' starting blocks on bottom row possibly adjacent.

    # We will treat initial states with left foot on S at (lx, h-1), right foot on S at (rx, h-1), lx < rx,
    # the next foot to move can be either left or right, but given he just placed both feet,
    # it's implied his next move is left or right. Problem: "After putting his left (or right) foot on a block,
    # he can only move his right (or left, respectively) foot." So, after placing both feet initially,
    # assume next move is left foot. We will search both variants (next_left = True or False) initially.

    # Cost to place foot on 'S' or 'T' is zero

    # We'll perform Dijkstra over states with:
    # state = (lx, ly, rx, ry, next_left)
    # dist[state] = minimal time to reach this configuration

    starts = cliff.starts
    if len(starts) < 2:
        # Need at least two start blocks to have both feet on
        # But problem states "by stepping his left or right foot on one of the blocks marked with 'S'"
        # So presumably initially only one foot is on the cliff? But constraints require left foot < right foot by x.
        # So to be consistent, let's allow initial states with one foot on 'S' block and the other foot off the cliff at (-1,-1)
        # and ignore constraints for that initial.
        # We perform a preliminary step to explore states starting from single-foot on S, other foot off:
        # But this complicates the model, instead we replicate the approach used in contest editorials:
        # "You start by placing either the left or the right foot on one block marked S in the bottom row,
        # the other foot is off the cliff (we'll represent impossible position -1,-1)."
        # To keep constraints (lx < rx), we'll represent off the cliff position as:
        # For left foot off cliff, lx = -1, for right foot off cliff rx = width (more than max)
        # so initially, possible initial states:
        # (lx, ly) = one 'S' block, (rx, ry) = (-1, -1) or vice versa, also next foot to move is the other foot
        # Constraints for off cliff will be relaxed just for initial positions.
        # We implement this with special logic.
        initial_states = []
        for (x, y) in starts:
            # left foot on S, right foot off
            initial_states.append(State(x, y, cliff.width, -1, False))
            # right foot on S, left foot off
            initial_states.append(State(-1, -1, x, y, True))

    else:
        # We start with both feet on different start blocks (lx < rx)
        initial_states = []
        for i in range(len(starts)):
            for j in range(i + 1, len(starts)):
                lx, ly = starts[i]
                rx, ry = starts[j]
                # next to move is left foot or right foot, try both
                initial_states.append(State(lx, ly, rx, ry, True))
                initial_states.append(State(lx, ly, rx, ry, False))

    # Dist map
    dist = {}
    from collections import deque

    # Priority queue for Dijkstra
    pq = PriorityQueue()

    def put_state(state, cost):
        if state in dist and dist[state] <= cost:
            return
        dist[state] = cost
        pq.push(cost, state)

    for st in initial_states:
        put_state(st, 0)

    while not pq.empty():
        cost, state = pq.pop()
        if dist[state] < cost:
            # Already have better cost recorded, skip
            continue

        # If either foot is on a target block, done
        if state.lx != -1 and state.ly != -1 and cliff.is_target(state.lx, state.ly):
            return cost
        if state.rx != -1 and state.ry != -1 and cliff.is_target(state.rx, state.ry):
            return cost

        # Determine which foot moves next
        next_left = state.next_left

        # Current positions
        lx, ly, rx, ry = state.lx, state.ly, state.rx, state.ry

        # Handle off cliff for constraints:
        # For off cliff left foot (-1,-1), treat position as (-1, -1)
        # For off cliff right foot (cliff.width, -1), treat as special

        # We generate candidates for next foot:
        candidates = []
        # special handling if left or right foot is off the cliff
        # if next foot is off cliff, it can be placed on any start block (since Jack only starts to climb by stepping on S)
        # so if next_left = True and left foot is off cliff, candidate positions are all S blocks in bottom row
        # similarly for right foot off cliff
        if next_left:
            if lx == -1 and ly == -1:
                # place left foot on an 'S' block
                candidates = cliff.starts
            else:
                candidates = cliff.neighbors_for_next_foot(lx, ly, rx, ry, True)
        else:
            if rx == cliff.width and ry == -1:
                candidates = cliff.starts
            else:
                candidates = cliff.neighbors_for_next_foot(lx, ly, rx, ry, False)

        for (nx, ny) in candidates:
            # compute new state's feet positions
            if next_left:
                n_lx, n_ly = nx, ny
                n_rx, n_ry = rx, ry
            else:
                n_lx, n_ly = lx, ly
                n_rx, n_ry = nx, ny

            # position validity was checked in neighbors_for_next_foot

            # compute cost to put foot on that block
            c = cliff.block_cost(nx, ny)
            if c is None:
                continue  # not walkable

            # create new state
            new_state = State(n_lx, n_ly, n_rx, n_ry, not next_left)
            new_cost = cost + c
            put_state(new_state, new_cost)

    # If all explored and no target reached
    return -1


class InputParser:
    def __init__(self):
        pass

    def parse_datasets(self):
        datasets = []
        while True:
            line = input().strip()
            if line == '':
                continue
            if line == '0 0':
                break
            w, h = map(int, line.split())
            grid = []
            for _ in range(h):
                row = input().strip().split()
                grid.append(row)
            datasets.append((w, h, grid))
        return datasets


class CliffClimbingApp:
    def __init__(self):
        self.parser = InputParser()

    def run(self):
        datasets = self.parser.parse_datasets()
        for w, h, grid in datasets:
            cliff = Cliff(w, h, grid)
            answer = cliff_climbing_solver(cliff)
            print(answer)


if __name__ == '__main__':
    # Prepare initial "off the cliff" positions used in initial states:
    # Set special values used in solver (needed outside class scope to be consistent)
    # We add these attributes to Cliff and State classes to avoid magic constants:
    Cliff.width = None
    Cliff.height = None
    app = CliffClimbingApp()
    app.run()