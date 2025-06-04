# Importing the sys module which provides access to system-specific parameters and functions
import sys

# Importing itertools for combination utilities, though in this code we will not need it
import math

# Define a constant for the maximum possible nodes (20)
MAXN = 20

# Define the infinite value, a very large integer (equivalent to 1e9)
INF = int(1e9)

# The program does not specify MOD or EPS constants, so we omit them

# We enter an infinite loop to continuously process multiple test cases,
# like a contest environment which expects input until a sentinel (0 0)
while True:
    # Read a line from standard input, remove leading/trailing whitespace,
    # and split it into a list of string items
    raw_input_line = sys.stdin.readline().strip()
    
    # If we've reached end of input, break out of the loop
    if not raw_input_line:
        break

    # Split the line into a list of strings
    parts = raw_input_line.split()

    # If less than 2 numbers, either empty or invalid line, break (skip)
    if len(parts) < 2:
        break

    # Extract the number of nodes (n) and required total cost (m), converting from string to int
    n, m = int(parts[0]), int(parts[1])

    # If both n and m are zero, this is the sentinel value to terminate input, so exit the loop
    if n == 0 and m == 0:
        break

    # Initialize an array for the node costs. Size is fixed to 20 as in the C++ code's array<int, 20>
    cs = [0] * MAXN

    # Initialize a list of lists representing the DAG (directed acyclic graph).
    # Each list at index i contains the immediate child nodes of node i
    g = [[] for _ in range(n)]

    # For each node, process its cost and edges
    i = 0  # Index for current node
    node_lines = []
    # Now we want to collect the next n lines of input for each node
    while len(node_lines) < n:
        # Read the next line of node data and split into items
        node_line = sys.stdin.readline().strip()
        if node_line:
            node_lines.append(node_line)
    # Now node_lines has n lines, one for each node

    # Process each node's data
    for i in range(n):
        # Each line starts with the node's cost, followed by the number of children, then the child indices
        items = list(map(int, node_lines[i].split()))
        # The first number is the node's cost
        cs[i] = items[0]
        # The second number is the number k of children
        k = items[1]
        # The next k numbers are the child indices (can be zero children)
        for j in range(k):
            r = items[2 + j]
            # Append this child index to the adjacency list of node i
            g[i].append(r)

    # This array will store for each node i the bitmask of nodes reachable from i (including itself)
    bs = [0] * MAXN

    # Define a depth-first search function to calculate reachable nodes for a given start node u
    # This function will perform a DFS starting at node u and mark all reachable nodes (including itself)
    def dfs(g, u):
        # Begin with a bitmask with only the u-th bit set (2^u)
        res = 1 << u
        # For every node v that is a direct child (outgoing edge from u), perform a DFS
        for v in g[u]:
            # The result mask is updated using bitwise OR assignment,
            # combining it with the mask from the subtree rooted at v
            res |= dfs(g, v)
        # Return the final bitmask representing all nodes reachable starting from u
        return res

    # For each node i, compute and store the bitmask of reachable nodes in bs
    for i in range(n):
        bs[i] = dfs(g, i)

    # Initialize a list to store the sum of costs for each subset (represented as a bitmask)
    # There are 2^n possible subsets, so the list has size 2^n
    sums = [0] * (1 << MAXN)
    # We only care about subsets composed of the first n nodes

    # For singleton sets (subset containing exactly one node),
    # sums[1 << i] is set to the cost of node i
    for i in range(n):
        sums[1 << i] = cs[i]

    # Now compute the sum of costs for all possible subsets using dynamic programming
    # This uses the well-known "Sum Over Subsets" technique.
    # For each subset i (represented as a bitmask), we calculate sums[i] as the sum of the cost of the lowest-set bit
    # and the sum for the subset with that bit unset.
    for i in range(1, 1 << n):
        # i & -i isolates the lowest set bit of i, i-(i&-i) clears that bit.
        # Sums of i = sums of the singleton represented by lowest set bit + sums of the rest
        # This ensures we add the cost for each included node exactly once per subset
        sums[i] = sums[i & -i] + sums[i - (i & -i)]

    # The result variable will track the minimum number of nodes required to achieve a cost >= m for all reachable nodes
    # Start with infinite value, meaning we haven't found a valid subset yet.
    res = INF

    # For each possible subset of the n nodes (represented as bitmask "i" from 0 to 2^n-1)
    for i in range(1 << n):
        # The number of selected nodes in subset i is the number of bits set to 1 (i.e., cardinality of the subset)
        selected_count = bin(i).count('1')
        # Only consider subsets where the number of selected nodes is less than the current best res
        if selected_count < res:
            # For each subset, calculate the union of all nodes reachable from the selected nodes
            # b will store the combined reachable nodes as a bitmask
            b = 0
            for j in range(n):
                # If j-th node is selected in subset i ((i >> j) & 1 checks if jth bit is set)
                if ((i >> j) & 1):
                    # Combine reachable nodes from j into the union by bitwise OR
                    b |= bs[j]
            # Now, b's bitmask represents all nodes reachable from the selected set
            # If the sum of costs for those reachable nodes is at least m, this is a valid solution
            if sums[b] >= m:
                # Update the result to be the minimum among candidates so far
                if selected_count < res:
                    res = selected_count

    # Output the found result (minimum number of starting nodes)
    print(res)