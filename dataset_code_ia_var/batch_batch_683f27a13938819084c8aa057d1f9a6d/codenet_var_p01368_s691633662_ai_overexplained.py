import sys

# Import the sys module so we can access standard input (stdin) and standard output (stdout).
# sys.stdin: Used for reading input from the user or a file redirected to the program.
# sys.stdout: Used for writing output from the program.

readline = sys.stdin.readline   # Assigns the function 'readline' from sys.stdin to a variable named 'readline'
write = sys.stdout.write       # Assigns the function 'write' from sys.stdout to a variable named 'write'

from collections import deque  # Import deque, a double-ended queue, from the collections module.

# Define the class for the Hopcroft-Karp algorithm, used for finding maximum matching in bipartite graphs.
class HopcroftKarp:
    def __init__(self, N0, N1):
        # This is the constructor of the HopcroftKarp class.
        # N0: Number of nodes on the left side of the bipartite graph.
        # N1: Number of nodes on the right side of the bipartite graph.
        self.N0 = N0  # Store the number of left nodes.
        self.N1 = N1  # Store the number of right nodes.
        self.N = N = 2 + N0 + N1  # Total number of nodes. 0 and 1 are special source/sink nodes.
        self.G = [[] for i in range(N)]  # Adjacency list for the graph, contains edges for each node, initially empty.

        # Initialize the edges between the source node (node 0) and the left partition,
        # and between the right partition and the sink node (node 1).
        for i in range(N0):
            forward = [2 + i, 1, None]   # Edge from source node (0) to left node (2 + i), with capacity 1.
            forward[2] = backward = [0, 0, forward]  # The backward edge from left node to source, with capacity 0.
            self.G[0].append(forward)     # Add the forward edge to the outgoing edges from source.
            self.G[2 + i].append(backward)  # Add the backward edge to the outgoing edges from the left node.

        self.backwards = bs = []  # List to save specific backward edges for later use (right to sink).
        for i in range(N1):
            forward = [1, 1, None]  # Edge from right node (2 + N0 + i) to sink node (1), with capacity 1.
            forward[2] = backward = [2 + N0 + i, 0, forward]  # Reverse edge back from sink to right node, capacity 0.
            bs.append(backward)  # Save reference to the backward edge for matching extraction.
            self.G[2 + N0 + i].append(forward)  # Add forward edge to right node's outgoing edges.
            self.G[1].append(backward)    # Add backward edge to sink's outgoing edges.

    def add_edge(self, fr, to):
        # Adds an edge in the bipartite graph from 'fr' in the left part to 'to' in the right part.
        # fr: An integer, index of the node on the left partition.
        # to: An integer, index of the node on the right partition.
        v0 = 2 + fr           # Node index of the left partition's vertex.
        v1 = 2 + self.N0 + to # Node index of the right partition's vertex.

        # Create the forward edge with capacity 1, from v0 (left node) to v1 (right node).
        forward = [v1, 1, None]   # Edge is [destination, capacity, pointer to reverse edge]
        # Create the backward (reverse) edge with capacity 0.
        forward[2] = backward = [v0, 0, forward]
        self.G[v0].append(forward)      # Add forward edge to edges from left node.
        self.G[v1].append(backward)     # Add backward edge to edges from right node.

    def bfs(self):
        # Breadth-first search to layer the graph (levels) for augmenting path search.
        G = self.G   # The adjacency list representation of the graph.
        level = [None] * self.N  # Marks the 'level' (distance from source) for each node, initially None.
        deq = deque([0])         # Queue for BFS; starts with the source node (node 0).
        level[0] = 0             # The source node has level 0.

        while deq:               # Continue while there are nodes in the queue.
            v = deq.popleft()    # Remove and return the element from the left side of the queue.
            lv = level[v] + 1    # Next level is one more than current.
            for w, cap, _ in G[v]:  # Enumerate the (to, capacity, rev) of each edge outgoing from v.
                if cap and level[w] is None:  # If this edge has available capacity, and w isn't visited yet.
                    level[w] = lv             # Assign the level to this node.
                    deq.append(w)             # Add the node to the queue to expand its neighbors.

        self.level = level                   # Store the level for use in DFS.
        return level[1] is not None          # Return True if sink node (node 1) is reachable (i.e., augmenting paths exist).

    def dfs(self, v, t):
        # Depth-first search to find an augmenting path from node v to t.
        if v == t:     # If current node is the target, we've found a path.
            return 1
        level = self.level   # The 'level' array giving us BFS-levels.

        for e in self.it[v]:      # For each outgoing edge from v. self.it is the current iterators for edges.
            w, cap, rev = e      # w: destination node, cap: remaining capacity, rev: reverse edge
            # If capacity is available, and we're going to a deeper level node (so as to respect levels).
            if cap and level[v] < level[w] and self.dfs(w, t):
                e[1] = 0         # Decrease forward edge capacity (now it's 0, as we're using the edge up).
                rev[1] = 1       # Increase reverse edge capacity to allow flow 'undo'.
                return 1         # Return success upwards (an augmenting path has been found).
        return 0                 # If no path is found, return failure

    def flow(self):
        # Returns the value of the maximum matching (max flow) in the bipartite graph.

        flow = 0                 # Counter for the number of matched pairs (total flow).
        G = self.G               # Adjacency list.
        bfs = self.bfs           # Reference to BFS function.
        dfs = self.dfs           # Reference to DFS function.

        while bfs():             # While there exists an augmenting path (layered graph built).
            *self.it, = map(iter, G)  # Initialize self.it as an array of iterators over each node's edge list.
            while dfs(0, 1):          # As long as an augmenting path can be found from source (0) to sink (1):
                flow += 1             # Each DFS increases the flow by 1.

        return flow                   # The total matching found.

    def matching(self):
        # Returns a list of current capacities of backward edges saved for right side nodes,
        # indicating which right nodes are matched (if capacity is 1 then that node is unmatched).
        return [cap for _, cap, _ in self.backwards]  # List comprehension to extract cap from backward edges.


