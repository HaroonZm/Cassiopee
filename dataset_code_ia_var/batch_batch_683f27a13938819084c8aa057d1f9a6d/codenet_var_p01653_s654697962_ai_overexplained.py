from heapq import heappush, heappop  # Importing heap functions for priority queue
import sys  # Importing sys module to use standard input and output streams

# Assigning standard input read and output write functions for faster I/O
readline = sys.stdin.readline  # Function to read a line from standard input
write = sys.stdout.write      # Function to write to standard output

def solve():
    # Read a line from input, split it by spaces and convert values to integers.
    N, M, S1, S2, T = map(int, readline().split())
    # If the number of nodes is 0, exit (no graph to process)
    if N == 0:
        return False  # Used to break the while loop at the end

    # Convert node indices from 1-based to 0-based for internal indexing.
    S1 -= 1  # Start node 1
    S2 -= 1  # Start node 2
    T -= 1   # Target node

    # Create adjacency lists for the graph
    # G: for normal edges (with integer weights)
    # Gx: for 'free' edges (edges with special property 'x' as weight)
    G = [[] for i in range(N)]   # List of adjacency lists for normal weighted edges
    Gx = [[] for i in range(N)]  # List of adjacency lists for 'x' edges
    L = 0  # Counter for the number of 'x' edges in the graph

    # Read M edges from input
    for i in range(M):
        a, b, w = readline().strip().split()  # Each edge: 2 nodes and a weight or 'x'
        a = int(a) - 1  # 0-based from input
        b = int(b) - 1  # 0-based from input
        if w == 'x':
            # If the edge is marked with 'x', add to the Gx adjacency list for both nodes
            Gx[a].append(b)
            Gx[b].append(a)
            L += 1  # Increment the count of 'x' edges
        else:
            # Else, treat as normal edge with integer weight
            w = int(w)
            G[a].append((b, w))  # Add neighbor and weight as tuple
            G[b].append((a, w))

    # Define an infinite value for initialization (a large number)
    INF = 10**18

    # Distance table:
    # dist[k][v] is the shortest distance to node v using exactly k 'x' edges
    dist = [[INF] * N for i in range(L+1)]

    # Priority queue for Dijkstra's algorithm: elements are (cost, node, num_x_edges_used)
    que = [(0, T, 0)]  # Start from the target node, cost 0, using 0 'x' edges

    # Main Dijkstra's loop
    while que:
        cost, v, k = heappop(que)  # Pop the element with the smallest cost

        # If already found a shorter path to this (v, k), skip
        if dist[k][v] < cost:
            continue

        dk0 = dist[k]  # Shorter name for current distances with k 'x' edges

        # Explore all normal edges from current node
        for w, d in G[v]:  # For each neighbor w via a normal edge of weight d
            if cost + d < dk0[w]:  # Check if found better path to w
                dk0[w] = cost + d  # Update distance
                heappush(que, (cost + d, w, k))  # Push new state into priority queue

        # If we can use another 'x' edge (i.e., k+1 does not exceed L)
        if k+1 <= L:
            dk1 = dist[k+1]  # Distance array when using one more 'x' edge
            for w in Gx[v]:  # For each neighbor w via an 'x' edge
                if cost < dk1[w]:  # 'x' edges have zero cost (treated as special)
                    dk1[w] = cost  # Update distance with same cost
                    heappush(que, (cost, w, k+1))  # Push state with one more 'x' edge used

    # Helper function: checks if three points (f1, f2, f3) are non-convex for envelope method
    def check(f1, f2, f3):
        return (f2[0] - f1[0]) * (f3[1] - f2[1]) >= (f2[1] - f1[1]) * (f3[0] - f2[0])

    # Linear function: for a given pair f1 = (a, b) and x, compute a*x + b
    def f(f1, x):
        return f1[0]*x + f1[1]

    que1 = []  # Envelope for S1
    que2 = []  # Envelope for S2

    # Build convex hulls by traversing number of 'x' edges decreasing (from L to 0)
    for a in range(L, -1, -1):  # For each possible number of used 'x' edges (from L down to 0)
        if dist[a][S1] != INF:
            f1 = (a, dist[a][S1])  # f1 = (slope, intercept) for S1
            # Maintain the upper/lower envelope for linear optimization, remove non-optimal
            while len(que1) >= 2 and check(que1[-2], que1[-1], f1):
                que1.pop()
            que1.append(f1)

        if dist[a][S2] != INF:
            f2 = (a, dist[a][S2])  # f2 = (slope, intercept) for S2
            while len(que2) >= 2 and check(que2[-2], que2[-1], f2):
                que2.pop()
            que2.append(f2)

    m1 = len(que1)  # Count of elements in que1 (functions for S1)
    m2 = len(que2)  # Count of elements in que2 (functions for S2)
    ans = 10**18    # Initialize the answer with an infinitely large number (to be minimized)

    # Double for-loop to process every combination of envelope segments
    for i in range(m1):
        # For convex function que1[i]
        px0 = 0  # Left limit of x (integer variable for number of 'x' edges)
        px1 = 10**18  # Right limit, arbitrarily large for upper bound
        ai, bi = que1[i]  # ai: slope, bi: intercept

        # Determine left bound px0 by intersection with previous segment (if exists)
        if i > 0:
            ci, di = que1[i-1]
            # The intersection point (rounded up) between lines i and i-1
            px0 = max((bi - di + ci - ai - 1) // (ci - ai), 0)
        # Determine right bound px1 by intersection with next segment (if exists)
        if i < m1 - 1:
            ci, di = que1[i+1]
            px1 = (di - bi) // (ai - ci)

        for j in range(m2):
            # Repeat similar steps for each segment of S2's envelope
            qx0 = 0  # Left limit
            qx1 = 10**18  # Right limit
            aj, bj = que2[j]

            if j > 0:
                cj, dj = que2[j-1]
                qx0 = max((bj - dj + cj - aj - 1) // (cj - aj), 0)
            if j < m2 - 1:
                cj, dj = que2[j+1]
                qx1 = (dj - bj) // (aj - cj)

            # Now find overlap interval [x0, x1]
            x0 = max(px0, qx0)
            x1 = min(px1, qx1)
            if not x0 <= x1:
                continue  # If intervals do not overlap, skip

            # minimized absolute difference of evaluations at end points of this interval
            ans = min(ans, abs((ai - aj) * x0 + (bi - bj)), abs((ai - aj) * x1 + (bi - bj)))

            # Try for value where the difference is zero (if within interval)
            if ai != aj:
                # Solve (ai - aj)*x + (bi - bj) = 0 -> x = (bj - bi) // (ai - aj)
                x = (bj - bi) // (ai - aj)
                if x0 <= x <= x1:
                    ans = min(ans, abs((ai - aj) * x + (bi - bj)))
                if x0 <= x+1 <= x1:
                    ans = min(ans, abs((ai - aj) * (x + 1) + (bi - bj)))

    # Write the minimal answer found to standard output
    write("%d\n" % ans)
    return True  # Continue the while loop

# Repeatedly call solve() for each test case
while solve():
    ...  # Loop continues until solve() returns False (i.e., blank input or N == 0)