from collections import deque

# Constants defining the grid size and directions for waterdrops
N = 4
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

def in_grid(r, c):
    """Check if a cell coordinate is inside the grid."""
    return 0 <= r < N and 0 <= c < N

def simulate_chain_reaction(grid):
    """
    Simulate the chain reaction caused by bubbles blowing up.
    This involves repeatedly processing bubbles with state >= 5,
    creating waterdrops that move each second until they disappear
    by hitting bubbles or leaving the grid.

    This function modifies the grid in-place to the resulting state after
    all chain reactions have resolved.
    """
    while True:
        # Find bubbles that will blow up this second
        blowups = []
        for r in range(N):
            for c in range(N):
                if grid[r][c] >= 5:
                    blowups.append((r, c))

        if not blowups:
            # No more blow ups, chain reaction ends
            break

        # Remove blown-up bubbles and place 4 waterdrops initially in their cell
        for r, c in blowups:
            grid[r][c] = 0

        # Each waterdrop has position and direction, start from blowup cells
        waterdrops = []
        for r, c in blowups:
            for dr, dc in DIRECTIONS:
                # At the moment of blowup, waterdrops start from the original cell
                waterdrops.append((r, c, dr, dc))

        # Process waterdrops moving outwards each second
        while waterdrops:
            # For the next position of each waterdrop
            hits = {}  # track bubble hits for this time unit, keys=(r,c), value=hit count
            new_waterdrops = []
            for wr, wc, dr, dc in waterdrops:
                nr, nc = wr + dr, wc + dc
                if not in_grid(nr, nc):
                    # Waterdrop leaves the grid
                    continue
                if grid[nr][nc] > 0:
                    # Waterdrop hits a bubble, increment hits
                    hits[(nr, nc)] = hits.get((nr, nc), 0) + 1
                else:
                    # Waterdrop continues flying
                    new_waterdrops.append((nr, nc, dr, dc))

            # Apply hits to bubbles
            for (hr, hc), count in hits.items():
                grid[hr][hc] += count

            # If any bubbles now blow up, break to start next chain of blowups
            if any(grid[r][c] >= 5 for r, c in hits.keys()):
                # Stop current waterdrop movement, continue chain reaction loop
                break
            # Otherwise continue waterdrops next second
            waterdrops = new_waterdrops

def serialize(grid):
    """Convert grid to tuple of tuples to use as state key in BFS."""
    return tuple(tuple(row) for row in grid)

def is_empty(grid):
    """Check if the grid has no bubbles."""
    for r in range(N):
        for c in range(N):
            if grid[r][c] > 0:
                return False
    return True

def minimum_clicks(initial_grid):
    """
    Compute the minimum number of clicks needed to blow up all bubbles,
    or return -1 if it requires more than 5 clicks.
    We use BFS over states. Each click changes the state by either
    increasing a bubble by 1, or creating a bubble (state=1) in an empty cell,
    then immediately processing chain reactions.
    """
    start_state = serialize(initial_grid)
    queue = deque()
    queue.append((start_state, 0))  # (grid_state, clicks)
    visited = {start_state}

    while queue:
        state, clicks = queue.popleft()
        if clicks > 5:
            # Exceeded maximum allowed clicks
            return -1

        # Deserialize state into grid to manipulate
        grid = [list(row) for row in state]

        if is_empty(grid):
            # Solved
            return clicks

        # Try clicking each cell
        for r in range(N):
            for c in range(N):
                new_grid = [row[:] for row in grid]
                if new_grid[r][c] == 0:
                    # Empty cell: create a bubble with state 1
                    new_grid[r][c] = 1
                else:
                    # Bubble exists: increase state by 1
                    new_grid[r][c] += 1

                # Simulate chain reaction caused by modifications
                simulate_chain_reaction(new_grid)

                nstate = serialize(new_grid)
                if nstate not in visited:
                    visited.add(nstate)
                    queue.append((nstate, clicks + 1))

    # Cannot solve in 5 clicks or fewer
    return -1

def main():
    # Read initial grid from input
    grid = [list(map(int, input().split())) for _ in range(N)]
    result = minimum_clicks(grid)
    print(result)

if __name__ == "__main__":
    main()