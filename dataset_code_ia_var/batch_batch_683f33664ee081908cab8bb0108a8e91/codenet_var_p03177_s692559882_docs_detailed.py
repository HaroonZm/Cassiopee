def power(x, n, mod):
    """
    Exponentiates a square matrix x to the power n modulo mod using binary exponentiation.

    Args:
        x (list of list of int): The base matrix to be exponentiated (must be square).
        n (int): The exponent.
        mod (int): The modulo to compute all operations with.

    Returns:
        list of list of int: The matrix x raised to the power n, under modulo mod.
    """
    # Determine the number of bits in n (used for exponentiation)
    digit = len(str(bin(n))) - 2  # Remove '0b' prefix from binary string
    a = len(x)  # The size of the square matrix

    # Precompute dp[i] = x^(2^i) for fast exponentiation
    dp = [x] * digit  # Initialize all slots with reference to x
    # Compute powers of x by repeated squaring
    for i in range(1, digit):
        dp[i] = dot(dp[i - 1], dp[i - 1], mod)

    # Initialize the answer as the identity matrix
    ans = [[0] * a for _ in range(a)]
    for i in range(a):
        ans[i][i] = 1

    # Multiply in the required dp[i] where the corresponding bit of n is set
    for i in range(digit):
        if (1 << i) & n:
            ans = dot(dp[i], ans, mod)

    return ans

def dot(A, B, mod):
    """
    Multiplies two matrices A and B modulo mod.

    Args:
        A (list of list of int): The first matrix of size (p x q).
        B (list of list of int): The second matrix of size (q x s).
        mod (int): The modulo to compute all operations with.

    Returns:
        list of list of int: The product matrix of size (p x s) modulo mod.
        Returns None if the matrices cannot be multiplied due to size mismatch.
    """
    p = len(A)    # Number of rows in A
    q = len(A[0]) # Number of columns in A (must equal number of rows in B)
    r = len(B)    # Number of rows in B
    s = len(B[0]) # Number of columns in B

    # Size mismatch check for matrix multiplication
    if q != r:
        print('掛け算できません')  # Means "Cannot multiply" in Japanese
        return

    # Initialize result matrix with zeros
    ans = [[0] * s for _ in range(p)]

    # Standard matrix multiplication
    for i in range(p):
        for j in range(s):
            for k in range(q):
                ans[i][j] += A[i][k] * B[k][j]
                ans[i][j] %= mod  # Apply modulo at each step to avoid overflow

    return ans

def solve():
    """
    Reads input data, computes the K-th power of the adjacency matrix of a graph,
    and returns the total number of paths of length K modulo 10^9+7.

    Input:
        First line: Two integers N (matrix size) and K (power to raise to).
        Next N lines: NxN integers representing the adjacency matrix.

    Output:
        Prints the sum of all entries in the matrix (i.e., total number of paths of length K).
    
    Returns:
        int: The sum mod 10^9+7 of all entries in the resulting matrix.
    """
    # Read the size of the matrix and the power
    N, K = map(int, input().split())

    # Read the N x N adjacency matrix
    mat = [list(map(int, input().split())) for _ in range(N)]

    # Create the identity matrix of size N x N
    init = [[0] * N for _ in range(N)]
    for i in range(N):
        init[i][i] = 1

    mod = 10 ** 9 + 7  # Modulo value

    # Compute mat^K using matrix exponentiation and multiply by identity matrix
    dp = dot(init, power(mat, K, mod), mod)

    # Sum all entries to get the total number of paths
    ans = sum(map(sum, dp)) % mod

    return ans

print(solve())