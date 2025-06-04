from heapq import heappush, heappop
import sys

# Alias for reading from stdin and writing to stdout for fast IO.
readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    """
    Main function to process each test case of the problem.
    Reads the graph input, runs a modified Dijkstra's algorithm with
    up to L special zero-cost edges, then finds the minimum difference
    in shortest path cost to two given nodes over all possible
    special edge utilizations.
    Returns True while there is more input to process, else returns False.
    """
    # Read basic parameters: number of nodes, edges, two start nodes, and target node
    N, M, S1, S2, T = map(int, readline().split())
    if N == 0:
        # Sentinel value for end of input
        return False

    # Adjust node indices to 0-based
    S1 -= 1
    S2 -= 1
    T -= 1

    # Initialize adjacency lists:
    # G - standard weighted edges
    # Gx - special zero-cost edges (labeled 'x')
    G = [[] for _ in range(N)]
    Gx = [[] for _ in range(N)]

    # L counts how many 'x' edges in the input, which limits the number of times we can use such edges
    L = 0

    # Read edges from input
    for _ in range(M):
        a, b, w = readline().strip().split()
        a = int(a) - 1
        b = int(b) - 1
        if w == 'x':
            # This is a special zero-cost edge
            Gx[a].append(b)
            Gx[b].append(a)
            L += 1
        else:
            # Normal weighted edge
            w = int(w)
            G[a].append((b, w))
            G[b].append((a, w))

    # Use a large constant as infinity
    INF = 10 ** 18

    # dist[k][v]: minimum distance to node v using exactly k special 'x' edges 
    dist = [[INF] * N for _ in range(L + 1)]

    # Priority queue for Dijkstra-like search; tuples are (cost, node, x-edges-used)
    # Initially, we start from T, distance 0, using 0 x-edges
    que = [(0, T, 0)]
    dist[0][T] = 0

    # Modified Dijkstra to handle up to L transitions (x-edges used)
    while que:
        cost, v, k = heappop(que)
        if dist[k][v] < cost:
            continue
        dk0 = dist[k]  # dist for the current allowance of used special edges

        # Traverse regular (weighted) edges
        for w, d in G[v]:
            if cost + d < dk0[w]:
                dk0[w] = cost + d
                heappush(que, (cost + d, w, k))

        # Traverse special zero-cost edges, if not used up our allowance
        if k + 1 <= L:
            dk1 = dist[k + 1]
            for w in Gx[v]:
                if cost < dk1[w]:
                    dk1[w] = cost
                    heappush(que, (cost, w, k + 1))

    def check(f1, f2, f3):
        """
        Determines whether to keep or remove a point in the convex hull
        during envelope optimization.

        Args:
            f1, f2, f3: Points represented as (number of x-edges used, distance)
        Returns:
            Boolean indicating if f2 should be removed
        """
        return (f2[0] - f1[0]) * (f3[1] - f2[1]) >= (f2[1] - f1[1]) * (f3[0] - f2[0])

    def f(f1, x):
        """
        Evaluates the linear function corresponding to a point.

        Args:
            f1: Tuple (slope, intercept)
            x: Integer to evaluate the function at
        Returns:
            Integer value of the function at x
        """
        return f1[0] * x + f1[1]

    # Build convex envelopes for S1 and S2
    que1 = []  # Holds (number of x-edges, distance from S1)
    que2 = []  # Holds (number of x-edges, distance from S2)

    # Traverse in decreasing number of special edges used
    for a in range(L, -1, -1):
        if dist[a][S1] != INF:
            f1 = (a, dist[a][S1])
            # Maintain lower envelope
            while len(que1) >= 2 and check(que1[-2], que1[-1], f1):
                que1.pop()
            que1.append(f1)

        if dist[a][S2] != INF:
            f2 = (a, dist[a][S2])
            # Maintain lower envelope
            while len(que2) >= 2 and check(que2[-2], que2[-1], f2):
                que2.pop()
            que2.append(f2)

    m1 = len(que1)
    m2 = len(que2)
    ans = 10 ** 18

    # Cross all valid pairs of (number of x-edges used, cost) for S1 and S2 envelopes
    for i in range(m1):
        # For the function que1[i], determine the valid x range
        px0 = 0
        px1 = 10 ** 18
        ai, bi = que1[i]
        if i > 0:
            ci, di = que1[i - 1]
            # Lower bound for x
            px0 = max((bi - di + ci - ai - 1) // (ci - ai), 0)
        if i < m1 - 1:
            ci, di = que1[i + 1]
            # Upper bound for x
            px1 = (di - bi) // (ai - ci)

        for j in range(m2):
            # For que2[j], determine its valid x range
            qx0 = 0
            qx1 = 10 ** 18
            aj, bj = que2[j]
            if j > 0:
                cj, dj = que2[j - 1]
                qx0 = max((bj - dj + cj - aj - 1) // (cj - aj), 0)
            if j < m2 - 1:
                cj, dj = que2[j + 1]
                qx1 = (dj - bj) // (aj - cj)

            # Take overlap of valid intervals for x (number of x-edges used)
            x0 = max(px0, qx0)
            x1 = min(px1, qx1)
            if not x0 <= x1:
                continue

            # Evaluate absolute difference in costs for valid x ranges
            ans = min(ans, abs((ai - aj) * x0 + (bi - bj)), abs((ai - aj) * x1 + (bi - bj)))
            if ai != aj:
                x = (bj - bi) // (ai - aj)
                if x0 <= x <= x1:
                    ans = min(ans, abs((ai - aj) * x + (bi - bj)))
                if x0 <= x + 1 <= x1:
                    ans = min(ans, abs((ai - aj) * (x + 1) + (bi - bj)))

    # Output the result for this test case
    write("%d\n" % ans)
    return True

# Keep solving test cases until input finishes (N==0)
while solve():
    ...