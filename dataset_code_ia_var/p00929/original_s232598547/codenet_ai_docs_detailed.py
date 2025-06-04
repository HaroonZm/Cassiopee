def main():
    """
    Main function to compute the number and total cost of "bridge" edges in a minimum spanning forest constructed from a set of weighted undirected edges.
    It reads the graph, builds its Minimum Spanning Tree, and finds all bridge edges (critical edges).
    """

    # Read input: N = number of nodes, M = number of edges
    N, M = map(int, input().split())

    # E0 will store all edges as (cost, start, dest)
    E0 = []
    for i in range(M):
        S, D, C = map(int, input().split())
        E0.append((C, S-1, D-1))  # Use zero-based indexing for nodes

    # Sort all edges by cost in non-decreasing order (for Kruskal's algorithm)
    E0.sort()

    # Disjoint set union-find initialization (for Kruskal's algorithm)
    parent = list(range(N))

    def root(x):
        """
        Find the root parent of node x with path compression.

        Args:
            x (int): Node index

        Returns:
            int: The representative (root) of node x
        """
        if x == parent[x]:
            return x
        # Path compression
        parent[x] = root(parent[x])
        return parent[x]

    def unite(x, y):
        """
        Unites the sets containing x and y.

        Args:
            x (int): First node
            y (int): Second node
        """
        px = root(x)
        py = root(y)
        if px < py:
            parent[py] = px
        else:
            parent[px] = py

    # Kruskal's algorithm: Build MST and determine the maximal edge cost in the MST (base)
    cnt = 0      # Number of selected edges
    base = None  # The maximum cost in the MST
    for i in range(M):
        C, S, D = E0[i]
        if root(S) != root(D):
            unite(S, D)
            cnt += 1
            if cnt == N - 1:  # All nodes are connected
                base = C  # The largest cost used in the MST

    # Prepare sets of all edges with cost <= base (MST or ties)
    ES = {}  # Edges by cost: {cost: set((s, d), ...)}
    CM = {}  # Map from edge (s,d) to its cost
    for i in range(M):
        C, S, D = E0[i]
        if C <= base:
            ES.setdefault(C, set()).add((S, D))
            CM[S, D] = C

    def bridge(G, N):
        """
        Finds all bridges (critical edges) in an undirected graph.

        Args:
            G (list of list): The graph as adjacency lists.
            N (int): Number of nodes.

        Returns:
            set: Set of (u, v) tuples representing bridges where u < v.
        """
        result = set()        # Set for bridges
        label = [None] * N    # Depths or timestamps of visitation for DFS
        gen = 0               # "Global" time counter, incremented each new node
        cost = [0] * N        # Used for backedge counting

        def dfs(u, p):
            """
            Depth-First Search helper to search for bridges.

            Args:
                u (int): Current node
                p (int): Parent node

            Returns:
                int: Number of backedges passing through u to its ancestors
            """
            nonlocal gen
            res = 0
            for v in G[u]:
                if v == p:
                    continue
                if label[v] is not None:
                    if label[v] < label[u]:
                        # Found a back edge to ancestor
                        cost[v] += 1
                        res += 1
                else:
                    label[v] = gen
                    gen += 1
                    r = dfs(v, u)
                    if r == 0:
                        # Edge (u, v) is a bridge (no back-edges over it)
                        result.add((u, v) if u < v else (v, u))
                    res += r
            res -= cost[u]
            return res

        # Start a DFS from every unvisited node
        for v in range(N):
            if label[v] is None:
                label[v] = gen
                gen += 1
                r = dfs(v, -1)
                assert r == 0, r  # Sanity check: all backedges processed

        return result

    # Build up the graph step-by-step for all edges with cost <= base
    G = [[] for _ in range(N)]  # Adjacency list for the current graph
    cnt = 0                     # Count of bridge edges
    ans = 0                     # Total cost for bridges

    # For every cost in increasing order, update the graph and check bridges
    for C in sorted(ES):
        for S, D in ES[C]:
            G[S].append(D)
            G[D].append(S)

        # Compute the set of bridges in the current graph snapshot
        B = bridge(G, N)

        # Find intersection: only count newly added edges with cost C that are bridges
        bridge_edges = B & ES[C]
        cnt += len(bridge_edges)
        ans += len(bridge_edges) * C

    print(cnt, ans)

if __name__ == "__main__":
    main()