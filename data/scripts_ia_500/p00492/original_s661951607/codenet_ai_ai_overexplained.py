def solve():
    # Import deque from collections module.
    # deque is a double-ended queue which allows appending and popping elements efficiently from both ends.
    from collections import deque

    # Import deepcopy function from copy module.
    # deepcopy is used to create a new compound object and recursively add copies of objects found in the original.
    from copy import deepcopy

    # Read input line consisting of two integers separated by space,
    # map each part of the input into an integer, and unpack them into variables W and H.
    # W represents width, H represents height.
    W, H = map(int, input().split())

    # Build a 2D list 'a' to represent a grid with borders.
    # The grid is created by:
    # - Adding a row of zeros of length (W+2) at the top.
    # - Reading H lines from input.
    #   For each line, add a zero at the beginning and end, then convert the line into a list of integers.
    # - Adding a row of zeros of length (W+2) at the bottom.
    #
    # The result is a grid of size (H+2) rows x (W+2) columns, where the outermost border cells are zeros.
    a = [[0]*(W+2)] + [list(map(int, ("0 "+input()+" 0").split())) for _ in [0]*H] + [[0]*(W+2)]

    # Initialize result variable to zero.
    # This variable will accumulate the sum of certain grid values during processing.
    result = 0

    # Create a deep copy of the grid 'a' called 'visited'.
    # This copy will be modified to keep track of which cells have been visited during traversal.
    visited = deepcopy(a)

    # Initialize a deque object 'dq' with a single tuple element (0, 0),
    # representing the starting coordinates on the grid.
    dq = deque([(0, 0)])

    # For performance optimization, bind the methods 'append' and 'popleft' of the deque
    # to local variables for faster access during the loop.
    append, popleft = dq.append, dq.popleft

    # Enter a loop that continues while there are still elements in the deque 'dq'.
    # Each iteration processes one position on the grid.
    while dq:
        # Remove and return the leftmost element (x, y coordinates) from dq.
        x, y = popleft()

        # Define the neighbors for the current cell depending on the parity of y.
        # Because the grid represents hexagonal adjacency in a staggered layout,
        # neighbors are adjusted for even and odd rows separately.
        # The neighbors list contains tuples of relative coordinates (dx, dy).
        #
        # For horizontal neighbors, always consider left (-1, 0) and right (1, 0).
        #
        # For even rows (y is even number):
        # Include neighbors at top-left (-1, -1), top (0, -1), bottom-left (-1, 1), bottom (0, 1).
        #
        # For odd rows (y is odd number):
        # Include neighbors at top (0, -1), top-right (1, -1), bottom (0, 1), bottom-right (1, 1).
        neighbour = [(-1, 0), (1, 0)] + ([(-1, -1), (0, -1), (-1, 1), (0, 1)] if y%2 == 0 else [(0, -1), (1, -1), (0, 1), (1, 1)])

        # For each neighboring cell coordinate (dx, dy):
        for dx, dy in neighbour:
            # Calculate absolute neighbor coordinates by adding relative displacement to current position.
            nx, ny = dx + x, dy + y

            # Check if neighbor coordinates (nx, ny) are within grid bounds.
            # The grid has indices from 0 up to W+1 horizontally and 0 up to H+1 vertically.
            if 0 <= nx < W + 2 and 0 <= ny < H + 2:
                # Accumulate the value found at the neighbor cell in the 'a' grid into the result variable.
                # This counts the sum of values for all neighbors of the current cell.
                result += a[ny][nx]

        # Second loop over neighbors to mark visited and append new water cells to process.
        for dx, dy in neighbour:
            nx, ny = x + dx, y + dy  # Neighbor coordinates as before

            # Check if neighbor is within bounds.
            if 0 <= nx < W + 2 and 0 <= ny < H + 2:
                # If the neighbor cell in the visited grid is still zero, it means not visited.
                if visited[ny][nx] == 0:
                    # Mark neighbor cell as visited by setting it to 1 in 'visited' grid.
                    visited[ny][nx] = 1

                    # Append the neighbor coordinates to the right side of the deque to process later.
                    append((nx, ny))

    # After the BFS traversal and summation is complete, print the final accumulated result.
    print(result)

# Check if this script is being run as the main program, not being imported as a module.
# If it is the main module, call the solve() function to execute the program logic.
if __name__ == "__main__":
    solve()