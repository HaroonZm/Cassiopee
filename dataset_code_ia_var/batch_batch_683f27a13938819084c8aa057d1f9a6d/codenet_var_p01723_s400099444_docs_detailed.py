import sys
from collections import deque

readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    """
    Main function that reads the input, builds the tree, precomputes combination counts,
    performs a dynamic programming depth-first search (DFS), and outputs the result.

    Problem structure:
    - Reads an integer N (number of nodes in a tree)
    - Reads N-1 edges (directed from a to b) building a rooted tree
    - Builds dynamic programming tables for merging subproblem solutions
    - Calculates, using DFS, the number of valid ways to label/organize the tree structure
      (the exact context may depend on the problem, but the code is generic for rooted trees)
    """

    MOD = 10 ** 9 + 7  # Large prime modulus for calculations to prevent overflow

    # Read the size of the tree (number of nodes)
    N = int(readline())

    # Precompute combination rules in a 3D DP array.
    # dp0[c][a][b]: Number of ways to merge multisets of size a and b into a set of size c,
    # considering the merging rules (here simulating combinations for trees).
    dp0 = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
    dp0[0][0][0] = 1  # Base case: 0 elements merged from 0 and 0 gives 1 way

    # Fill dp0 via dynamic programming.
    # dp0[c][a][b] is the number of ways to make a forest of size c by merging
    # subforests of sizes a and b.
    for c in range(1, N + 1):
        for a in range(N + 1):
            for b in range(N + 1):
                r = 0
                if a:
                    r += dp0[c - 1][a - 1][b]       # Add one from left subtree
                if b:
                    r += dp0[c - 1][a][b - 1]       # Add one from right subtree
                if a and b:
                    r += dp0[c - 1][a - 1][b - 1]   # Add one from both subtrees at once
                dp0[c][a][b] = r % MOD

    # Build the tree structure as adjacency lists and in-degree array.
    G = [[] for _ in range(N)]       # G[i]: List of children from node i
    deg = [0] * N                    # deg[i]: In-degree (number of incoming edges) for node i

    # Read edges; the tree may not be rooted at node 0, so deg/queue will find root.
    for i in range(N - 1):
        a, b = map(int, readline().split())
        G[a].append(b)    # Edge from node a to node b
        deg[b] += 1       # Track in-degree for each node

    # Find the root node (unique node with in-degree 0)
    r = 0
    for i in range(N):
        if deg[i] == 0:
            r = i
            break

    # Topological order the nodes (from leaves up to the root) using BFS
    que = deque([r])  # Queue for BFS starting from the root
    vs = []           # List to store nodes in BFS order
    while que:
        v = que.popleft()
        vs.append(v)
        for w in G[v]:
            que.append(w)
    vs.reverse()  # Reverse to process nodes from leaves to root

    # Compute height of subtree rooted at each node
    hs = [0] * N  # hs[i]: height of the subtree rooted at node i
    for v in vs:
        e = 0     # Height variable for current node
        for w in G[v]:
            e = max(e, hs[w] + 1)  # Height is one more than the maximum height of children
        hs[v] = e

    def dfs(v):
        """
        Performs a DP-based DFS on the tree rooted at node v.

        For each node, computes an array res where res[i] is the number of subtree structures
        with i nodes below this node.

        Returns:
            list[int]: Array containing number of arrangements per subtree size.
        """
        res = [1]  # Initially only the empty subtree; res[0] = 1
        hv = 0     # Total number of nodes in the subtree so far

        # Process all children and merge the DP arrays with root v
        for w in G[v]:
            r = dfs(w)          # Recursive call: DP array for child w
            hw = len(r) - 1     # Size of the subtree of w
            r0 = [0] * (hv + hw + 1)  # DP array for merging this child into current result

            # Merge the DP arrays using the precomputed dp0 table
            for i in range(hv + 1):          # Nodes picked from the current res
                for j in range(hw + 1):      # Nodes picked from current child
                    for k in range(max(i, j), i + j + 1):  # All possible merged sizes
                        # Update number of ways for merged size k
                        r0[k] += res[i] * r[j] * dp0[k][i][j] % MOD
            res = r0      # Set the result to the merged DP array
            hv += hw      # Update the size of the merged subtree

        return [0] + res  # Shift result right: no arrangement of size 0 except for empty subtree

    # Write the answer: sum over all arrangements for the full tree, modulo MOD
    write("%d\n" % (sum(dfs(r)) % MOD))

solve()