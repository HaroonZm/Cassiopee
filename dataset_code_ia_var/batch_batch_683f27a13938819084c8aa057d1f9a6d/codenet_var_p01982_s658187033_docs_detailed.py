def process_ranges():
    """
    Reads multiple cases from the standard input and processes each according to the following:
    - For each case, reads three integers n, l, r.
    - If all three are zero, terminates the loop.
    - Otherwise, reads n divisors into a list A.
    - For every integer x in the range [l, r]:
        - Checks if x is divisible by any element in A.
            - If so, and the index of the divisor in A is even, increments the answer by 1 and moves to the next x.
        - If x is not divisible by any element in A, and n is even, increments the answer by 1.
    - Prints the answer for each test case.

    No arguments, input is read from standard input, output is printed to standard output.
    """
    while True:
        # Read a line and split into three integers n, l, r
        n, l, r = map(int, input().split())
        
        # Termination condition: if all three values are zero
        if n == l == r == 0:
            break

        # Read n lines, each containing an integer to form the divisor list A
        A = [int(input()) for _ in range(n)]

        # Initialize the answer counter to zero
        ans = 0

        # Iterate over the range [l, r] inclusive
        for x in range(l, r + 1):
            # For every number in A, test if x is divisible by A[i]
            for i in range(n):
                if x % A[i] == 0:
                    # If found and the index i is even, increment ans
                    if i % 2 == 0:
                        ans += 1
                    # Stop checking further divisors for this x
                    break
                elif i == (n - 1):
                    # If we reach the last divisor and x was not divisible by any,
                    # and n is even, increment ans
                    if n % 2 == 0:
                        ans += 1

        # Output the total answer for the current case
        print(ans)

# Run the main processing function
process_ranges()