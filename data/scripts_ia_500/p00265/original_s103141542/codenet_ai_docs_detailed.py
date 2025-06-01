N, Q = list(map(int, input().split()))
C = list(map(int, input().split()))

# Maximum value in C plus one, used for indexing arrays T and L
M = max(C) + 1

# Initialize array T of length M with zeros
# T[i] will be 1 if value i is present in C, 0 otherwise
T = [0] * M
for v in C:
    T[v] = 1

# Initialize array L with length M to store links to previous valid indices
L = [0] * M
# Variable m keeps track of the last index i where T[i] == 1 encountered in the iteration
m = 0

# Fill array L so that for each i, L[i] contains 
# the largest index less than i for which T[index] == 1
for i in range(M):
    L[i] = m
    if T[i]:
        m = i

def query_max_remainder(q, L, m):
    """
    Calculate the maximum remainder when dividing indices linked in L by q.

    Parameters:
    q (int): The divisor used in modulus operations.
    L (list): List where each element holds the index of the previous valid element.
    m (int): The maximum index from the array T with value 1.

    Returns:
    int: The maximum remainder found among the indices accessed via L.
    """
    maxv = 0  # Store the maximum remainder found
    cur = m   # Start from the maximum valid index
    while cur > 0:
        p = cur % q  # Calculate remainder of current index when divided by q
        maxv = max(maxv, p)  # Update max remainder if current is greater
        if cur - p < 0:
            break  # Stop if subtraction would be negative, no further valid indices
        cur = L[cur - p]  # Move to the previous valid index
    return maxv

# For each query, read the integer q and print the maximum remainder calculated
for _ in range(Q):
    q = int(input())
    print(query_max_remainder(q, L, m))