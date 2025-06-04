def main():
    # Import the 'sys' module to access system-specific parameters and functions.
    import sys
    # Import 'sqrt' function from the 'math' module to compute square roots.
    from math import sqrt
    # Override built-in input() with sys.stdin.readline for efficient input reading.
    input = sys.stdin.readline

    # Define a constant 'mod' for modulo operations to avoid integer overflow.
    mod = 1000000007

    # Read a line from standard input using input(), split it into tokens, convert to int, and unpack into N and K.
    N, K = map(int, input().split())

    # Calculate the floor value of the square root of N. This will be used to partition our data for efficiency.
    n = int(sqrt(N))

    # Initialize a 2D list (K+1 rows, 2*n+1 columns) used for dynamic programming (DP).
    # Each element in this table will be an integer initially set to 0.
    # dp[i][j] will represent the number of certain objects (depending on the problem) for stage i and parameter j.
    dp = [[0] * (2*n+1) for _ in range(K+1)]

    # Set the base case of the DP: stage 0 and index 1 is initialized to 1.
    # In most DP problems, the base case represents one way to assemble or choose from nothing.
    dp[0][1] = 1

    # Initialize a list 'num' of size (n+1), to store counts of how many numbers in [1, N] have the same floor division result.
    num = [0] * (n+1)

    # Loop from 1 to n-1 (inclusive: range(1, n)), and compute the number of integers x in [1, N] such that N // x = i.
    # This works because floor division decreases as x increases.
    for i in range(1, n):
        num[i] = N // i - N // (i+1)

    # For i == n, the previous formula would involve division by n+1, which might miss some values,
    # so we handle it specially.
    num[n] = N // n - n

    # Begin DP transitions; repeat K times, for each stage of the process.
    for i in range(K):
        # For efficiency, alias/slice two parts of the DP row: cs and cs2.
        # cs will point to the first n+1 elements of the current row (dp[i][0], ..., dp[i][n]).
        cs = dp[i][:n+1]
        # cs2 will point to the remaining elements, starting from dp[i][n+1] to the end.
        cs2 = dp[i][n+1:]

        # Compute prefix sums for 'cs'. For each index from 1 to n, accumulate the values, modulo mod.
        # Prefix sums help in efficiently computing range sums in DP transitions.
        for j in range(1, n+1):
            cs[j] = (cs[j] + cs[j-1]) % mod

        # Similarly, compute prefix sums over 'cs2' for indices 1 to n-1.
        for j in range(1, n):
            cs2[j] = (cs2[j] + cs2[j-1]) % mod

        # Now, update the next DP stage (dp[i+1]) based on the current prefix sums.
        for j in range(1, n+1):
            # Update negative indices from the end: -j means the j-th from the end of list.
            # This state is computed by multiplying the prefix sum up to index j by num[j], all modulo mod.
            dp[i+1][-j] = (cs[j] * num[j]) % mod
            # Update positive indices, possibly referring to "large class" states.
            # The value is the prefix sum from cs2 at position -j plus the total sum up to cs[n], all modulo mod.
            dp[i+1][j] = (cs2[-j] + cs[n]) % mod

    # After all DP stages, sum up all values in the last row of DP table to get the answer.
    ans = 0
    for a in dp[-1]:
        ans = (ans + a) % mod

    # Print the final answer. In contests, output must be precise, so we use print().
    print(ans)

# Standard "main" guard in Python to ensure that main() only runs when this script is executed directly,
# and not when imported as a module in another program.
if __name__ == '__main__':
    main()