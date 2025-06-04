def main():
    """
    Main function to compute the number of non-empty subsets in which the average of the subset is equal to a given value A.
    It reads input, processes the data, uses dynamic programming to count valid subsets, and prints the result.
    """
    # Read input values: N (number of elements), A (target average)
    N, A = map(int, input().split())

    # Read the list of integers (alist)
    alist = list(map(int, input().split()))

    # Transform each element by subtracting A to focus on their "deviation" from A
    blist = list(map(lambda x: x - A, alist))

    # Initialize the variables to compute the range of possible sums for blist
    sum_plus = 0   # This will store the total positive sum in blist
    sum_minus = 0  # This will store the total (negative) sum in blist

    for i in blist:
        if i > 0:
            sum_plus += i
        else:
            sum_minus += i  # sum_minus will be negative or zero

    # dp[i][j] : number of ways to select from the first i elements to get the sum (j + sum_minus)
    # The offset sum_minus is used so that even negative sums can be represented as indices >=0

    N = len(alist)
    # Create the DP table:
    # Rows: 0 to N (inclusive), Columns: from sum_minus to sum_plus (inclusive) -> (sum_plus - sum_minus + 1)
    dp = [[0 for _ in range(sum_plus - sum_minus + 1)] for _ in range(N + 1)]

    # Base case initialization: With 0 elements chosen, one subset (the empty subset) has sum 0 (index offset by -sum_minus)
    dp[0][0 - sum_minus] = 1

    # Dynamic Programming to fill the dp table
    for i in range(N):  # For each element in alist/blist
        for j in range(sum_plus - sum_minus + 1):  # For each possible current sum index
            # If including blist[i] does not take us out of bounds:
            if 0 <= j - blist[i] <= (sum_plus - sum_minus):
                # Number of ways to get sum "j" with first i+1 elements is the sum of:
                # - Ways to get sum "j" without using blist[i] (dp[i][j])
                # - Ways to get sum "j-blist[i]" with previous elements and including blist[i] (dp[i][j-blist[i]])
                dp[i + 1][j] = dp[i][j - blist[i]] + dp[i][j]
            else:
                # Cannot include blist[i], so just carry over previous value
                dp[i + 1][j] = dp[i][j]

    # The required answer: number of non-empty subsets whose sum is zero (index offset by -sum_minus)
    # Subtract 1 to remove the count for the empty subset
    print(dp[N][0 - sum_minus] - 1)

if __name__ == "__main__":
    main()