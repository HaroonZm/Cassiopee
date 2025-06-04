import sys
from collections import defaultdict

def input():
    """
    Reads a line from standard input, removing the trailing newline character.
    Returns:
        str: The next line of input, stripped of trailing whitespace.
    """
    return sys.stdin.readline().strip()

def list2d(a, b, c):
    """
    Generates a 2D list of dimensions a x b, with all elements initialized to c.

    Args:
        a (int): Number of rows.
        b (int): Number of columns.
        c: Initial value for each entry.

    Returns:
        list: 2D list.
    """
    return [[c] * b for _ in range(a)]

def list3d(a, b, c, d):
    """
    Generates a 3D list of dimensions a x b x c, with all elements initialized to d.

    Args:
        a (int): First dimension.
        b (int): Second dimension.
        c (int): Third dimension.
        d: Initial value for each entry.

    Returns:
        list: 3D list.
    """
    return [[[d] * c for _ in range(b)] for _ in range(a)]

def list4d(a, b, c, d, e):
    """
    Generates a 4D list of dimensions a x b x c x d, with all elements initialized to e.

    Args:
        a (int): First dimension.
        b (int): Second dimension.
        c (int): Third dimension.
        d (int): Fourth dimension.
        e: Initial value for each entry.

    Returns:
        list: 4D list.
    """
    return [[[[e] * d for _ in range(c)] for _ in range(b)] for _ in range(a)]

