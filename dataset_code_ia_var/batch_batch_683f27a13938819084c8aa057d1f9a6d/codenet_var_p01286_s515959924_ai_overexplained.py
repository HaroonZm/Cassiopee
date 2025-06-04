import collections  # Import the 'collections' module which provides alternatives to built-in types, such as deque, which we use for BFS queue

class MaxFlow:
    """
    Dinic Algorithm for finding the maximum flow in a flow network.

    Complexity: O(EV^2), where E is the number of edges, and V is the number of vertices.
    Used for the AOJ problem GRL6A and alike.
    """

    class Edge:
        """Class representing an edge in the graph used for the flow network."""

        def __init__(self, to, cap, rev):
            # 'to' is an integer representing the destination (target) vertex this edge points to
            # 'cap' is the capacity of the edge (how much flow it can carry; initially, the available space on the edge)
            # 'rev' is the index of the reverse edge in the adjacency list of the 'to' vertex for easy updates
            self.to = to
            self.cap = cap
            self.rev = rev

    def __init__(self, V):
        """
        Initialize a MaxFlow instance.

        Args:
            V: Number of vertices in the graph (an integer). Vertices will be labeled from 0 to V-1.

        Attributes:
            self.V (int): Stores the number of vertices.
            self.E (list): Adjacency list storing edges for each vertex (list of lists of Edge objects).
        """
        self.V = V
        # For each of the V vertices, create an empty list in self.E to later hold the edges coming out of that vertex
        self.E = [[] for _ in range(V)]

    def add_edge(self, fr, to, cap):
        """
        Add an edge (and its residual reverse edge) between two vertices.

        Args:
            fr (int): The starting vertex of the edge.
            to (int): The destination (ending) vertex of the edge.
            cap (int): The capacity for the forward edge.

        For each forward edge, we also add a backward (reverse) edge initially with zero capacity.
        The reverse edge is essential for adjusting (subtracting) the flow when pushing it back.
        """
        # Add forward edge from 'fr' to 'to' with the given capacity
        self.E[fr].append(self.Edge(to, cap, len(self.E[to])))
        # Add backward edge from 'to' to 'fr' with zero capacity.
        # The 'rev' fields point to the indices of forward/reverse pair for easy access when updating capacities
        self.E[to].append(self.Edge(fr, 0, len(self.E[fr]) - 1))

    def run(self, source, sink, INF=10**9):
        """
        Find the maximum flow from 'source' to 'sink' using Dinic's algorithm.

        Args:
            source (int): Index of source vertex.
            sink (int): Index of the sink vertex.
            INF (int): Large number representing 'infinity' for practical purposes (maximum augmenting flow).

        Returns:
            maxflow (int): The value of the maximum flow found from source to sink.
        """
        maxflow = 0  # Start with zero flow
        while True:
            self.bfs(source)  # Do BFS to construct level graph (assigns levels to reachable nodes)
            if self.level[sink] < 0:
                # If sink can't be reached in the level graph, no more augmenting path exists
                return maxflow  # Terminate algorithm and return the computed max flow
            # 'itr' keeps track of which edges have already been explored with the DFS for each vertex
            self.itr = [0] * self.V
            while True:
                flow = self.dfs(source, sink, INF)  # Use DFS to search for blocking flow/path and send min(INF, min residual cap on the path)
                if flow > 0:
                    maxflow += flow  # Add the augmented flow to the total maxflow
                else:
                    # If no augmenting path was found in the level graph, break loop and restart after rebuild graph
                    break

    def dfs(self, vertex, sink, flow):
        """
        Recursively search for an augmenting path using depth-first search.

        Args:
            vertex (int): The current vertex during DFS.
            sink (int): The vertex we want the flow to reach.
            flow (int): The value of flow we can send along this path (the bottleneck so far).

        Returns:
            (int): Amount of flow sent from 'vertex' to 'sink'.
            If no flow can be sent along this path, returns 0.
        """
        if vertex == sink:
            # If we've reached the sink, return the flow (may be less than the original if bottlenecked on the path)
            return flow
        # Iterate over the edges from this vertex, starting from where we last left off
        for i in range(self.itr[vertex], len(self.E[vertex])):
            # Store the index we are currently working on; so that each call resumes at the correct spot for this vertex
            self.itr[vertex] = i
            e = self.E[vertex][i]  # Take the i-th edge from vertex
            # Check if there is room for pushing flow (cap > 0) and the next node is at the next level (for blocking flow)
            if e.cap > 0 and self.level[vertex] < self.level[e.to]:
                # Recursively continue DFS, looking for paths to sink, with flow being bottlenecked by this edge's capacity
                d = self.dfs(e.to, sink, min(flow, e.cap))
                if d > 0:
                    # If positive flow can be pushed through, decrease available cap of this edge
                    e.cap -= d
                    # Increase the cap of the reverse edge, as flow can be sent backward in residual graph if required later
                    self.E[e.to][e.rev].cap += d
                    return d  # Return the flow sent
        return 0  # No augmenting path found from this vertex; return 0

    def bfs(self, start):
        """
        Assign levels to each vertex by performing BFS starting from 'start'.

        Args:
            start (int): The starting vertex (usually the source).

        Returns:
            None, but updates self.level so that self.level[v] is the level of vertex v in the layered graph,
            or -1 if unreachable.
        """
        que = collections.deque()  # Create an empty deque for queue
        # Initially, set all vertices' levels to -1, meaning not yet visited/reachable
        self.level = [-1] * self.V
        que.append(start)  # Add starting vertex to the queue
        self.level[start] = 0  # The start vertex has level 0

        while que:  # While the queue is not empty
            fr = que.popleft()  # Dequeue the first vertex
            for e in self.E[fr]:
                # If the edge has available capacity and its destination hasn't been visited yet (level < 0)
                if e.cap > 0 and self.level[e.to] < 0:
                    self.level[e.to] = self.level[fr] + 1  # Set level to one higher than current
                    que.append(e.to)  # Add this vertex to the queue to continue BFS

