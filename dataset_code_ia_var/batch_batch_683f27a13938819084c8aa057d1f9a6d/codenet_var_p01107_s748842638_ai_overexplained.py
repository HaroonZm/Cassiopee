# Define the list 'dd' containing 4 tuples, each representing a direction vector for movement on a 2D grid.
# The directions are: up, left, down, right, ordered as (-1,0):left, (0,-1):up, (1,0):right, (0,1):down.
dd = [(-1, 0), (0, -1), (1, 0), (0, 1)]

# Start an infinite loop with 'while 1', which is equivalent to 'while True'.
# It will continue to execute until explicitly broken from inside.
while 1:
    # Read a line of input from the user, split it by whitespace, map both values to integers.
    # Assign the first value to 'n' (number of rows), second value to 'm' (number of columns).
    n, m = map(int, input().split())

    # Check if both 'n' and 'm' are zero. 'n == m == 0' is syntactic sugar for 'n == 0 and m == 0'.
    # If true, break the loop and end the program.
    if n == m == 0:
        break

    # Build the grid 'C' as a list of lists, one inner list per row.
    # For each row index from 0 to n-1 (using 'for i in range(n)'), read a line of input string.
    # Append one extra character '#' to each row to avoid index errors on the right edge,
    # then convert the row string + '#' into a list of single-character strings (so we can index and mutate).
    # Add an extra row at the bottom consisting only of '#' characters. Length is 'm+2' to cover all columns and extra border.
    C = [list(input() + "#") for i in range(n)] + ["#"*(m+2)]

    # Initialize a 2D list 'used' with zeros, dimensions n x m.
    # Each element in 'used' will track if a grid cell has been visited if necessary, but not used in this code.
    used = [[0]*m for i in range(n)]

    # Define the function 'move' which attempts to traverse the grid from a start position (x0, y0)
    # to an end position (x1, y1), following the boundary with a given initial direction 'd'.
    # The direction 'd' is an integer: 0=left, 1=up, 2=right, 3=down.
    def move(x0, y0, x1, y1, d):
        # Initialize 'x' and 'y' to starting coordinates.
        x = x0
        y = y0
        # 'moved' is a flag set to 1 if any movement occurred in this path following.
        moved = 0
        # 'cnt' counts the number of steps taken in the outer while loop to avoid infinite cycles.
        cnt = 0
        # 'history' will keep track of all positions visited in the path.
        history = []
        # Continue moving while the current position is not the destination (x1, y1).
        while x != x1 or y != y1:
            # Increment the step counter.
            cnt += 1
            # Compute direction vectors for the left (relative to current facing)
            # 'd-3' modulo 4 gives the index of the direction to the left.
            rx, ry = dd[d-3]
            # 'dd[d]' gives the vector for current facing direction.
            dx, dy = dd[d]
            # If we can go forward (the cell ahead is not '#') and cannot go left (blocked by '#'), go forward.
            while C[y+dy][x+dx] != '#' and C[y+ry][x+rx] == '#':
                x += dx
                y += dy
                # Add the current position to history.
                history.append([x, y])
                # Set 'moved' flag, because we have left the initial position.
                moved = 1
            # If we cannot move forward (cell ahead is '#'), and the cell to the left is also '#', rotate left (counterclockwise).
            if C[y+dy][x+dx] == '#' and C[y+ry][x+rx] == '#':
                d = (d - 1) % 4
            # Else if the cell to the left is open ('#' not there), rotate right (clockwise) and step into it.
            elif C[y+ry][x+rx] != '#':
                d = (d + 1) % 4
                x += rx
                y += ry
                history.append([x, y])
            # If we have at least moved once (moved is 1), or have looped more than 4 times without escape;
            # and are back at our starting cell, this trip is invalid (likely stuck in a loop), so return 0.
            if (moved or cnt > 4) and x == x0 and y == y0:
                return 0
        # After ending loop (target reached), mark all cells in history except the last one as '#' in 'C'
        # (these are considered visited and blocked for subsequent traversals).
        for x, y in history[:-1]:
            C[y][x] = '#'
        # Success, return 1.
        return 1

    # Chain together four calls to 'move' to walk the four sides of the grid's border.
    # 1st: from (0,0) (top-left) to (0,n-1) (bottom-left), initially facing 'down' (3)
    # 2nd: from (0,n-1) to (m-1,n-1) (bottom-left to bottom-right), initially facing 'right' (2)
    # 3rd: from (m-1,n-1) to (m-1,0) (bottom-right to top-right), initially facing 'up' (1)
    # 4th: from (m-1,0) back to (0,0), initially facing 'left' (0)
    # Only if all segments can be traversed without error (all move return 1), print "YES", else print "NO".
    if move(0, 0, 0, n-1, 3) and move(0, n-1, m-1, n-1, 2) and move(m-1, n-1, m-1, 0, 1) and move(m-1, 0, 0, 0):
        print("YES")
    else:
        print("NO")