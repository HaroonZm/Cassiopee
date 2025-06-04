import sys

# sys module provides system-specific parameters and functions.
# We use it here mainly for fast input using stdin and for setting recursion limit.

# Buffer methods for stdin for efficient input.
read = sys.stdin.buffer.read           # Reads all data from standard input as bytes. This is often much faster than input().
readline = sys.stdin.buffer.readline   # Reads one line (up to a newline) from standard input as bytes.
readlines = sys.stdin.buffer.readlines # Reads all lines from standard input as a list of byte strings.

# Increase recursion depth limit for potentially deep recursions.
sys.setrecursionlimit(10 ** 7)         # Set the maximum depth of the Python interpreter stack. Useful for deep recursions (common in tree/graph dfs).

# Import numpy for efficient array and numerical computations.
import numpy as np

# From scipy.sparse, import a representation for sparse matrices.
from scipy.sparse import csr_matrix    # Compressed Sparse Row matrix, efficient for row slicing and matrix operations.
from scipy.sparse.csgraph import depth_first_order   # Efficient dfs traversal for graphs in sparse matrix form.

MOD = 10**9 + 7   # Define a modulus, common in competitive programming to prevent integer overflow.

# Read the number of nodes (vertices) in the tree.
N = int(readline())

# Read the rest of the input, map each value to integer.
# The input should contain 2*(N-1) integers (for N-1 edges, undirected).
XY = list(map(int, read().split()))

# Create an adjacency matrix for the tree in CSR (Compressed Sparse Row) format.
# [1]*(N-1): Means each edge gets a value "1" (the weight, but as an unweighted graph).
# XY[::2]: Gives the start node of each edge.
# XY[1::2]: Gives the end node of each edge.
# Shape is (N+1, N+1): This assumes nodes are labeled from 1 to N, so index 0 is unused.
graph = csr_matrix(
    ([1] * (N - 1), (XY[::2], XY[1::2])),
    (N + 1, N + 1)
)

# Compute DFS order and parent list from given graph starting at node 1.
# dfs_order: array of vertex IDs in the order they are first visited.
# par: parent of each node in the DFS tree (-9999 or similar for root).
dfs_order, par = depth_first_order(graph, 1, directed=False)
dfs_order = dfs_order.tolist()     # Convert from numpy array to Python list for easier use.
par = par.tolist()

# Prepare an array to store the size of the subtree rooted at each node.
# Initially, set size 1 for every node (each is counted as its own subtree).
subtree_size = [1] * (N + 1)

# Boolean flags to keep track of whether each node is (possibly) a centroid.
is_cent = [True] * (N + 1)         # Start assuming all nodes could be centroids.

# Process nodes in dfs reverse order (from leaves towards root).
for v in dfs_order[::-1]:
    # If the current subtree size is too small, v cannot be a centroid
    if subtree_size[v] < (N + 1) // 2:
        is_cent[v] = False
    # Get the parent of node v.
    p = par[v]
    # If p < 0, we have reached beyond the root; stop processing.
    if p < 0:
        break
    # If subtree rooted at v is too big (more than half the tree), its parent cannot be centroid.
    if subtree_size[v] > N // 2:
        is_cent[p] = False
    # Propagate subtree sizes up: parent accumulates from its children.
    subtree_size[p] += subtree_size[v]

# List of centroid nodes.
# By definition, a centroid is a node where none of its children have more than N//2 nodes,
# and also the rest of the tree (after removing that node) does not exceed N//2.
centroid = [v for v in range(1, N + 1) if is_cent[v]]  # Exclude node 0 (unused).
Ncent = len(centroid)  # Number of centroids; can be 1 or 2.

# Now, depending on the number of centroids, calculate partition sizes of the subtrees.
if Ncent == 1:
    # For one centroid c, its "outside" component has size N - subtree_size[c],
    # and for each direct child v of c, its subtree size is subtree_size[v].
    c = centroid[0]
    # Compose the sizes: the component outside c, plus one for each child component.
    sizes = [N - subtree_size[c]] + [subtree_size[v] for v in range(1, N + 1) if par[v] == c]
