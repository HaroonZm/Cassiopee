from collections import deque
import sys

# Shortcut references for standard input and output
readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    """
    Reads a tree structure and processes it to find the maximum possible value
    according to a custom dynamic programming on trees approach
    with a subtree size constraint K.

    The function expects the following input via stdin:
      - The first line contains two integers N and K: number of nodes and a size constraint.
      - The next N-1 lines each contain two integers u and v, representing undirected edges.

    Output:
      - A single integer, which is the maximum value computed based on subtree DP.
    """

    # Read the number of nodes N and the constraint K
    N, K = map(int, readline().split())
    
    # Initialize the adjacency list for the tree with N nodes
    G = [[] for _ in range(N)]
    
    # Read and build the tree edges (1-based index in input, convert to 0-based)
    for _ in range(N - 1):
        u, v = map(int, readline().split())
        G[u - 1].append(v - 1)
        G[v - 1].append(u - 1)
    
    # BFS initialization
    P = [-1] * N        # Parent array for each node (P[child] = parent)
    vs = []             # List to store the nodes in BFS order
    que = deque([0])    # Start BFS from the root node (node 0)
    used = [0] * N      # Array to mark which nodes have been visited
    used[0] = 1         # Mark the root as visited

    # Perform BFS to generate BFS order and parent relation
    while que:
        v = que.popleft()
        vs.append(v)
        for w in G[v]:
            if used[w]:
                continue  # Skip already visited nodes
            used[w] = 1
            que.append(w)
            P[w] = v     # Set parent of child node
    
    # Arrays to store subtree sizes and DP values for each node
    sz = [0] * N        # sz[v]: size of subtree rooted at node v
    dp = [0] * N        # dp[v]: DP value for node v
    
    ans = 0             # Variable to keep track of the answer
    
    # Process nodes in post-order (from leaves to root)
    vs.reverse()
    for v in vs:
        s = 1               # Initial size of current subtree (count itself)
        d = 0               # Counter for children with subtree size >= K
        p = P[v]            # Parent of the current node
        ds = []             # For storing adjusted DP values of the children
        
        # Process all adjacent nodes (children)
        for w in G[v]:
            if w == p:
                continue    # Don't revisit parent
            s += sz[w]      # Add subtree size of child
            if sz[w] >= K:
                d += 1  # This child is a "big" child (size >= K)
                ds.append(dp[w] - 1)  # Extra edge reduction in DP for big child
            else:
                ds.append(dp[w])
        
        # Sort adjusted DP values descending for optimal selection
        ds.sort(reverse=True)
        
        # Compute DP value for current node
        # Either take only d, or d + largest ds element if any exists
        dp[v] = max(d, d + ds[0] if ds else 0)
        
        # Try to update answer using the optimal combination
        if ds:
            # Compute extra factor if the rest of the tree (above current v)
            # is big enough to be considered as a "big child"
            e = d + 1 if N - s >= K else d
            # Consider taking the largest child (ds[0])
            ans = max(ans, e + ds[0])
            # Optionally, take the two largest (ds[0] + ds[1]) if available
            if len(ds) > 1:
                ans = max(ans, e + ds[0] + ds[1])
        
        # Register the computed subtree size
        sz[v] = s
    
    # Output the final answer
    write("%d\n" % ans)

# Entry point to start processing
solve()