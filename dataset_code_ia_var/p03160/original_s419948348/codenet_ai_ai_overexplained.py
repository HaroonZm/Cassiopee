# 配るDP （Dynamic Programming with distributing method）
# H (list of heights), 1-indexed for easier logic (so H[0] is dummy)
# Per comment, explain EVERY concept, even the most basic

# Read integer n from standard input (number of stones)
n = int(input())

# Read next line, split by spaces, convert each to integer
# ... then make a list from those integers (heights)
# Since we use 1-based indexing for heights, we add a 0 at start of list
H = [0] + list(map(int, input().split()))

# Create dp list of length n+1 (to allow use of 1-indexed access)
# Each element initially set to a very large value (10**10)
# This represents that, at start, the minimal cost to reach each stone is infinity
dp = [10**10] * (n + 1)

# It costs 0 to start at stone 1 (the first stone)
dp[1] = 0

# For every stone index from 1 to n-1 (since we cannot jump past the final stone)
for i in range(1, n):
    # First, consider jump of TWO steps (from i to i+2)
    # Only process if i+2 does not exceed n (it's within bounds)
    if i + 2 <= n:
        # Calculate the cost of jumping from i to i+2
        # The cost is the current cost to reach i (dp[i])
        # plus the absolute height difference between stone i and stone i+2
        # We compare this with the existing minimal cost to reach i+2 (dp[i+2])
        # and keep the smaller one (using min function)
        dp[i + 2] = min(dp[i] + abs(H[i] - H[i + 2]), dp[i + 2])
    # Then, always consider jump of ONE step (from i to i+1)
    # This is always valid because i+1 <= n when i < n
    # Similar calculation: cost to reach i+1 could be from i
    dp[i + 1] = min(dp[i] + abs(H[i] - H[i + 1]), dp[i + 1])

# After processing, dp[n] contains the minimal cost to reach the last stone (stone n)
print(dp[n])