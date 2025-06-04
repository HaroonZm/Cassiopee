from collections import deque

def neighbors(pos, n):
    r, c = pos
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                yield (nr, nc)

def move_positions(pos, n):
    # all 8 adjacent positions
    r, c = pos
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                yield (nr, nc)

def infection_transition(grid, vehicle_pos, n):
    # grid: tuple of strings (immutable)
    # vehicle_pos: position of vehicle (r,c)
    # return new grid (tuple of strings) after transition
    # Note: vehicle_pos area does NOT change
    # Also, vehicle acts as infected for neighbors although it is uninfected itself

    # Precompute infection count for each cell:
    # for counting adjacent infected areas, the vehicle position counts as infected area
    new_grid = [list(row) for row in grid]

    # Track infected positions (exclude vehicle position; we use grid directly)
    infected = set()
    for r in range(n):
        for c in range(n):
            if (r,c) != vehicle_pos and grid[r][c] == '#':
                infected.add((r,c))
    # For counting infected neighbors, vehicle pos counts as infected, even if uninfected
    infected.add(vehicle_pos)

    # We'll compute next state for every cell except vehicle_pos
    for r in range(n):
        for c in range(n):
            if (r, c) == vehicle_pos:
                # protected by vehicle; area never infected here
                new_grid[r][c] = '.'
                continue
            cnt = 0
            for nr, nc in neighbors((r,c), n):
                if (nr,nc) in infected:
                    cnt += 1
            current = grid[r][c]
            if current == '#':
                # infected stays infected if 2 or 3 adjacent infected areas
                if cnt == 2 or cnt == 3:
                    new_grid[r][c] = '#'
                else:
                    new_grid[r][c] = '.'
            else:
                # uninfected area becomes infected if exactly 3 adjacent infected areas
                if cnt == 3:
                    new_grid[r][c] = '#'
                else:
                    new_grid[r][c] = '.'

    return tuple(''.join(row) for row in new_grid)

def serialize(grid, vehicle_pos):
    # To store visited states: (vehicle_pos, grid_str)
    return (vehicle_pos, grid)

def all_disinfected(grid):
    for row in grid:
        if '#' in row:
            return False
    return True

def solve(dataset):
    n = dataset[0]
    grid_lines = dataset[1:]
    grid = tuple(grid_lines)
    vehicle_pos = None
    for r in range(n):
        for c in range(n):
            if grid[r][c] == '@':
                vehicle_pos = (r,c)
                # Replace '@' by '.' in the grid parsed
                row_list = list(grid[r])
                row_list[c] = '.'
                grid = grid[:r] + (''.join(row_list),) + grid[r+1:]
                break
        if vehicle_pos is not None:
            break

    if all_disinfected(grid):
        # no steps needed
        return 0

    queue = deque()
    visited = set()

    start_state = serialize(grid, vehicle_pos)
    queue.append( (grid, vehicle_pos, 0) )
    visited.add(start_state)

    while queue:
        current_grid, current_pos, steps = queue.popleft()

        # vehicle must move to one of eight adjacent free (uninfected) areas
        for nxt_pos in move_positions(current_pos, n):
            nr, nc = nxt_pos
            if current_grid[nr][nc] == '#':
                # cannot move to infected area
                continue

            # after move, apply infection transition (except vehicle pos)
            nxt_grid = infection_transition(current_grid, nxt_pos, n)
            # check if all disinfected
            if all_disinfected(nxt_grid):
                return steps + 1
            state = serialize(nxt_grid, nxt_pos)
            if state not in visited:
                visited.add(state)
                queue.append((nxt_grid, nxt_pos, steps+1))

    return -1

def main():
    import sys
    lines = sys.stdin.read().splitlines()
    idx = 0
    while True:
        if idx >= len(lines):
            break
        n_line = lines[idx].strip()
        idx += 1
        if n_line == '0':
            break
        n = int(n_line)
        dataset = [n]
        for _ in range(n):
            dataset.append(lines[idx])
            idx += 1
        print(solve(dataset))

if __name__ == '__main__':
    main()