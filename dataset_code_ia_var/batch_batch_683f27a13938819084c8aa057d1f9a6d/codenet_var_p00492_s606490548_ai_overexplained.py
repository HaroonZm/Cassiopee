import sys

def solve(data, w, h):
    # 'invisible_area' is a set to store coordinates (x, y) of grid cells which are 'invisible' (not exposed to outer space)
    invisible_area = set()
    # 'visible_area' is a set to store all cells that are connected to outside space
    visible_area = set()
    # 'visited' keeps track of all already explored grid cells to avoid redundant processing
    visited = set()

    # Iterate over each cell in the grid using a nested for-loop
    # 'y' varies along the height (rows), 'x' along the width (columns)
    for y in range(h):
        for x in range(w):
            # Mark this cell as visited - ensures we never process a cell more than once
            visited.add((x, y))

            # If current cell contains '1', it's a wall/obstacle and cannot expand into it
            if data[y][x] == 1:
                invisible_area.add((x, y))

            # 'is_visible' is a boolean to keep track of whether the current region connects to the outer boundary
            is_visible = False

            # If the current cell is already known as 'invisible' or 'visible', move to next cell
            if (x, y) in invisible_area or (x, y) in visible_area:
                continue

            # 'area' is the set of all connected cells forming one contiguous empty ('0') region
            area = {(x, y)}
            # 'stack' is used for DFS (Depth-First Search), initialized with current cell
            stack = [(x, y)]

            # Classical DFS algorithm to find all connected empty cells starting from (x, y)
            while stack:
                # Pop the last element from stack to process it (LIFO order typical of DFS)
                cx, cy = stack.pop()
                # Mark this cell as visited - prevents revisiting
                visited.add((cx, cy))

                # Determine hexagonal neighbor directions:
                # This is required because the grid is not rectangular; neighbors depend on parity of row (cy)
                # For even-numbered rows (cy % 2 == 0) - use one pattern, else use another
                if cy % 2 == 0:
                    # Even row neighbors (6 directions for hex grid)
                    dxy = (
                        (cx,     cy-1),   # top neighbor
                        (cx+1,   cy-1),   # top-right neighbor
                        (cx-1,   cy),     # left neighbor
                        (cx+1,   cy),     # right neighbor
                        (cx,     cy+1),   # bottom neighbor
                        (cx+1,   cy+1)    # bottom-right neighbor
                    )
                else:
                    # Odd row neighbors (different offsets for hex grid)
                    dxy = (
                        (cx-1,   cy-1),   # top-left neighbor
                        (cx,     cy-1),   # top neighbor
                        (cx-1,   cy),     # left neighbor
                        (cx+1,   cy),     # right neighbor
                        (cx-1,   cy+1),   # bottom-left neighbor
                        (cx,     cy+1)    # bottom neighbor
                    )

                # Process all neighbors of current cell
                for nx, ny in dxy:
                    # If neighbor is outside grid boundary, mark the region as 'visible'
                    if not (0 <= nx < w) or not (0 <= ny < h):
                        is_visible = True

                    # Only consider grid cells that are:
                    # - Inside the grid (boundary check)
                    # - Are not obstacles (data[ny][nx] == 0)
                    # - Have not been visited yet
                    if 0 <= nx < w and 0 <= ny < h and data[ny][nx] == 0 and (nx, ny) not in visited:
                        # Add to stack for DFS, mark as part of current area
                        stack.append((nx, ny))
                        area.add((nx, ny))

            # After processing the connected region (possibly more than one cell):
            if is_visible:
                # If any part connects to the outside (touches boundary), mark the entire region as 'visible'
                visible_area |= area  # |= is equivalent to set union
            else:
                # Else, mark region as fully surrounded and 'invisible'
                invisible_area |= area

    # Now, count the answer for the problem:
    # This counts the number of wall 'edges' that are 'visible' from the outside

    ans = 0  # Initialize the result accumulator

    # Loop through every cell:
    for cy in range(h):         # Row index
        for cx in range(w):     # Column index
            # Only consider cells in the grid that contain a wall ('1')
            if data[cy][cx] == 1:
                # Determine directions for the 6 neighbors as per hex grid
                if cy % 2 == 0:
                    dxy = (
                        (cx,     cy-1),
                        (cx+1,   cy-1),
                        (cx-1,   cy),
                        (cx+1,   cy),
                        (cx,     cy+1),
                        (cx+1,   cy+1)
                    )
                else:
                    dxy = (
                        (cx-1,   cy-1),
                        (cx,     cy-1),
                        (cx-1,   cy),
                        (cx+1,   cy),
                        (cx-1,   cy+1),
                        (cx,     cy+1)
                    )
                # For each neighbor direction:
                # If the adjacent cell in 'dxy' is part of an invisible area (full), it is not an exposed edge
                # Initial wall has 6 possible edges, subtract the number of edges that touch other wall cells
                ans += 6 - sum((nx, ny) in invisible_area for nx, ny in dxy)
    # Return the total count of visible wall edges
    return ans

def main(args):
    # Read width and height from a single line, splitting by default whitespace and converting to integers
    w, h = map(int, input().split())
    # For each row (height), read a line, split it, convert entries to int, form a list of lists (2D grid)
    data = [list(map(int, input().split())) for _ in range(h)]
    # Compute the answer using the solve function, pass in data, w, h
    ans = solve(data, w, h)
    # Output the result as per required specification
    print(ans)

# The following boilerplate checks if this file is being run as a standalone program
# If so, call the 'main' function, passing any command-line arguments (excluding script name itself)
if __name__ == '__main__':
    main(sys.argv[1:])