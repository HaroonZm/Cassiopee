import sys
import numpy as np

# Assign stdin buffer read functions for efficient input processing.
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# Read the first line and parse the integers H, W, K.
H, W, K = map(int, readline().split())

# Read the rest of the input and parse it into a numpy array:
# - The frombuffer function reads as an array of characters ('S1').
# - Reshape to (H, -1), automatically inferring size; we then select up to W columns.
# - Comparison with b'#' gives a boolean mask where each True means a black cell.
S = np.frombuffer(read(), 'S1').reshape(H, -1)[:, :W] == b'#'

# The modulo for all result computations.
MOD = 10 ** 9 + 7

# Early exit cases for small K:
if K in [0, 1]:
    print(1)
    exit()

# Count the total number of black ('#') cells in the grid.
B = int(S.sum())

# Handle the special case when the grid is one-dimensional.
if H == 1 or W == 1:
    if B == H * W:
        # Entire row or column is black; only one way.
        answer = 1
    else:
        # Otherwise, ways are B^(K-1) modulo MOD.
        answer = pow(int(B), K-1, MOD)
    print(answer)
    exit()

# For general (2D) cases, we check for wrap-around connectivity.

# Check if the leftmost and rightmost columns are both black for each row.
concat_h = S[:, 0] & S[:, -1]
# Check if the top and bottom rows are both black for each column.
concat_w = S[0] & S[-1]

# Whether there is any wrap-around in rows or columns (any 'True' in the concatenations).
bl_h = np.any(concat_h)
bl_w = np.any(concat_w)

if bl_h and bl_w:
    # If both connections exist, grid is a black cycle; answer is always 1.
    print(1)
    exit()
if not bl_h and not bl_w:
    # If no wrap-around, answer is B^(K-1) modulo MOD.
    answer = pow(B, K-1, MOD)
    print(answer)
    exit()
if bl_w:
    # If wrap-around exists only in columns, transpose for unified handling.
    H, W = W, H
    S = S.T
    concat_h, concat_w = concat_w, concat_h

def power_mat(A: np.ndarray, n: int, MOD: int) -> np.ndarray:
    """
    Efficiently computes the matrix A raised to the power n, modulo MOD, using binary exponentiation.
    
    Parameters:
        A (np.ndarray): Square numpy matrix (shape k x k).
        n (int): Non-negative integer exponent.
        MOD (int): Modulo value.
        
    Returns:
        np.ndarray: The result of (A ** n) % MOD.
    """
    k = A.shape[0]
    if n == 0:
        # The 0-th power of a matrix is the identity matrix.
        return np.eye(k, dtype=np.int64)
    B = power_mat(A, n // 2, MOD)
    B = np.dot(B, B) % MOD
    if n % 2:
        # If odd power, multiply once by A.
        return np.dot(A, B) % MOD
    else:
        return B

# Count the number of horizontal edges (adjacent pairs of black cells in each row).
h_edge = (S[:, :-1] & S[:, 1:]).sum()

# Construct the transition matrix for the recurrence relation.
# See problem-related explanations for further background.
A = np.array([
    [B, -h_edge], 
    [0, np.count_nonzero(concat_h)]
], dtype=np.int64)

# Using linear algebra, compute the sequence with the transition matrix.
answer = power_mat(A, K-1, MOD)[0].sum() % MOD

print(answer)