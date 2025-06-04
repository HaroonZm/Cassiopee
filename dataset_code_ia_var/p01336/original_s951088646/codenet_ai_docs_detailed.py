def main():
    """
    Main function to continuously read test cases from input, process each, and print the maximal value found
    among three categories, subject to capacity constraints. Input reading stops when an error occurs (e.g., EOF).
    """
    while True:
        try:
            # Read the number of items N and the maximal capacity M for the test case
            N, M = map(int, raw_input().split())

            # Initialize the dynamic programming (DP) table with three rows (categories),
            # each with M+1 columns (capacities from 0 to M), all entries set to 0 at start
            dp = [[0] * (M + 1) for _ in range(3)]

            # Loop over each item
            for _ in range(N):
                # Read the item's name (ignored for computation)
                name = raw_input()

                # Read item's cost, and three values associated (V, D, L)
                C, V, D, L = map(int, raw_input().split())

                # Store the three values in a list for easier iteration
                VDL = [V, D, L]

                # If the cost exceeds the capacity, this item can't be chosen
                if C > M:
                    continue

                # Iterate over the three value categories (V, D, L)
                for i in range(3):
                    # For current cost C, try to update DP if this item's value is better
                    dp[i][C] = max(dp[i][C], VDL[i])

                    # Check all existing capacities j (from 0 up to M-1)
                    for j in range(M):
                        # If there is a solution for this capacity j (dp[i][j] > 0)
                        if dp[i][j]:
                            # If adding this item does not exceed max capacity
                            if j + C <= M:
                                # Update the DP table entry for capacity j+C in the i-th category
                                dp[i][j + C] = max(dp[i][j + C], dp[i][j] + VDL[i])

            # After processing all items, find the best value across all categories and capacities
            print max(max(dp[0]), max(dp[1]), max(dp[2]))

        except:
            # Break the loop if any exception occurs (likely input exhausted)
            break

if __name__ == "__main__":
    main()