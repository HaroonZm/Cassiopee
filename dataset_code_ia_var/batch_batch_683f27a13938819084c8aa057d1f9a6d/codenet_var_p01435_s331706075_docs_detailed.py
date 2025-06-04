from heapq import heappush, heappop
import sys

# Shortcut for fast input
readline = sys.stdin.readline
# Shortcut for fast output
write = sys.stdout.write

def solve():
    """
    Resolves the shortest time/steps to reach a target node in a dependency graph where:
    - Each node may be initially 'active' or 'inactive' (W).
    - Edges represent activation dependencies with associated conditions.
    - Some nodes are activated via initial means, others via triggers from dependencies.
    - Reports the minimal number of steps required to reach a target (T), or -1 if impossible.
    """
    # Read basic problem parameters: N (nodes), E (edges), T (target node)
    N, E, T = map(int, readline().split())
    # Read the activation state of nodes. W[i]=1 means node i+1 is initially active.
    W = list(map(int, readline().split()))
    # G: Outgoing adjacency list (not used but reserved for future logic/clarity)
    G = [[] for _ in range(N)]
    # R: Reverse dependencies; for each node, the list of edge indices that depend on it
    R = [[] for _ in range(N)]
    # C: Number of dependencies remaining to activate for each edge
    C = [0] * E
    # Q: For each edge, stores a tuple (target node, source dependencies)
    Q = [None] * E

    # Read E edges, store their information, and fill in reverse dependencies
    for i in range(E):
        # Each line: g c s1 s2 ... sk
        # g: target node, c: number of sources, s: list of source nodes
        input_line = list(map(int, readline().split()))
        g, c, *s = input_line
        # For each source node, note that edge i depends on activation of s_j
        for e in s:
            R[e - 1].append(i)
        # Number of required activated source nodes to trigger this edge
        C[i] = c
        # Record edge info (target node, source nodes)
        Q[i] = (g, s)

    # Initialize a priority queue for processing activations ('cost', edge_index)
    que = []
    # Constant representing infinity for initialization
    INF = 10 ** 9

    def calc(s):
        """
        Computes the activation cost for a dependency:
        When all required nodes in s are activated, activation of dependent node/edge
        takes max(i + dp[s_i]) over all dependency indices 'i' and their activation costs.

        Args:
            s (list): List of source node indices (1-based).

        Returns:
            int: Computed activation cost.
        """
        # Sort dependencies by their activation times (high to low)
        s.sort(key=lambda x: dp[x - 1], reverse=True)
        r = 0
        # Compute the maximum time taken across all dependencies
        for i, j in enumerate(s):
            r = max(r, i + dp[j - 1])
        return r

    # dp[i]: Minimal number of steps to activate node i+1
    dp = [INF] * N
    # Initialize dp[i]=1 (step 1) if node is active from the start
    for i in range(N):
        if W[i]:
            dp[i] = 1
            # For each edge that depends on this node,
            # decrease its count of remaining unactivated dependencies
            for j in R[i]:
                C[j] -= 1
                # If all dependencies for the edge are resolved, add to processing queue
                if C[j] == 0:
                    g0, s0 = Q[j]
                    heappush(que, (calc(s0), j))

    # Process activation queue
    while que:
        cost, e = heappop(que)
        # Retrieve target node g for this edge and its dependencies s
        g, s = Q[e]
        # If this edge does not improve the cost for activating node g, skip it
        if dp[g - 1] < cost:
            continue
        # If a better activation cost is found, update and process downstream dependencies
        if cost < dp[g - 1]:
            dp[g - 1] = cost
            for j in R[g - 1]:
                C[j] -= 1
                # If dependencies are resolved, push next edge to the queue
                if C[j] <= 0:
                    g0, s0 = Q[j]
                    heappush(que, (calc(s0), j))

    # Final result: If impossible (cost is still INF), output -1.
    # Otherwise output minimal activation cost to reach target node T.
    if dp[T - 1] != INF:
        write("%d\n" % dp[T - 1])
    else:
        write("-1\n")

# Start the solver
solve()