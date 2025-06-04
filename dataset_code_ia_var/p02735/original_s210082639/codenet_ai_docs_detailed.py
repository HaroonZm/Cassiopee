def solve():
    """
    Reads input for the grid (height H, width W, and H lines of field layout), and prints the minimum
    number of color changes (from '.' to '#') needed to traverse from the top-left to bottom-right of the grid.
    """
    # Read the dimensions of the grid (H: rows, W: columns)
    H, W = map(int, input().split())

    # Read the grid layout, where each cell is either '.' or '#'
    # Each row of the grid is stored as a list of characters
    field = [list(input()) for _ in range(H)]

    # Initialize the DP table.
    # dp[h][w] will store the minimum number of '.' to '#' transitions
    # (color changes) required to reach cell (h, w) from (0, 0)
    dp = [[0] * W for _ in range(H)]

    # Initialize the first column (except the top-left cell)
    # For each cell in the first column, check if there is a color change from above
    for h in range(1, H):
        if field[h-1][0] == '.' and field[h][0] == '#':
            # If moving from a '.' to a '#', increment transition count
            dp[h][0] = dp[h-1][0] + 1
        else:
            # Otherwise, carry over previous transition count
            dp[h][0] = dp[h-1][0]

    # Initialize the first row (except the top-left cell)
    # For each cell in the first row, check if there is a color change from the left
    for w in range(1, W):
        if field[0][w-1] == '.' and field[0][w] == '#':
            # If moving from a '.' to a '#', increment transition count
            dp[0][w] = dp[0][w-1] + 1
        else:
            # Otherwise, carry over previous transition count
            dp[0][w] = dp[0][w-1]

    # Fill the rest of the DP table
    for w in range(1, W):
        for h in range(1, H):
            # Calculate number of transitions if coming from above (upward)
            from_upward = dp[h-1][w]
            if field[h-1][w] == '.' and field[h][w] == '#':
                from_upward += 1

            # Calculate number of transitions if coming from the left
            from_left = dp[h][w-1]
            if field[h][w-1] == '.' and field[h][w] == '#':
                from_left += 1

            # Take the minimum of the two possible routes to this cell
            dp[h][w] = min(from_upward, from_left)

    # The answer is the computed value at the bottom-right cell
    ans = dp[H-1][W-1]

    # If the starting cell is '#', we need to count this initial transition as well
    if field[0][0] == '#':
        ans += 1

    # Output the result
    print(ans)

if __name__ == '__main__':
    solve()