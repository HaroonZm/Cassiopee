def solve(low, n, ls):
    # Create a list 'dp' with (n+1) elements, each initialized to a very large number (10^20).
    # 'dp' will be used for dynamic programming to store interim optimal results.
    # This large number acts as "infinity" for initial minima comparisons.
    dp = [10 ** 20 for i in range(n + 1)]
    # Set the base case value: To partition 0 elements, the best "high" length is 'low', since that's our starting minimum.
    dp[0] = low

    # Iterate over each possible endpoint 'i' for possible partitions (from the 0th to (n-1)th position).
    for i in range(n):
        # Initialize the 'length' variable for this iteration. It will accumulate segment lengths backwards.
        length = 0

        # For every possible start index 'j' for the current segment, moving backwards from i to 0:
        # (We are thus considering every possible segment ending at position i)
        for j in range(i, -1, -1):
            # Add the value at ls[j] to 'length'. This is the sum of ls[j]...ls[i] (inclusive).
            length += ls[j]

            # Special check: If this is the case where we are considering the full list (first segment from 0 to n-1),
            # skip processing this configuration, as it is not a valid split (there must be more than one partition).
            if i + 1 == n and j == 0:
                continue

            # Only consider segments whose accumulated length is at least 'low'.
            if length >= low:
                # 'high' is the largest value between the current accumulated 'length' and the best result so far at dp[j].
                # Effectively, we are keeping track of the maximum segment length for this particular partition scheme.
                high = max(length, dp[j])

                # We want to minimize the largest segment size; so assign to dp[i+1] the minimum between its current value
                # and 'high' (the max length of the current partition configuration).
                dp[i+1] = min(dp[i+1], high)
    # Finally, the answer is the best largest segment length achievable for n elements, minus the original 'low'.
    return dp[n] - low

def main():
    # Read an integer from input: the number of elements (segments) to be considered.
    n = int(input())

    # Create a list 'ls' of the next n inputs, each converted into an integer.
    # We use a list comprehension to iterate n times and build the list of segment lengths.
    ls = [int(input()) for i in range(n)]

    # Initialize the result variable 'ans' to a very large number, to ensure any real result will be less than this.
    # This will be used to keep track of the minimum possible value throughout iterations.
    ans = 10 ** 20

    # We will try every possible single-segment prefix as the minimum length.
    # For every possible starting position i (from 0 to n-1):
    for i in range(n):
        # Initialize the cumulative length to zero for this starting position.
        length = 0

        # Compute all possible segment lengths that start at i and extend to any j>=i (all suffixes from i).
        for j in range(i, n):
            # Incrementally add the segment length at ls[j] to the running total 'length'.
            length += ls[j]

            # Call the 'solve' function with current 'length' as 'low', to find the optimal segmentation 
            # where no segment can be shorter than 'length'.
            # Update 'ans' to be the minimum of its current value and the result of 'solve'.
            ans = min(ans, solve(length, n, ls))

    # After evaluating all partitions, print the minimum possible answer.
    print(ans)

# Invoke the main function to start the program's execution when run.
main()