else:
    # For two centroids, the tree splits into two parts of size N//2 each.
    sizes = [N // 2, N // 2]

# Function: computes cumulative product modulo MOD (for efficient n! computation).
def cumprod(arr, MOD):
    # arr: numpy array of integers.
    # L: length of array.
    L = len(arr)
    # Lsq: define a size (nearest square above length L for reshaping a square grid).
    Lsq = int(L ** .5 + 1)
    # Resize arr to a square grid, shape (Lsq, Lsq). Some entries may be invalid but np.resize pads with repeats.
    arr = np.resize(arr, Lsq ** 2).reshape(Lsq, Lsq)
    # Multiply cumulatively along rows (axis 1).
    for n in range(1, Lsq):
        arr[:, n] *= arr[:, n - 1]
        arr[:, n] %= MOD
    # Multiply cumulatively along columns (axis 0), propagate last column downward.
    for n in range(1, Lsq):
        arr[n] *= arr[n - 1, -1]
        arr[n] %= MOD
    # Flatten 2D square back to 1D array, truncate back to length L, and return.
    return arr.ravel()[:L]

# Function: precomputes factorial and inverse factorial arrays up to U.
def make_fact(U, MOD):
    # x: array of integers from 0 to U-1 (for factorials).
    x = np.arange(U, dtype=np.int64)
    x[0] = 1   # 0! defined as 1.
    fact = cumprod(x, MOD)   # Compute 1!, 2!, ..., (U-1)!
    # x for inverse factorial: descending from U to 1.
    x = np.arange(U, 0, -1, dtype=np.int64)
    # Modular inverse using Fermat's little theorem as MOD is prime:
    # fact[-1] = (U-1)!
    # pow(a, MOD-2, MOD) returns the modular inverse of a modulo MOD.
    x[0] = pow(int(fact[-1]), MOD - 2, MOD)
    fact_inv = cumprod(x, MOD)[::-1]   # Reverse back to have inv fact for 0,1,...,U-1.
    return fact, fact_inv

# Precompute factorial (fact) and inverse factorial (fact_inv) for all required up to N+100.
fact, fact_inv = make_fact(N + 100, MOD)   # Large enough so all binomials and partitions fit.

# Function: constructs an array that encodes the number of ways to partition a component of size n.
def create_component_arr(n):
    # Start with x: array of length n+1, set all values to n! mod MOD.
    x = np.full(n + 1, fact[n], dtype=np.int64)
    # Multiply by inverse factorial for (n-k): this is for binomial coefficients.
    x *= fact_inv[n::-1]
    x %= MOD
    # Multiply again by x: this is equivalent to (n!/(n-k)!) * n! = n!^2/(n-k)!
    x *= x
    x %= MOD
    # Multiply by inverse factorial for k!; now this is n!^2 / ((n-k)! * k!)
    x *= fact_inv[:n + 1]
    x %= MOD
    # For odd k, multiply by -1 (alternating signs), using Python slice notation.
    x[1::2] *= (-1)
    x %= MOD
    return x

# Function: performs a convolution, i.e., polynomial multiplication of two arrays x and y modulo MOD.
def convolve(x, y):
    Lx = len(x)
    Ly = len(y)
    # Ensure that x is the longer polynomial for efficiency.
    if Lx < Ly:
        Lx, Ly = Ly, Lx
        x, y = y, x
    # Allocate result array of correct length (the resulting degree = sum of degrees).
    z = np.zeros(Lx + Ly - 1, np.int64)
    # Do the convolution: for each term in y, combine it with all of x, sliding window.
    for n in range(Ly):
        z[n:n + Lx] += x * y[n] % MOD
    # Take result modulo MOD after all additions.
    return z % MOD

# Initialize final answer polynomial with [1] (degree 0).
x = np.array([1], np.int64)

# For each component size computed earlier, convolve with its characteristic array.
for s in sizes:
    x = convolve(x, create_component_arr(s))

# The answer differs for single and double centroid cases:
if Ncent == 1:
    # Single centroid: sum up the terms weighted by factorials, from N to 1.
    answer = (x * fact[N:0:-1] % MOD).sum() % MOD
else:
    # Double centroid: sum up each term times factorial from N down to 0.
    answer = (x * fact[N::-1] % MOD).sum() % MOD

# Finally, print the answer.
print(answer)