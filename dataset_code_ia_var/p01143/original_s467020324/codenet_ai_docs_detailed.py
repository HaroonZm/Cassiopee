def main():
    """
    Main function that reads input, processes each test case according to the problem's rules,
    and writes the output to standard output.
    """
    import sys

    # Read a single line from standard input efficiently.
    readline = sys.stdin.readline
    # List to accumulate output strings for all test cases.
    ans = []

    while True:
        # Read the first line for the test case, splitting it into three integers: N (number of participants), M (index of winner), and P (percent fee)
        line = readline()
        N, M, P = map(int, line.split())
        # If N is zero, no more test cases remain -- exit the loop.
        if N == 0:
            break

        # Read the contributions of each participant, one per line, storing them as integers in list X.
        X = [int(readline()) for _ in range(N)]

        # Calculate the total sum of all contributions.
        total_contributions = sum(X)
        # Get the contribution of the winner (convert M from 1-based to 0-based index).
        winner_contribution = X[M - 1]

        # If the winner's contribution is zero, the output for this test case is '0'
        if winner_contribution == 0:
            ans.append("0\n")
            continue

        # Compute the total prize excluding the percent fee, then determine the winner's share.
        # The prize is total_contributions * (100 - P) // 100 divided proportionally among the winner's tickets.
        # To avoid floating-point issues, perform the calculation using integer arithmetic.
        winner_share = int(total_contributions * (100 - P) / winner_contribution)
        ans.append(f"{winner_share}\n")

    # Write all the accumulated answer lines to standard output at once.
    sys.stdout.writelines(ans)

if __name__ == "__main__":
    main()