import sys

def main():
    """
    Reads problem submissions, counts the number of accepted problems and the total number of failed attempts
    for those accepted problems before their first 'AC' verdict.

    Input:
        First line: two integers N (number of problems), M (number of submissions)
        Next M lines: each line contains 'p s' where p is problem number (1-indexed), s is verdict ('AC' or 'WA')

    Output:
        Prints two integers: total number of accepted problems, and total number of failed attempts (for solved problems).
    """
    # Read the numbers of problems (N) and submissions (M)
    N, M = map(int, input().split())

    # Arrays to keep track of AC status and number of WA attempts for each problem
    ac = [0 for _ in range(N)]  # ac[i] = 1 if problem i has been solved, 0 otherwise
    wa = [0 for _ in range(N)]  # wa[i] = number of wrong attempts before first correct submission for problem i

    # Process each submission
    for _ in range(M):
        p, s = input().split()
        p = int(p) - 1  # Convert problem number to 0-based index
        
        if s == 'AC':
            # If the problem wasn't accepted before, mark as accepted
            ac[p] = 1
        else:
            # Only count wrong attempts before the problem is accepted
            if ac[p] == 0:
                wa[p] += 1

    # After all submissions, set the wrong attempt counter to zero for unsolved problems
    for i in range(N):
        if ac[i] == 0:
            wa[i] = 0

    # Output total number of solved problems and total number of wrong attempts for solved problems
    print(str(sum(ac)) + " " + str(sum(wa)))


if __name__ == '__main__':
    main()