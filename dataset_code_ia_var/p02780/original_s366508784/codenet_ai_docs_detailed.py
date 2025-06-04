def main():
    """
    Main function that reads input, computes the maximum expected value of the sum of K consecutive dice throws,
    and prints the result.
    """
    # Read two integers from the first input line: N is the number of dice, K is the number of consecutive dice to consider
    N, K = map(int, input().split())
    
    # Read the second input line: a list of integers representing the number of faces for each die
    dice = [int(p) for p in input().split()]
    
    # Initialize a prefix sum array S where S[i] holds the sum of expected values for dice 0 through i-1
    # S[0] = 0 by definition
    S = [0 for _ in range(N + 1)]
    
    # Compute expected values and populate the prefix sum array.
    # The expected value for a die with p faces is (p + 1) / 2
    for i in range(1, N + 1):
        S[i] = S[i - 1] + (dice[i - 1] + 1) / 2.0
    
    # Initialize variable to store the maximum expected sum over any sequence of K consecutive dice
    max_E = 0
    
    # Consider all possible sequences of K consecutive dice
    for i in range(N - K + 1):
        # Expected sum for dice in positions [i, i+K-1] is S[i+K] - S[i]
        E = S[i + K] - S[i]
        # Update max_E if this sum is higher than current maximum
        if max_E < E:
            max_E = E
    
    # Output the maximum expected sum found
    print(max_E)


if __name__ == "__main__":
    main()