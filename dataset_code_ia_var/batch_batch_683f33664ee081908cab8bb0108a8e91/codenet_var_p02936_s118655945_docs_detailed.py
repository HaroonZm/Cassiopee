def main():
    """
    Main function to process a rooted tree and perform incremental updates
    at given nodes, then propagate the increments to all descendants. 
    Finally, it prints the accumulated value at each node after all operations.
    """
    # Read number of nodes in tree (N) and number of queries (Q)
    N, Q = map(int, input().split())
    
    # Initialize adjacency list for the tree.
    # Each index in 'point' represents a node, and contains a list of its children.
    point = [[] for _ in range(N)]
    
    # Initialize the list to store extra value added to each node from queries.
    plus = [0] * N

    # Read N-1 edges to build the tree.
    # The input edges are 1-indexed; converting to 0-indexed.
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1  # convert to 0-based indexing
        b -= 1  # convert to 0-based indexing
        point[a].append(b)

    # Apply the Q queries that increment the value at node p by x.
    for _ in range(Q):
        p, x = map(int, input().split())
        p -= 1  # convert to 0-based indexing
        plus[p] += x

    # Initialize the answer list to store the propagated value for each node.
    ans = [0] * N

    # Use a stack to perform an explicit depth-first traversal starting from the root (node 0).
    # Each stack item is a tuple: (current_node, inherited_value)
    dfs = [(0, 0)]
    while len(dfs):
        n, p = dfs.pop()
        # Add the value explicitly set at this node
        p += plus[n]
        # Store cumulative value at this node
        ans[n] = p
        # Traverse each child, passing down the cumulative sum
        for child in point[n]:
            dfs.append((child, p))

    # Output the answer as space-separated values.
    for a in ans:
        print(a, end=' ')
    print()

if __name__ == "__main__":
    main()