while True:
    # Read space-separated integers for each test case:
    # H = number of people, W = number of workshops, C = number of courses,
    # M = number of meals, NW = cap for workshops, NC = cap for courses, NM = cap for meals
    H, W, C, M, NW, NC, NM = map(int, input().split())
    # If H == -1, this implies the end of input (problem convention)
    if H == -1:
        break

    # Calculate number of vertices (V): each group gets its own regions in the graph as per problem transformation
    V = H + 2 * (W + C) + M + 5 + 2  # The formula is specific for this graph construction
    mf = MaxFlow(V)  # Create a MaxFlow instance for this graph with V vertices
    # The last two vertices are set as source and sink for the flow problem
    source, sink = V - 2, V - 1

    # Below are functions to compute the vertex indices in the graph for the different entities (people, workshops, etc.)
    inH = lambda i: i  # Vertex index for person i (0-based)
    inW = lambda i: H + i  # Index for "input" node of workshop i
    outW = lambda i: H + W + i  # Index for "output" node of workshop i (splitting for capacity limiting)
    inC = lambda i: H + 2 * W + i  # "Input" node of course i
    outC = lambda i: H + 2 * W + C + i  # "Output" node of course i (again, splitting for capacity limiting)
    inM = lambda i: H + 2 * (W + C) + i  # Input node for meal i
    inNW = H + 2 * (W + C) + M  # Node representing the "extra" workshop capacity
    outNW = inNW + 1  # "Output" node of Extra Workshop
    inNC = outNW + 1  # Node representing the "extra" course capacity
    outNC = inNC + 1  # "Output" node of Extra Course
    inNM = outNC + 1  # "Input" node for extra meals

    # Add edges from the source node to each person (one per person)
    for i in range(H):
        mf.add_edge(source, inH(i), 1)  # Capacity 1, since each person can participate once

    # For each workshop, read the people who wish to attend and add edges accordingly
    for i in range(W):
        friends = [int(x) - 1 for x in input().split()][1:]  # First input is number, then 1-based indices
        for friend in friends:
            mf.add_edge(inH(friend), inW(i), 1)  # Edge from this person to this workshop, capacity 1

    # Each person can alternatively use the extra workshop capacity (represented as another node)
    for i in range(H):
        mf.add_edge(inH(i), inNW, 1)  # Edge from person i to extra workshop inNW

    # For each workshop, split into in/out with capacity 1 to limit assignment to one person per workshop
    for i in range(W):
        mf.add_edge(inW(i), outW(i), 1)  # Only one can proceed through this in/out split
    mf.add_edge(inNW, outNW, NW)  # Edge for extra workshop node with capacity NW (workshop limit)

    # For each course, read which workshops lead to this course, and add edges accordingly
    for i in range(C):
        friends = [int(x) - 1 for x in input().split()][1:]  # Workshops are 1-based indices
        for friend in friends:
            mf.add_edge(outW(friend), inC(i), 1)  # Edge from workshop's 'out' to course's 'in'
        mf.add_edge(outNW, inC(i), 1)  # The extra workshop output can also lead to the course

    # The output of each workshop (outW) can also go to the node representing extra course capacity (inNC)
    for i in range(W):
        mf.add_edge(outW(i), inNC, 1)
    # Edge from extra workshop output to the extra course input, with capacity NC
    mf.add_edge(inNC, outNC, NC)

    # For each course, split into in/out for capacity limitation
    for i in range(C):
        mf.add_edge(inC(i), outC(i), 1)
    mf.add_edge(inNC, outNC, NC)  # Already added above, kept for clarity

    # For each meal, read the courses needed and add corresponding edges
    for i in range(M):
        friends = [int(x) - 1 for x in input().split()][1:]  # Courses are 1-based
        for friend in friends:
            mf.add_edge(outC(friend), inM(i), 1)  # From the output node of a course to meal input
        mf.add_edge(outNC, inM(i), 1)  # The extra course output can reach the meal too

    # Output of each course can also lead to the extra meal node
    for i in range(C):
        mf.add_edge(outC(i), inNM, 1)

    # From each meal's node to the sink node
    for i in range(M):
        mf.add_edge(inM(i), sink, 1)  # Each meal can be assigned to one only
    mf.add_edge(inNM, sink, NM)  # Extra meal node to the sink, NM is the capacity

    # After network is constructed for this test case, calculate and print the maximal flow value from source to sink
    print(mf.run(source, sink))  # This will invoke Dinic's method for this graph