import sys
import numpy as np
from heapq import heappop, heappush

# For fast I/O operations
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def choose_increasing(q):
    """
    Returns a strictly increasing subsequence of the input sequence q.

    Iterates through the given sequence and maintains a mono-increasing list
    by removing the tail elements that are not less than the current element.
    
    Args:
        q (iterable of int): The input sequence of integers.
    
    Returns:
        numpy.ndarray: The strictly increasing subsequence as a numpy int64 array.
    """
    A = []  # List to store the increasing subsequence
    for x in q:
        # Remove elements from the end that are greater than or equal to x
        while A and A[-1] >= x:
            A.pop()
        A.append(x)
    return np.array(A, np.int64)

def main(A, N):
    """
    Computes an array based on a particular greedy heap-based splitting process.

    Simulates a process where numbers are recursively split, and their
    contributions are tracked using a heap for optimal calculation.
    
    Args:
        A (numpy.ndarray): A strictly increasing numpy array of int64.
        N (int): The size of the final array to generate.
    
    Returns:
        numpy.ndarray: The result array of length N, with values as per computed contributions.
    """
    # Initialize a max-heap (using negated values since Python's heapq is a min-heap)
    heap = [(-A[-1], 1)]  # Each entry is a tuple: (negated value, coefficient)
    # Process the array in reverse (from largest to smallest)
    for n in A[::-1]:
        while True:
            # Break if the largest value in the heap is less than or equal to n
            if -heap[0][0] <= n:
                break
            x, coef = heappop(heap)
            # Combine coefficients for equal values in the heap
            while heap and heap[0][0] == x:
                _, c = heappop(heap)
                coef += c
            # Divide -x by n, obtaining quotient and remainder
            q, r = divmod(-x, n)
            # The quotient contributes coef*q times for value n
            heappush(heap, (-n, coef * q))
            # The remainder contributes coef times for value r
            heappush(heap, (-r, coef))
    # Prepare the output array with sufficient size (N+10 for safety margin)
    ret = np.zeros(N + 10, np.int64)
    # Apply the contributions in a difference array scheme
    for x, c in heap:
        x = -x  # Get the actual value
        ret[1] += c
        ret[x + 1] -= c
    # Compute the prefix sum to get the final values
    ret = np.cumsum(ret)
    return ret[1:N + 1]

if sys.argv[-1] == 'ONLINE_JUDGE':
    # If running under an online judge, use numba for JIT compilation and C export
    import numba
    from numba.pycc import CC
    i8 = numba.int64
    cc = CC('my_module')
    
    def cc_export(f, signature):
        """
        Helper to export and jit-compile functions with numba and pycc.
        """
        cc.export(f.__name__, signature)(f)
        return numba.njit(f)
    
    main = cc_export(main, (i8[:], i8))
    cc.compile()

# Import the possibly JIT-compiled main function.
from my_module import main

# Read values from standard input.
N, Q = map(int, readline().split())
# Read Q values and prepend N as the first element
q = [N] + list(map(int, read().split()))

# Get a strictly increasing subsequence from q
A = choose_increasing(q)
# Call main function to compute the answer array
ans = main(A, N)
# Print each value of the result on a new line
print('\n'.join(map(str, ans.tolist())))