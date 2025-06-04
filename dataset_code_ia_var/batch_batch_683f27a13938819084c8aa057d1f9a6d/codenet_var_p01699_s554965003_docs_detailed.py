import sys

# Set up shortcuts to standard input and output functions for efficiency
readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    """
    Solve the problem for a single test case.

    Reads input data specifying N ranges [A_i, B_i], performs dynamic programming to count
    the number of digit sequences satisfying certain constraints defined by the ranges, and
    outputs the result.

    Returns:
        bool: False if N == 0 (terminates input loop), True otherwise (continues).
    """
    # Read the number of intervals (N)
    N = int(readline())
    if N == 0:
        # Terminate processing if 0 is read
        return False

    # Initialize arrays for the lower and upper bounds of the intervals
    A = [0] * N
    B = [0] * N
    for i in range(N):
        # Read and split the interval endpoints for each i
        A[i], B[i] = map(int, readline().split())

    # Set the total possible state size (bitmask for each interval)
    N0 = 1 << (3 * N)
    # DP table: dp[position][state]
    #   - position: number of digits placed
    #   - state: bitmask encoding interval satisfaction
    dp = [[0] * N0 for _ in range(2 * N + 1)]

    # Initialize DP for first digit (position=1)
    for i in range(1, 10):
        c = 0  # State bitmask for the first interval
        # Check if the one-digit number i fits into various conditions for the first interval
        if A[0] <= i <= B[0]:
            c |= 1
        if A[0] // 10 <= i < B[0] // 10 or A[0] // 10 == B[0] // 10 == i:
            c |= 2
        if A[0] // 10 < i <= B[0] // 10:
            c |= 4
        dp[1][c] += 1  # Update DP table

    # Process subsequent positions (digits to be placed)
    for pos in range(1, N * 2):
        dp0 = dp[pos]        # Current layer of DP
        dp1 = dp[pos + 1]    # Next layer of DP
        for state in range(1, N0):   # Iterate through all possible states
            v = dp0[state]
            if v == 0:
                # Skip states that have no valid paths
                continue
            # Try placing digits 0-9 in the next position
            for digit in range(10):
                c = 0  # New state bitmask to build for next position
                for l in range(N):
                    a0 = A[l]
                    b0 = B[l]
                    s = 1 << (3 * l)  # Bit position for interval l

                    # Process next interval, if state bit and other conditions allow
                    if state & s and l < N - 1 and digit > 0:
                        a1 = A[l + 1]
                        b1 = B[l + 1]
                        if a1 <= digit <= b1:
                            c |= (s << 3)
                        if (a1 // 10 <= digit < b1 // 10) or (a1 // 10 == b1 // 10 == digit):
                            c |= (s << 4)
                        if a1 // 10 < digit <= b1 // 10:
                            c |= (s << 5)

                    # Check state of current interval, adjust accordingly
                    if state & (s << 1):
                        if state & (s << 2):
                            c |= s
                        elif a0 // 10 == b0 // 10:
                            if a0 % 10 <= digit <= b0 % 10:
                                c |= s
                        elif a0 % 10 <= digit:
                            c |= s
                    if state & (s << 2):
                        if digit <= b0 % 10:
                            c |= s
                if c:
                    # Add the number of ways to reach current state to the new state
                    dp1[c] += v

    # Sum the answer: only count DP states where highest interval bit (for last interval) is set
    ans = 0
    for pos in range(2 * N + 1):
        dpi = dp[pos]
        ans += sum(dpi[j] for j in range(N0) if j & (1 << (3 * N - 3)))

    # Output the answer to stdout
    write("%d\n" % ans)
    return True

# Keep processing test cases until N == 0
while solve():
    ...