def solve():
    # Reads a single test case, solves it, and writes the answer.
    N, M, L = map(int, readline().split())  # Read integers N (nodes), M (edges), and L (requests).
    if N == 0:
        return False  # If N==0 indicates end of input, we stop solving more test cases.

    INF = 10 ** 9                      # A large value to represent 'infinity' (for shortest path calculation).
    E = [[INF] * N for i in range(N)]  # Initialize adjacency matrix with INF for all node pairs.

    # Read M edges and set corresponding distances in the adjacency matrix.
    for i in range(M):
        u, v, d = map(int, readline().split())  # For each edge, u, v are node indices, d is the distance.
        E[u][v] = E[v][u] = d                   # Undirected edge: distance is the same both ways.

    for i in range(N):
        E[i][i] = 0      # Distance from a node to itself is zero.

    # Compute the all-pairs shortest path using the Floyd-Warshall algorithm.
    # This updates each E[i][j] to the minimum distance from i to j, possibly via intermediate nodes.
    for k in range(N):
        for i in range(N):
            Ei = E[i]         # Just a fast local variable to not repeat E[i]
            for j in range(N):
                Ei[j] = min(Ei[j], Ei[k] + E[k][j])  # Update the shortest distance if a shortcut through k exists.

    g = HopcroftKarp(L, L)  # Create a bipartite matcher with L left and L right nodes.

    P = [list(map(int, readline().split())) for i in range(L)]  # Read L requests; each request is (start_node, time).
    # P[i][0]: the starting node.
    # P[i][1]: the time at which the request happens.

    P.sort(key=lambda x: x[1])  # Sort the requests by their time, to compute feasible chains.

    for i in range(L):
        pi, ti = P[i]  # pi: start node of request i, ti: time of request i
        for j in range(i + 1, L):  # For every subsequent request in time order...
            pj, tj = P[j]
            # If finishing at pi at time ti, can reach pj before its time tj?
            if ti + E[pi][pj] <= tj:
                g.add_edge(i, j)  # Add an edge in the matching graph between these requests.

    write("%d\n" % (L - g.flow()))  # The minimal number of observers/agents required is L - maximum matching.
    return True  # Return True to indicate we should continue solving more test cases.

# Keep solving until we meet a test case with N == 0.
while solve():
    ...   # Ellipsis is a no-op in Python; used here since the loop body is not needed.