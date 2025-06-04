from heapq import heappop as pop
from heapq import heappush as push

def solve():
    """
    Reads a graph and computes the maximum of the floor division by 2 (with rounding up) 
    of the sum of shortest-path distances between endpoints of each edge plus the edge's cost.
    
    Input:
        N M K
        M lines: s t c (1-based node indices and edge cost)
        K lines: starting node indices (1-based)
    
    Output:
        The maximum value as described above.
    """
    INF = 10 ** 18  # Represents infinity for initial distances

    class Edge:
        """
        Represents an edge in the graph.

        Attributes:
            to (int): The target vertex index.
            cost (int): The cost or weight of the edge.
        """
        def __init__(self, to, cost):
            self.to = to
            self.cost = cost

    # Read input values for the number of vertices (N), edges (M), and starting nodes (K)
    N, M, K = map(int, input().split())

    # Initialize the adjacency list for the graph.
    # G[i]: list of Edge objects representing edges from vertex i
    G = [[] for _ in range(N)]

    # Distance array: d[i] gives shortest distance from any starting node to node i
    d = [INF for _ in range(N)]

    def dijkstra(starts):
        """
        Computes shortest distances from any of the given starting nodes to all other nodes 
        using Dijkstra's algorithm.

        Args:
            starts (list of int): List of starting node indices (0-based).
        Modifies:
            d (list): Updates global variable with shortest distances from starts.
        """
        que = []
        # Initialize distances for start nodes and add them to the priority queue
        for s in starts:
            d[s] = 0
            push(que, (0, s))  # (distance, node)

        while que:
            dist_u, u = pop(que)
            # If we have already found a shorter path, skip this node
            if d[u] < dist_u:
                continue
            # Explore all neighbors of u
            for edge in G[u]:
                v = edge.to
                cost_uv = edge.cost
                if d[v] > d[u] + cost_uv:
                    # Update distance if a shorter path is found
                    d[v] = d[u] + cost_uv
                    push(que, (d[v], v))

    # Read the M edges and build the graph (undirected)
    for _ in range(M):
        s, t, c = map(int, input().split())
        s -= 1  # Convert to 0-based index
        t -= 1
        G[s].append(Edge(t, c))
        G[t].append(Edge(s, c))

    # Read the K starting points and convert to 0-based indices
    lst = [int(input()) - 1 for _ in range(K)]

    # Run Dijkstra's algorithm from all starting nodes
    dijkstra(lst)

    # Compute the required value for each edge and store in 'answers'
    answers = []
    # For each node, and its adjacent edges
    for i in range(N):
        for edge in G[i]:
            # x is the sum of shortest path to i and to edge.to, plus the edge's cost
            x = d[i] + d[edge.to] + edge.cost
            # We want ceil(x / 2) for input (output) as per the original code
            # If x is odd, add 1 before division to simulate ceiling
            if x % 2:
                answers.append(x // 2 + 1)
            else:
                answers.append(x // 2)

    # Output the maximum found value
    print(max(answers))

solve()