import sys

# Assign sys.stdin.readline to the variable 'input' for fast input
# sys.stdin.readline() reads a whole line (including '\n') from standard input (usually faster than input())
input = sys.stdin.readline

# Read an integer value from input, which represents 'n'
n = int(input())

# Read a line of input, split it into separate values, convert each to integer, and collect them into a list called 'b'
# 'b' is a list of numbers (most likely 0 or 1 values based on later code)
b = list(map(int, input().split()))

# Create a list called 'ope' with 'n' empty lists (one for each index from 0 to n-1)
# This will store, for each index, a list of left-endpoints 'l' for ranges ending at that position
ope = [[] for i in range(n)]

# Read an integer 'Q', representing the number of queries (or operations)
Q = int(input())

# For each of the Q queries, do the following:
for i in range(Q):
    # Read two integers l and r from input, representing a range [l, r]
    l, r = map(int, input().split())
    # Adjust values to 0-based indices (subtract 1 from both l and r as Python lists are zero-based)
    # For the right endpoint r-1, append the left endpoint l-1 to its list of operations
    ope[r-1].append(l-1)

# Count the number of zeros in list 'b' using list.count(), store it in 'res'
res = b.count(0)

# Create a list 'Data' where each element is either 1 or -1 depending on b[i]
# 'b[i]==1' is True (1) if b[i] is 1, else False (0)
# ((b[i]==1)+1) becomes 2 if b[i] is 1, or 1 otherwise
# (-1)**2 is 1, (-1)**1 is -1, so 'Data' gets 1 if b[i] is 1, -1 if b[i] is not 1 (i.e., 0)
Data = [(-1)**((b[i]==1)+1) for i in range(n)]

# Now, for each i from 1 to n-1, cumulatively add previous value to the current
for i in range(1, n):
    Data[i] += Data[i-1]

# Insert 0 at the start of Data, so its length becomes n+1 and indices match certain usages in the code
Data = [0] + Data

# For each list within 'ope', sort it in reverse order (highest first) - will be helpful when popping largest element first
for i in range(n):
    ope[i].sort(reverse=True)

# Set 'N' to n + 1, because we'll work with a range including n
N = n + 1

# N0 is set to the smallest power of two greater or equal to N
# This is useful for constructing a segment tree that is easy to index
N0 = 2**((N-1).bit_length())

# Create a list 'data' of size 2*N0 for the segment tree nodes, initialized with None
data = [None] * (2 * N0)

# Define a constant INF which is a tuple of two large negative numbers
# Used as a sentinel value in segment tree queries
INF = (-2**31, -2**31)

# Define a function 'update' to update the values in the segment tree
# The function updates all intervals [l, r), setting those to 'v'
# 'v' is expected to be a tuple (t, value), where t is a timestamp or priority, value is the value itself
def update(l, r, v):
    # Shift the indices to the proper position in the segment tree
    L = l + N0
    R = r + N0
    # Loop while L < R, which means we still have covered all relevant intervals
    while L < R:
        # If R is odd (i.e., last element on the right), process reduction of R
        if R & 1:
            R -= 1
            # If data at node R-1 exists (is not None), assign the maximum of existing and v
            if data[R-1]:
                data[R-1] = max(v, data[R-1])
            else:
                # Otherwise, simply assign v
                data[R-1] = v
        # If L is odd (i.e., first element on the left), process and move L right
        if L & 1:
            if data[L-1]:
                data[L-1] = max(v, data[L-1])
            else:
                data[L-1] = v
            L += 1
        # Move up in the tree (shift bits to right by 1 divides by 2)
        L >>= 1
        R >>= 1

# Define a function '_query' which, given an index k, returns the maximum (t, value) along the path from the leaf to the root
def _query(k):
    # Shift k to leaf position
    k += N0 - 1
    # Start from INF, which is a tuple of very low values, ensuring any real value replaces it
    s = INF
    # Traverse layer-by-layer upwards from leaf to root in the segment tree
    while k >= 0:
        if data[k]:
            s = max(s, data[k])
        # Move k to its parent (index of parent node)
        k = (k - 1) // 2
    return s

# Define query(k) to fetch the value (not t) for position k as stored in the segment tree
def query(k):
    # '_query(k)' returns a tuple (t, value), but we only want the value
    return _query(k)[1]

# Initialize the segment tree so that, for each index from 0 to n,
# we assign both t and value as -Data[i] (for proper propagation and queries)
for i in range(n + 1):
    update(i, i + 1, (-Data[i], -Data[i]))

# If there are operations ending at position 0, set the value at position 1 to (0,0)
if ope[0]:
    update(1, 2, (0, 0))

# For each index from 1 to n-1, perform DP update and process all attached operations (left-ends) at this right-end
for i in range(1, n):
    # Query the current value at position i
    val = query(i)
    # Update the segment tree at position i+1 so it reflects the correct DP transform
    # The value is set considering cumulative Data differences
    update(i+1, i+2, (val + Data[i] - Data[i+1], val + Data[i] - Data[i+1]))
    # For every left endpoint l for operations ending at position i
    for l in ope[i]:
        # Find current value at position l
        val = query(l)
        # Propagate this value as a possible optimal value to every position in [l+1, i+2)
        update(l+1, i+2, (val, val))

# After all processing, the answer is n minus (number of zeros in b + query at n + cumulative sum at n)
# query(n) returns the minimum changes needed up to n, and Data[n] is the prefix sum up to n
print(n - (res + query(n) + Data[n]))