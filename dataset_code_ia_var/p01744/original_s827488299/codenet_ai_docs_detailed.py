from collections import defaultdict
import sys

def solve():
    """
    Reads input parameters for the problem, processes the defined operations, and prints the final result.

    The function reads three integers H, W, N representing height, width, and the number of swaps,
    then reads N pairs of integers for swap positions. It computes the result of a grid shuffling
    process with permutations described in the problem and prints the final mapping as required.

    Input:
        stdin: expects (H, W, N) followed by N lines of two integers each.

    Output:
        Prints W lines, each corresponding to the final position.
    """
    # Alias for faster input/output operations
    readline = sys.stdin.readline
    write = sys.stdout.write

    # Read input values: H (height), W (width), N (number of operations)
    H, W, N = map(int, readline().split())

    # Initialize helper arrays for permutation computation
    # A[]: Used for mapping positions for swaps
    # B[], C[]: Helper mappings for determining permutation indices
    A = [0] * W
    B = [0] * W
    C = [0] * W

    # Fill A, B, and C arrays depending on the current index in the first half of W
    # These define the reordering patterns applied later
    for i in range(W // 2):
        # Set position for pattern A[]
        A[i] = i * 2 + 1        # Odd indices from start
        A[-i - 1] = i * 2       # Even indices from end

        # Set values for B[] and C[] to help with swap computations
        B[i * 2] = C[i * 2 - 1] = i
        B[-1 - i * 2] = C[-1 - i * 2 + 1] = i + W // 2

    # X: Holds the current permutation state, i.e., an identity permutation
    X = list(range(W))

    # Read each pair (a, b) representing swap operations and store in list P
    P = [list(map(int, readline().split())) for _ in range(N)]
    P.sort()  # Ensure operations are processed in ascending order

    # For each operation (a, b), compute swap indices using A, B, C permutations,
    # then swap corresponding positions in X (the working permutation)
    for a, b in P:
        if a % 2 == 1:
            # Odd a: compute pattern for swapping using B[]
            k = a // 2
            m = (b // 2) * 2
            p = A[(B[m] + k) % W]
            q = A[(B[m + 1] + k) % W]
        else:
            # Even a: compute pattern for swapping using C[]
            k = a // 2 - 1
            m = ((b - 1) // 2) * 2
            p = A[(C[m + 1] + k) % W]
            q = A[(C[m + 2] + k) % W]
        # Swap elements at positions p and q
        X[p], X[q] = X[q], X[p]

    # Compute the result of a shuffle pattern over H rows, using the process described.
    # E0 is the base shuffle permutation (row shuffling step 1)
    E0 = list(range(W))
    for i in range(W // 2):
        E0[2 * i], E0[2 * i + 1] = E0[2 * i + 1], E0[2 * i]
    # E1 is the result of an additional shuffle (row shuffling step 2)
    E1 = E0[:]
    for i in range(W // 2 - 1):
        E1[2 * i + 1], E1[2 * i + 2] = E1[2 * i + 2], E1[2 * i + 1]

    # Use exponentiation by squaring to apply shuffle H // 2 times efficiently
    k = H // 2
    Y = list(range(W))  # Y holds the shuffle permutation state
    while k:
        if k & 1:
            # If current power bit is set, apply E1 shuffle
            Y = [Y[e] for e in E1]
        # Compose E1 with itself
        E1 = [E1[e] for e in E1]
        k >>= 1

    # If H is odd, perform final E0 shuffle
    if H % 2:
        Y = [Y[e] for e in E0]

    # Compose the final answer: ans[i] is the (1-based) index after all permutations
    ans = [0] * W
    for i, e in enumerate(Y):
        ans[X[e]] = i + 1

    # Output result, one per line
    for e in ans:
        write("%d\n" % e)

solve()