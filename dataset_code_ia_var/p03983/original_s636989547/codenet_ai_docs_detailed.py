import sys
import numpy as np

# Assign input reading shortcuts for efficient stdin usage
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# Define the modulo constant for all calculations to avoid overflow
MOD = 10**9 + 7

def precompute(M):
    """
    Precompute arrays used for efficiently solving queries up to a maximum value M.

    Args:
        M (int): The upper limit for which to precompute dp1 and dp2 arrays.

    Returns:
        tuple of np.ndarray: Returns a tuple (dp1, dp2)
            - dp1: Number of ways for M seconds
            - dp2: Sum of production start times for M seconds
    """
    # Initial group size is set a bit above M to start searching for max 'g'
    g = M + 10

    # dp1: For each time m, holds the number of people/ways
    dp1 = np.ones(M, np.int64)
    # dp2: For each time m, holds the sum of production start timestamps
    dp2 = np.zeros(M, np.int64)

    # Find the largest g so that group size timing stays within bounds
    while g * (g - 1) // 2 > M:
        g -= 1

    # Decrementally process each possible group size
    while g >= 1:
        # Prepare new dp arrays for the updated group count
        newdp1 = np.ones_like(dp1)
        newdp2 = np.zeros_like(dp2)
        # For each time m that can fit the current group size 'g'
        for m in range(2 * g, M):
            # Update ways count:
            # - the original
            # - plus ways with 'g' subtracted (representing splitting)
            newdp1[m] = (newdp1[m - g] + dp1[m - g]) % MOD
            # Update start time sum:
            # - the original
            # - plus start times for the scenario with 'g' subtracted
            # - plus group size 'g' times the count for this subproblem
            newdp2[m] = (newdp2[m - g] + dp2[m - g] + g * newdp1[m]) % MOD
        # Decrease group size for next iteration
        g -= 1
        # Swap in the new dp arrays
        dp1, dp2 = newdp1, newdp2
    return dp1, dp2

def main(NC):
    """
    Solve queries using precomputed dp arrays.

    Args:
        NC (np.ndarray): Interleaved array of length 2*k where:
            - Even indices (NC[0], NC[2], ...) are values of n (seconds/amount)
            - Odd indices (NC[1], NC[3], ...) are values of c (split/count)
    """
    # Precompute dp1, dp2 arrays up to a set large value
    dp1, dp2 = precompute(100_010)

    # Split input array into separate n and c arrays
    N = NC[::2]
    C = NC[1::2]

    # Process all query pairs
    for i in range(len(N)):
        n, c = N[i], C[i]
        # Divide 'n' into 'c'-sized blocks
        q, r = divmod(n, c)
        # Use dp arrays for efficient calculation
        ans = dp1[q] * n - dp2[q] * c
        # Output the result modulo MOD
        print(ans % MOD)

# If running in an online judge environment, use numba for JIT and register exports
if sys.argv[-1] == 'ONLINE_JUDGE':
    import numba
    from numba.pycc import CC
    i8 = numba.int64
    cc = CC('my_module')

    def cc_export(f, signature):
        """
        Decorator to compile and export functions using numba for the online judge.
        """
        cc.export(f.__name__, signature)(f)
        return numba.njit(f)

    precompute = cc_export(precompute, (i8, ))
    main = cc_export(main, (i8[:], ))
    cc.compile()

# Import compiled main if available
from my_module import main

# Read all stdin input, split into integers (ignoring first, usually a count), and process
NC = np.array(read().split(), np.int64)[1:]

# Run the (possibly numba-compiled) main function
main(NC)