# Import the sys module, which provides access to some variables used or maintained by the Python interpreter
import sys

# Set up input reading with lower-level byte interfaces from sys.stdin
# sys.stdin.buffer is a buffered binary interface to standard input
# read reads all remaining input at once as bytes. Assign the function to 'read'
read = sys.stdin.buffer.read
# readline reads a single line from standard input as bytes. Assign this function to 'readline'
readline = sys.stdin.buffer.readline
# readlines reads all remaining lines from standard input as bytes, returning a list. Assign this function to 'readlines'
readlines = sys.stdin.buffer.readlines

# Import the numpy library and assign it to the commonly used alias 'np'.
import numpy as np

# Read a line from standard input, which will contain an integer N, and remove any trailing newline byte (\n)
# Convert the bytes to integer using int(), since readline() returns bytes
N = int(readline())

# Read the rest of the input in one call, which will contain N-1 pairs of integers representing edges
# Use read() to get all remaining input as bytes
# Split the bytes into a list of bytes objects for each integer using split()
# Map each bytes object to an int to create an iterator of integers
m = map(int, read().split())

# Use zip to pair up the mapped integers into 2-tuples (representing edges)
# zip(m, m) pairs each consecutive pair: (m0, m1), (m2, m3), ...
AB = zip(m, m)

# Initialize the adjacency list for the graph as a list of empty lists
# The graph has N+1 nodes (1-indexed for convenience), so create N+1 empty lists
graph = [[] for _ in range(N+1)]

# Iterate through each edge (a, b) in AB
for a, b in AB:
    # For an undirected graph, add b to the adjacency list of a, and a to the adjacency list of b
    graph[a].append(b)
    graph[b].append(a)

# Choose vertex 1 as the root of the tree (assuming the tree is rooted at 1)
root = 1

# Initialize the parent array, with N+1 zeros (since nodes are 1-indexed)
# parent[x] will store the parent of node x in the tree, or 0 if x is the root
parent = [0] * (N+1)

# Initialize an empty list order to store the order in which nodes are visited in a traversal (DFS order)
order = []

# Initialize a stack for depth-first search traversal, starting with the root node
stack = [root]

# While there are nodes left to process in the stack
while stack:
    # Remove (pop) the last node added to the stack. This is how DFS is implemented with a stack
    x = stack.pop()
    # Append the current node to the traversal order
    order.append(x)
    # Iterate over all neighbors y of the current node x
    for y in graph[x]:
        # If y is the parent of x, skip it (prevent revisiting the parent)
        if y == parent[x]:
            continue
        # Set the parent of y to be x
        parent[y] = x
        # Add y to the stack to continue DFS traversal
        stack.append(y)

# Define a bitmask with all bits set to 1 up to 60 bits (full mask for all possible colors, as 2^60 is more than enough)
# The parenthesis is needed for grouping: (1 << 60) means 1 shifted left by 60, which is 2^60
# Subtract 1 to get a number with 60 ones in binary
full = (1 << 60) - 1

# Initialize arrays for the algorithm, each with N+1 elements (1 per node)
# uninity[x] will store the least significant bit representing the color assigned to node x
uninity = [0] * (N+1)
# dp[x] will keep track of used color bitmasks for the subtree rooted at x
dp = [0] * (N+1)
# twice[x] will track colors that are assigned more than once within the subtree of node x
twice = [0] * (N+1)

# Traverse the tree in reverse order (from leaves up to the root) according to the DFS traversal order
for x in order[::-1]:
    # Get parent of the current node x
    p = parent[x]
    
    # Compute n as the position of the highest bit set in twice[x], minus one
    # bit_length returns the number of bits necessary to represent the integer in binary
    # If twice[x] is 0, bit_length() returns 0, so n becomes -1 in that case
    n = twice[x].bit_length() - 1
    
    # If n >= 0, meaning there are some "twice-assigned" colors in the subtree of x:
    if n >= 0:
        # Set the lowest (n+1) bits of dp[x] to 1 using a bitmask
        # (1 << (n+1)) shifts 1 left by (n+1), subtract 1 to turn the lowest (n+1) bits on
        dp[x] |= (1 << (n+1)) - 1
    
    # Determine which colors can be used for this node (those not already used in the subtree)
    # Take bitwise NOT of dp[x], AND with full to confine the result to 60 bits
    can_use = full & (~dp[x])
    
    # Extract the least significant bit set to 1 in can_use
    # -can_use is the two's complement (bitwise negation plus one), ANDing gives only the lowest set bit
    lsb = can_use & (-can_use)
    
    # Store this bit as the color for node x
    uninity[x] = lsb
    
    # Mark this color as now used in dp[x]
    dp[x] |= lsb
    
    # To avoid using lower colors in parent or siblings, mask out any colors lower than current lsb by setting them to zero
    # (lsb - 1) will have all lower bits set; ~ (lsb - 1) will be ones everywhere except for those lower bits
    dp[x] &= full & ~(lsb - 1)
    
    # Update twice[p] by OR'ing in all colors used both in dp[x] and dp[p] (indicating colors used more than once)
    twice[p] |= (dp[x] & dp[p])
    
    # Update dp[p] by OR'ing in all colors now used in dp[x]
    dp[p] |= dp[x]

# Find the maximum value in uninity (i.e., the largest color used among all nodes)
x = max(uninity)

# The answer is the position of the highest set bit in x, minus 1 (because bit positions are zero-indexed)
# This gives the maximum color index used
answer = x.bit_length() - 1

# Print the answer to standard output
print(answer)