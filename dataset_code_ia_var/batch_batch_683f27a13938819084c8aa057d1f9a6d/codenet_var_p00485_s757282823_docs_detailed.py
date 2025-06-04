from heapq import heappop as pop
from heapq import heappush as push

INF = 10 ** 18  # A large value to represent infinity for initial distances

class edge:
    """Class representing an edge in the graph.

    Attributes:
        to (int): Destination vertex of the edge.
        cost (int): The cost or weight of the edge.
    """
    def __init__(self, to, cost):
        """
        Initializes an edge.

        Args:
            to (int): Target node this edge points to.
            cost (int): Weight/cost associated with this edge.
        """
        self.to = to
        self.cost = cost

# Read number of nodes, number of edges, and number of starting nodes
N, M, K = map(int, input().split())

# Initialize adjacency list; G[i] stores the list of outgoing edges from node i
G = [[] for _ in range(N)]

# Initialize shortest distance array with infinity values
# d[i] represents the shortest known distance from any starting node to vertex i
d = [INF for _ in range(N)]

def dijkstra(lst):
    """Executes Dijkstra's algorithm to find minimum distance to all nodes from any given starting nodes.

    Args:
        lst (list of int): List of starting nodes (indices) for the Dijkstra algorithm.
    Side Effects:
        Updates the global 'd' list with shortest distances from any start node to every node.
    """
    que = []  # Priority queue for Dijkstra; items are (distance, node index) tuples
    for s in lst:
        d[s] = 0      # Distance from a start node to itself is zero
        push(que, (0, s))  # Add start node to queue

    while que:
        p = pop(que)      # Remove node with smallest current distance
        v = p[1]          # The node index
        if d[v] < p[0]:   # Skip if there is already a shorter path found
            continue
        for e in G[v]:    # Check all edges/issues from node v
            if d[e.to] > d[v] + e.cost:                      # If using this edge leads to a shorter path
                d[e.to] = d[v] + e.cost                      # Update shortest path to e.to
                push(que, (d[e.to], e.to))                   # Add the new candidate to the queue

# Read the edge list and populate the graph G as an adjacency list
for _ in range(M):
    s, t, c = map(int, input().split())
    s -= 1  # Adjust for zero-based indexing
    t -= 1
    # Since the graph is undirected, add edges in both directions
    G[s].append(edge(t, c))
    G[t].append(edge(s, c))

# Read the list of K starting node indices (convert to zero-based indices)
lst = [int(input()) - 1 for _ in range(K)]

# Run Dijkstra's algorithm from all starting nodes
dijkstra(lst)

anss = []         # List to collect potential answers

# For every node and its outgoing edges, analyze the sum of distances and edge cost
for i in range(N):
    for e in G[i]:
        x = d[i] + d[e.to] + e.cost  # Calculate the path's "cost" through both ends of each edge
        # Depending on whether sum is odd or even, append the "rounded up" half, which simulates ceil
        if x % 2:
            anss.append(x // 2 + 1)
        else:
            anss.append(x // 2)

# Output the maximum value found in the 'anss' list,
# which represents the answer to the specific problem context
print(max(anss))