def main():
    """
    Main function to process multiple test cases for the knapsack-like problem.
    Reads input, processes each item, updates dynamic programming tables, 
    and prints the best result among the objectives.
    The loop continues to process data until EOF or a parsing error occurs.
    """
    while True:
        try:
            # Read N (number of items), M (capacity) for the current test case
            N, M = map(int, raw_input().split())
            
            # Initialize DP tables:
            # dp[i][j] = best achievable value for objective i using total cost j
            # There are 3 objectives (V, D, L), for costs from 0 to M
            dp = [[0] * (M + 1) for _ in range(3)]
            
            for _ in range(N):
                # Read item name (unused, but required by input)
                name = raw_input()
                # Read item properties: Cost, Value, Durability, Lifespan
                C, V, D, L = map(int, raw_input().split())
                VDL = [V, D, L]  # Objective values for the item
                
                for i in range(3):  # Loop over each objective (V, D, L)
                    try:
                        # Try to update dp[i][C] by picking only this item
                        dp[i][C] = max(dp[i][C], VDL[i])
                    except IndexError:
                        # If C > M, ignore as it can't fit in the knapsack
                        break
                    for j in range(M + 1):  # Try all current achievable costs j
                        if dp[i][j]:
                            # If there's a way to reach cost j, try adding this item
                            try:
                                if j + C <= M:
                                    dp[i][j + C] = max(dp[i][j + C], dp[i][j] + VDL[i])
                            except IndexError:
                                # If j + C > M, we can't store this state
                                break
            # Compute and print the best achievable value across all objectives and costs
            max_value = max(max(dp[0]), max(dp[1]), max(dp[2]))
            print max_value
        except:
            # On input error/EOF, exit the loop and stop processing
            break

# Entry point for the program
if __name__ == "__main__":
    main()