from collections import deque

# Directions for vehicle moves and adjacency (8 directions)
DIRECTIONS = [(-1,-1), (-1,0), (-1,1),
              (0,-1),          (0,1),
              (1,-1),  (1,0),  (1,1)]

def get_adjacent_positions(x, y, n):
    """Return list of valid adjacent positions (including diagonals) around (x,y) within grid size n."""
    adj = []
    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            adj.append((nx, ny))
    return adj

def next_infection_state(grid, vehicle_pos):
    """
    Compute the next infection state of the grid after one time step,
    given the vehicle position.
    
    Rules:
    - At each time step, we first move the vehicle then update states.
    - Vehicle occupies exactly one cell, not infected, 
      protects its current cell from getting infected,
      also counts as infected for adjacency calculation.
    - All cells except vehicle cell update according to rules.
    
    Infection rules for cell c:
    Count vehicle as infected for adjacency if c != vehicle cell.
    For c != vehicle cell:
        infected neighbor count = number of adjacent '#' + (1 if vehicle adjacent else 0)
        If c is infected (#) and neighbors infected count in {2,3} => keep infected (#)
        If c is uninfected (.) and neighbors infected count == 3 => become infected (#)
        else become free (.)
    For vehicle cell (vx, vy):
        It never becomes infected as long as vehicle stays (always '.')
    """
    n = len(grid)
    new_grid = [list(row) for row in grid]
    vx, vy = vehicle_pos
    
    # Precompute adjacency infected counts for all cells, including vehicle influence
    # We'll count infected neighbors + vehicle if adjacent
    infected_positions = set()
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '#':
                infected_positions.add((i,j))
    
    # Vehicle counts as infected for adjacency (but vehicle cell never infected)
    # For each cell, count infected neighbors + vehicle if adjacent
    
    # Precompute adjacency infected counts (for each cell)
    def infected_adj_count(x,y):
        count = 0
        for nx, ny in get_adjacent_positions(x, y, n):
            if (nx, ny) in infected_positions:
                count += 1
        # Add vehicle as infected neighbor if it's adjacent (except for vehicle cell itself)
        if (abs(x - vx) <= 1 and abs(y - vy) <= 1) and (x,y) != (vx, vy):
            count += 1
        return count
    
    for i in range(n):
        for j in range(n):
            if (i,j) == (vx, vy):
                # Vehicle cell never infected (always '.')
                new_grid[i][j] = '.'
            else:
                c = grid[i][j]
                neighbors = infected_adj_count(i,j)
                if c == '#':
                    # infected stays infected with 2 or 3 neighbors infected
                    new_grid[i][j] = '#' if neighbors in (2,3) else '.'
                else:
                    # uninfected becomes infected with exactly 3 infected neighbors
                    new_grid[i][j] = '#' if neighbors == 3 else '.'
    return tuple(''.join(row) for row in new_grid)

def find_vehicle_position(grid):
    """Find the vehicle '@' position in the grid."""
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '@':
                return (i,j)
    return None

def can_move_to(grid, x, y):
    """Check if the vehicle can move to the cell (x,y). It must be free ('.' or '@')."""
    # '@' will not appear after first step, but just in case
    return grid[x][y] != '#'

def solve(dataset):
    """
    Solve the problem for one dataset.
    Use BFS on states:
    state = (grid_state_as_tuple_of_strings, vehicle_position)
    
    For each step:
      - Move vehicle to one of 8 adjacent cells (not infected, not out of bounds, not same cell)
      - Update infection states for new grid
      - Check if all cells are free (no '#')
    
    Return min steps or -1 if impossible.
    """
    n = len(dataset)
    initial_grid = tuple(dataset)
    vehicle_pos = find_vehicle_position(initial_grid)
    
    # Normalize grid: replace '@' by '.' because position is tracked separately
    grid_list = [list(row) for row in initial_grid]
    vx, vy = vehicle_pos
    grid_list[vx][vy] = '.'
    init_grid = tuple(''.join(row) for row in grid_list)
    
    # BFS setup
    # Visited will hold (grid_state, vehicle_pos) to avoid cycles
    visited = set()
    queue = deque()
    # state = (grid, (vx,vy), steps)
    queue.append((init_grid, vehicle_pos, 0))
    visited.add((init_grid, vehicle_pos))
    
    while queue:
        grid, (vx, vy), steps = queue.popleft()
        
        # Check goal: no infected areas
        if all('#' not in row for row in grid):
            return steps
        
        # Try all 8 moves for vehicle
        for dx, dy in DIRECTIONS:
            nx, ny = vx + dx, vy + dy
            # Must be inside the grid
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            # Must move (can't stay in same place)
            if (nx, ny) == (vx, vy):
                continue
            # Vehicle cannot move to infected cell
            if not can_move_to(grid, nx, ny):
                continue
            # Compute next infection grid after vehicle moves to (nx,ny)
            next_grid = next_infection_state(grid, (nx, ny))
            # Check if visited
            state = (next_grid, (nx, ny))
            if state not in visited:
                visited.add(state)
                queue.append((next_grid, (nx, ny), steps+1))
    return -1

def main():
    import sys
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        n_line = input_lines[idx].strip()
        idx += 1
        if n_line == '0':
            break
        n = int(n_line)
        dataset = []
        for _ in range(n):
            dataset.append(input_lines[idx])
            idx += 1
        result = solve(dataset)
        print(result)

if __name__ == "__main__":
    main()