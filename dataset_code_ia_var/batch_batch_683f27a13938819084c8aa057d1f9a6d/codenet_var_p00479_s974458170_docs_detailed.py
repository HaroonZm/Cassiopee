def getN():
    """
    Reads an integer from standard input.

    Returns:
        int: The integer value provided by the user.
    """
    return int(input())


def getlist():
    """
    Reads a line of space-separated integers from standard input.

    Returns:
        list: A list of integers entered by the user.
    """
    return list(map(int, input().split()))


def solve(n, pos):
    """
    Determines the color ID for a given position in an n x n grid.

    The function normalizes the coordinates (x, y) onto the closest distance
    to the border and computes a color based on this minimum distance.
    The colors cycle through integers 1, 2, 3.

    Args:
        n (int): The size of the grid (n x n).
        pos (list or tuple): A pair [x, y] representing the position
            (with 1-based indexing).

    Returns:
        int: The color ID at the given position (1, 2, or 3).
    """
    # Extract x and y from the pos argument
    x, y = pos

    # Symmetrize x: bring it as close as possible to the top/bottom border
    if x > n // 2:
        x = n - x + 1

    # Symmetrize y: bring it as close as possible to the left/right border
    if y > n // 2:
        y = n - y + 1

    if x == y:
        # On a diagonal equidistant from border: color based only on x (or y)
        color = ((x - 1) % 3) + 1
    else:
        # Off diagonal: color based on the minimum distance to the borders
        definitive = min(x, y)
        color = ((definitive - 1) % 3) + 1

    return color


# Read the grid size
n = getN()
# Read the number of queries
k = getN()

# Process each query and output the color
for i in range(k):
    pos = getlist()  # Read current query position
    print(solve(n, pos))