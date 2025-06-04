from collections import deque
import sys

def solve():
    # Directions for movement: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Read input until "0 0 0" is encountered
    while True:
        line = ''
        # Skip empty lines if any
        while line.strip() == '':
            line = sys.stdin.readline()
            if not line:
                return
        w, h, n = map(int, line.strip().split())
        if w == 0 and h == 0 and n == 0:
            break

        grid = []
        for _ in range(h):
            grid.append(list(sys.stdin.readline().rstrip('\n')))

        # Map letters for ghosts: the first n lowercase letters indicate ghosts
        # and their corresponding uppercase letters indicate destinations
        ghosts_pos = [None]*n  # store current positions of ghosts
        targets_pos = [None]*n  # store target positions of ghosts

        # We will map ghost letters 'a', 'b', 'c' to indices 0,1,2
        # Similarly for their uppercase targets 'A', 'B', 'C'
        # Scan the grid to find positions of these ghosts (initial and target)
        for i in range(h):
            for j in range(w):
                ch = grid[i][j]
                if 'a' <= ch <= 'z':
                    idx = ord(ch) - ord('a')
                    if idx < n:
                        ghosts_pos[idx] = (i, j)
                elif 'A' <= ch <= 'Z':
                    idx = ord(ch) - ord('A')
                    if idx < n:
                        targets_pos[idx] = (i, j)

        # Preprocessing: collect all corridor cells for movement validation
        # Walls are '#', corridor cells are anything else (including spaces and ghost chars)
        # We will use a grid of booleans indicating corridor cells
        is_corridor = [[False]*w for _ in range(h)]
        for i in range(h):
            for j in range(w):
                if grid[i][j] != '#':
                    is_corridor[i][j] = True

        # State: positions of all ghosts (tuple of coordinates)
        # We want to find minimal steps to move all ghosts from ghosts_pos to targets_pos
        # BFS over states, at each step each ghost can stay or move one step to an adjacent corridor cell
        # Conditions:
        # - No two ghosts occupy the same cell after move
        # - No pair swap positions in one step
        # At each step, we move simultaneously all ghosts

        # To implement the no-swap condition: if ghost A moves to ghost B's previous pos and ghost B moves to ghost A's previous pos in the same step, forbidden

        # BFS variables
        start_state = tuple(ghosts_pos)
        goal_state = tuple(targets_pos)

        # Visited set to avoid repeated states
        visited = set()
        visited.add(start_state)

        queue = deque()
        queue.append((start_state, 0))  # (state, steps)

        # Generate all possible moves for ghosts:
        # Each ghost can move to one of 5 positions: stay, or move to one of adjacent corridor cells
        # Generate moves for each ghost, then consider all combinations (up to 5^n)
        # n ≤ 3, so at most 125 states per iteration (manageable)

        while queue:
            state, steps = queue.popleft()

            # Check if goal reached
            if state == goal_state:
                print(steps)
                break

            # Generate possible next positions for each ghost
            possible_moves = []
            for pos in state:
                moves_for_ghost = []
                i, j = pos
                # ghost can stay
                moves_for_ghost.append((i, j))
                # ghost can move to adjacent corridor cells
                for di, dj in directions:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < h and 0 <= nj < w and is_corridor[ni][nj]:
                        moves_for_ghost.append((ni, nj))
                possible_moves.append(moves_for_ghost)

            # Iterate over Cartesian product of all ghosts' moves
            # To avoid importing product from itertools for minimal code, implement simple recursive combination

            next_states = []

            def backtrack(idx, current_positions):
                if idx == n:
                    # Check conditions on the move:
                    # 1) No duplicate final positions
                    # 2) No pair of ghosts swapped positions (i.e. ghosts A and B do not end in each other's previous positions simultaneously)
                    # current_positions is tuple of positions after the move
                    positions_set = set(current_positions)
                    if len(positions_set) < n:
                        # some ghosts occupy same cell -> invalid
                        return
                    # Check no swaps:
                    # For every pair of ghosts i < j:
                    # if current_positions[i] == state[j] and current_positions[j] == state[i]: invalid
                    for i1 in range(n):
                        for j1 in range(i1+1, n):
                            if current_positions[i1] == state[j1] and current_positions[j1] == state[i1]:
                                return
                    # Valid next state
                    next_states.append(tuple(current_positions))
                    return

                for pos_to in possible_moves[idx]:
                    backtrack(idx+1, current_positions + [pos_to])

            backtrack(0, [])

            # For each valid next state, if not visited, add to queue
            for nxt in next_states:
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps+1))

if __name__ == '__main__':
    solve()