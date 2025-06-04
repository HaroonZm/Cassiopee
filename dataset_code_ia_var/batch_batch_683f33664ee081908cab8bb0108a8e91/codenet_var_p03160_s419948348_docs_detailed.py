def distribute_dp_min_cost():
    """
    Solves the minimum cost problem using the 'distribute DP' approach (配るDP).
    The problem scenario: Given a list of heights, H, and a frog that starts at the first stone,
    you want to find the minimum total cost for the frog to reach the last stone, 
    where the frog can jump forward by one or two steps, and the cost of each jump 
    is the absolute difference between the heights of the current and destination stones.

    Input:
        n (int): The number of stones.
        H (List[int]): List of heights of the stones (1-indexed).

    Output:
        Prints the minimum cost to reach the last stone.
    """
    # Read the number of stones from input
    n = int(input())

    # Read the heights of the stones from input, and prepend a dummy value (0)
    # so that heights are 1-indexed for convenience (H[1] is the height of the first stone)
    H = [0] + list(map(int, input().split()))

    # Initialize the dp array:
    # dp[i] will store the minimum cost to reach the i-th stone
    # All values are initialized to a large number (10^10) except for the start position
    dp = [10**10] * (n + 1)

    # The cost to reach the first stone is 0 (starting position)
    dp[1] = 0

    # Loop through each stone (1-indexed) to propagate the dp values forward
    for i in range(1, n):
        # If jumping two stones ahead is within bounds, update dp[i+2]
        if i + 2 <= n:
            # The cost to jump from stone i to i+2
            jump_two_cost = dp[i] + abs(H[i] - H[i + 2])
            # Update dp[i+2] if we found a smaller cost
            dp[i + 2] = min(jump_two_cost, dp[i + 2])

        # Update the cost for jumping to the next stone (i+1)
        jump_one_cost = dp[i] + abs(H[i] - H[i + 1])
        dp[i + 1] = min(jump_one_cost, dp[i + 1])

    # After filling dp, dp[n] contains the minimum cost to reach the last stone
    print(dp[n])

# Call the function to execute the DP resolution
distribute_dp_min_cost()