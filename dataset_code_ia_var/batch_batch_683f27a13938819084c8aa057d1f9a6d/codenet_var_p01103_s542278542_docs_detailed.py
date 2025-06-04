import sys

# Extend the maximum recursion limit to prevent potential stack overflows in deeply recursive computations
sys.setrecursionlimit(10**9)

# Fast input using sys.stdin.readline, which is preferable for large input sizes
input = sys.stdin.readline

def calcVolume(L, R, T, B, min_wall):
    """
    Calculate the total volume of the pond that can be formed within the given boundaries.

    Args:
        L (int): Left boundary (inclusive) of the pond area (column index).
        R (int): Right boundary (inclusive) of the pond area (column index).
        T (int): Top boundary (inclusive) of the pond area (row index).
        B (int): Bottom boundary (inclusive) of the pond area (row index).
        min_wall (int): Height of the shortest surrounding wall (minimum boundary value).

    Returns:
        int: Total water volume that the defined pond can store.
    """
    ret = 0  # Initialize total volume
    for w in range(L, R + 1):
        for h in range(B, T + 1):
            # Add the difference between the minimum wall height and the current height
            ret += (min_wall - garden[h][w])
    return ret

def pondsVolume(L, R, T, B):
    """
    Check if a pond can be created in the specified area and calculate its volume.

    If the lowest surrounding wall is not higher than the highest point in the pond area,
    a pond cannot be formed.

    Args:
        L (int): Left boundary (inclusive) of the pond area (column index).
        R (int): Right boundary (inclusive) of the pond area (column index).
        T (int): Top boundary (inclusive) of the pond area (row index).
        B (int): Bottom boundary (inclusive) of the pond area (row index).

    Returns:
        int: Total water volume if a pond can be formed; otherwise -1.
    """
    # Find the maximum height within the pond area itself
    max_in_pond = 0
    for w in range(L, R + 1):
        for h in range(B, T + 1):
            max_in_pond = max(max_in_pond, garden[h][w])

    # Find the minimum height among all surrounding wall cells
    min_wall = float('inf')
    # Top and bottom walls
    for w in range(L - 1, R + 2):
        min_wall = min(min_wall, garden[B - 1][w], garden[T + 1][w])
    # Left and right walls (excluding the corners counted above)
    for h in range(B - 1, T + 2):
        min_wall = min(min_wall, garden[h][L - 1], garden[h][R + 1])

    # If the minimum surrounding wall is lower or equal to the highest cell inside, no pond is possible
    if min_wall <= max_in_pond:
        return -1
    else:
        # Otherwise, compute pond volume
        return calcVolume(L, R, T, B, min_wall)

# Main routine: process each case until a case with d==0 is encountered
while True:
    # Read dimensions: d = number of rows (height), w = number of columns (width)
    d, w = map(int, input().split())
    if d == 0:
        # Sentinel value to end the loop
        break

    # Read the garden layout: a 2D array of heights
    garden = [list(map(int, input().split())) for _ in range(d)]

    ans = 0  # Track the largest possible pond volume

    # Brute-force all possible subrectangles within bounds not touching the outer wall
    for L in range(1, w - 1):
        for B in range(1, d - 1):
            for R in range(L, w - 1):
                for T in range(B, d - 1):
                    # Calculate the maximal pond for each valid rectangle
                    ans = max(ans, pondsVolume(L, R, T, B))
    # Output the answer for the current case
    print(ans)