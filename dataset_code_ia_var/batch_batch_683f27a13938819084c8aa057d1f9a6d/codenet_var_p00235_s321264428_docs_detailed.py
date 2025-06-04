def tree_walk_1(start, parent=None):
    """
    Traverse the tree rooted at 'start', recording parent and edge information for each node.

    Args:
        start (int): Current node being traversed.
        parent (int, optional): Parent node of the current node. Defaults to None.

    Side effects:
        Updates the global lists P and C:
            - P[i]: tuple of (parent, edge_length) for node i.
            - C[start]: list of (child, edge_length) tuples for node 'start'.
    """
    for i, t in adj[start]:
        if i != parent:
            P[i] = (start, t)  # Record parent and edge length for child node 'i'
            C[start].append((i, t))  # Add child 'i' and edge length to children list of 'start'
            tree_walk_1(i, start)  # Recursively traverse child


def tree_walk_2(start):
    """
    Recursively traverses the tree to calculate the total travel time needed to visit all nodes,
    according to the problem's visiting rules.

    Args:
        start (int): Current node being visited.

    Side effects:
        Updates the global variable 'time' to accumulate the total time spent.
        Marks nodes as visited in the global 'notVisited' list.

    Uses:
        - C: children list for each node.
        - P: parent edge for each node.
        - notVisited: tracks nodes that haven't been visited.
    """
    global time
    notVisited[start] = False  # Mark the current node as visited
    for c, t1 in C[start]:  # Iterate over all children of the current node
        if notVisited[c]:
            time += 2 * t1  # Add twice the edge weight (go & return)
            tree_walk_2(c)  # Recursively visit child
    p, t2 = P[start]  # Obtain parent and edge length to parent
    if notVisited[p]:
        time += t2  # Add only the edge weight to parent
        tree_walk_2(p)  # Recursively visit parent


from sys import stdin

# Read input from stdin
f_i = stdin

while True:
    # Read the number of nodes
    N = int(f_i.readline())
    if N == 0:
        break  # End of input

    # Build adjacency list for the tree
    adj = [[] for i in range(N)]
    for i in range(N - 1):
        a, b, t = map(int, f_i.readline().split())
        a -= 1  # Convert to 0-based index
        b -= 1
        adj[a].append((b, t))  # Edge from a to b with length t
        adj[b].append((a, t))  # Edge from b to a with length t (undirected)

    # "Leaf cutting": remove leaves except for root (node 0) to create a pruned tree
    lf = []
    for i, a in enumerate(adj[1:], start=1):
        if len(a) == 1:
            lf.append(i)
    for l in lf:
        # Remove the only connection from the leaf node
        i, t = adj[l].pop()
        adj[i].remove((l, t))  # Remove the reversed edge too

    # Find root candidates: nodes (except root) with degree 1 (leaf nodes after pruning)
    rc = [i for i, a in enumerate(adj[1:], start=1) if len(a) == 1]
    if not rc:
        # No remaining leaves, then minimum time is zero
        print(0)
        continue

    time_rec = []  # List to store time results for all root candidates

    # Evaluate all root candidates
    for r in rc:
        # Initialize parent and children lists for the tree
        P = [None] * N  # P[i] = (parent, edge_length)
        P[r] = (r, 0)   # Root has itself as parent; edge length zero
        C = [[] for i in range(N)]  # C[i]: children list for node i
        tree_walk_1(r)  # Build parent/children structure for the tree

        # Prepare for traversal to compute total time
        time = 0
        notVisited = [True] * N  # Track nodes that remain unvisited
        tree_walk_2(0)           # Always start traversal from root (node 0)
        time_rec.append(time)

    print(min(time_rec))  # Output the minimal travel time among all options