def ceil(x, y=1):
    """
    Calculates the ceiling of x divided by y.

    Args:
        x (int): Numerator.
        y (int): Denominator (default 1).

    Returns:
        int: Ceiling value of x / y.
    """
    return int(-(-x // y))

def INT():
    """
    Reads and converts the next input line as an integer.

    Returns:
        int: Integer value from input.
    """
    return int(input())

def MAP():
    """
    Reads a line from input and converts it into a map of integers.

    Returns:
        map: Map object containing input integers.
    """
    return map(int, input().split())

def LIST(N=None):
    """
    Reads a list of integers from input.

    Args:
        N (int, optional): If specified, reads N lines as integers. Otherwise, reads one line split by spaces.

    Returns:
        list: List of integers.
    """
    if N is None:
        return list(MAP())
    else:
        return [INT() for _ in range(N)]

def Yes():
    """
    Prints 'Yes' to standard output.
    """
    print('Yes')

def No():
    """
    Prints 'No' to standard output.
    """
    print('No')

def YES():
    """
    Prints 'YES' to standard output.
    """
    print('YES')

def NO():
    """
    Prints 'NO' to standard output.
    """
    print('NO')

# Increase recursion limit for deep recursions (not needed for this code, precautionary)
sys.setrecursionlimit(10 ** 9)

INF = 10 ** 18  # Large value for infinity representation
MOD = 10 ** 9 + 7  # Large prime, commonly used as modulo in competitive programming

class MinCostFlow:
    """
    Implements a minimum cost flow algorithm using Dijkstra's algorithm with potentials.
    Time complexity: O(F * E * logV), where F is flow, E is number of edges, V is number of vertices.
    """
    INF = 10 ** 18  # Infinity constant for this class

    def __init__(self, N):
        """
        Initializes a flow network.

        Args:
            N (int): Number of nodes in the graph.
        """
        self.N = N
        self.G = [[] for _ in range(N)]  # G[i] stores edges from vertex i

    def add_edge(self, fr, to, cap, cost):
        """
        Adds a directed edge to the flow network.

        Args:
            fr (int): Source node.
            to (int): Target node.
            cap (int): Capacity of edge.
            cost (int): Cost per unit flow for this edge.
        """
        G = self.G
        # Edge format: [target, remaining capacity, cost, index of reverse edge in G[to]]
        G[fr].append([to, cap, cost, len(G[to])])
        # Add a reverse edge in the target node for residual graph traversal
        G[to].append([fr, 0, -cost, len(G[fr]) - 1])

    def flow(self, s, t, f):
        """
        Calculates the minimum cost to send flow f from node s to node t.

        Args:
            s (int): Source node.
            t (int): Sink node.
            f (int): Amount of flow to send.

        Returns:
            int: The minimum cost for the requested flow. If impossible, returns self.INF.
        """
        from heapq import heappush, heappop

        N = self.N
        G = self.G
        INF = MinCostFlow.INF

        res = 0  # Total cost
        H = [0] * N  # Potential (for Dijkstra's)
        prv_v = [0] * N  # Previous vertex in path
        prv_e = [0] * N  # Previous edge index in path

        while f:
            # Dijkstra's algorithm to find cheapest augmenting path
            dist = [INF] * N
            dist[s] = 0
            que = [(0, s)]  # (cost, vertex)

            while que:
                c, v = heappop(que)
                if dist[v] < c:
                    continue
                for i, (to, cap, cost, _) in enumerate(G[v]):
                    if cap > 0 and dist[to] > dist[v] + cost + H[v] - H[to]:
                        # Potential is used to keep edge weights non-negative
                        dist[to] = r = dist[v] + cost + H[v] - H[to]
                        prv_v[to] = v
                        prv_e[to] = i
                        heappush(que, (r, to))
            if dist[t] == INF:
                # No augmenting path found, flow is impossible
                return INF

            # Update potentials
            for i in range(N):
                H[i] += dist[i]

            # Determine the minimal residual capacity along the path
            d = f
            v = t
            while v != s:
                d = min(d, G[prv_v[v]][prv_e[v]][1])
                v = prv_v[v]
            f -= d  # Reduce remaining flow to send by d
            res += d * H[t]  # Add cost for this augmentation

            # Update edge capacities along the path
            v = t
            while v != s:
                e = G[prv_v[v]][prv_e[v]]
                e[1] -= d  # Reduce capacity along the edge
                G[v][e[3]][1] += d  # Increase reverse edge's capacity (residual graph)
                v = prv_v[v]
        return res

# --- Problem-specific code begins here ---

# Read input values: M, N, K
M, N, K = MAP()  # M: number of items to select, N: number of item types, K: number of used items
A = LIST(N)      # A: list of values/profits for item types (size N)
B = [b - 1 for b in LIST(K)]  # B: sequence of used items (0-indexed)

# Remove consecutive duplicates in B, to minimize redundant path states
B2 = [B[0]]
for i in range(1, K):
    if B[i-1] != B[i]:
        B2.append(B[i])
K2 = len(B2)

# For each position, precompute the next occurrence of the same value in B2.
nxt = [INF] * K2  # nxt[i]: the next index in B2 where the same value B2[i] appears again
D = defaultdict(lambda: INF)  # Map from value to its most recent position in B2
total = 0  # Total sum of all item values used

for i in range(K2 - 1, -1, -1):
    b = B2[i]
    nxt[i] = D[b]
    D[b] = i
    total += A[b]  # Sum up values as we traverse

# Instantiate the MinCostFlow graph with K2 nodes
mcf = MinCostFlow(K2)
MAX = 10 ** 4  # Large constant, used for cost adjustment to ensure non-negative costs

# Construct the flow network
for i in range(K2 - 1):
    b = B2[i]
    # If we 'do not keep' this occurrence, profit for that position is 0,
    # but we pass M-1 units of flow along
    mcf.add_edge(i, i + 1, M - 1, MAX)
    j = nxt[i]
    if j != INF:
        # If we 'keep' this occurrence (can use this value for a selection),
        # We gain a profit of A[b] at cost reduction. The capacity is 1 since each unique value can be kept once.
        # The cost is adjusted with MAX*(j - i - 1) - A[b] to keep everything non-negative.
        mcf.add_edge(i + 1, j, 1, MAX * (j - i - 1) - A[b])

# Run the min cost flow to select M-1 paths from 0 to K2-1
# The adjustment terms (MAX multipliers) ensure the costs are non-negative for the flow formulation
res = MAX * (K2 - 1) * (M - 1) - mcf.flow(0, K2 - 1, M - 1)

# Final result: subtract the cost from the total value to get the optimal selection's value gain
print(total - res)