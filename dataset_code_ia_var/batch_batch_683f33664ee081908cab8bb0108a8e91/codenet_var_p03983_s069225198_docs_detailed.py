import sys
import numpy as np
import numba
from numba import njit

# Use int64 throughout for consistency with numba
i8 = numba.int64

# Standard input buffer short-hands
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# Modulo constant for calculations
MOD = 10 ** 9 + 7

@njit((i8,), cache=True)
def precompute(M):
    """
    Precomputes two dynamic programming arrays up to M:
      - dp1[m]: The count of possible arrangements for each m.
      - dp2[m]: The sum of production start times for each m.
    This uses a backwards induction approach with a variable step size 'g'
    to efficiently populate both arrays for subsequent queries.

    Parameters
    ----------
    M : int
        The maximum value up to which computations are carried out.

    Returns
    -------
    dp1 : numpy.ndarray
        An array where dp1[m] is the number of ways for state m.
    dp2 : numpy.ndarray
        An array where dp2[m] is the sum of production start times for state m.
    """

    # g is the upper-bound step for grouping
    g = M + 10
    # dp1: Number of arrangements for each m
    dp1 = np.ones(M, np.int64)
    # dp2: Sum of production start times for each m, initialised to zero
    dp2 = np.zeros(M, np.int64)
    # Adjust g downwards so that g*(g-1)//2 <= M
    while g * (g - 1) // 2 > M:
        g -= 1
    # Iterate and update DP tables for different g
    while g >= 1:
        # Use new buffers to store calculated values for the current g
        newdp1 = np.ones_like(dp1)
        newdp2 = np.zeros_like(dp2)
        # For each time m from 2*g up to M-1
        for m in range(2 * g, M):
            # Update count for dp1 at m
            newdp1[m] = (newdp1[m - g] + dp1[m - g]) % MOD
            # Update sum for dp2 at m
            newdp2[m] = (newdp2[m - g] + dp2[m - g] + g * newdp1[m]) % MOD
        # Proceed to next smaller g
        g -= 1
        # Swap new buffers into dp1, dp2 for next iteration
        dp1, dp2 = newdp1, newdp2
    return dp1, dp2

@njit((i8[:],), cache=True)
def main(NC):
    """
    For an array of paired values (N, C) where each N denotes the number of objects
    and C a constant per query, computes for each pair an answer using the two DP arrays
    from precompute. The result involves combinations and modular arithmetic.

    Parameters
    ----------
    NC : numpy.ndarray
        1D array containing alternating N, C values for each query: [N0, C0, N1, C1, ...].
    """
    # Precompute DP arrays up to a large enough limit (problem-specific)
    dp1, dp2 = precompute(100_010)
    
    # Extract N and C arrays from input
    N = NC[::2]
    C = NC[1::2]

    for i in range(len(N)):
        n, c = N[i], C[i]
        q, r = divmod(n, c)
        # Compute answer using dp1 and dp2 at index q and modulo arithmetic
        ans = dp1[q] * n - dp2[q] * c
        print(ans % MOD)

# Read and convert input: the first element is the number of test cases and is skipped
NC = np.array(read().split(), np.int64)[1:]

# Run the main processing function with the input
main(NC)