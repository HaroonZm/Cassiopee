import sys
import heapq
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M, X = map(int, input().split())
H = [int(input()) for _ in range(N)]

graph = [[] for _ in range(N)]
for _ in range(M):
    A, B, T = map(int, input().split())
    graph[A-1].append((B-1, T))
    graph[B-1].append((A-1, T))

# dist[node] = minimal time to reach node at its top (height H[node])
# but we can be at any height between 0 and H[node]
# So we consider time to move vertically to the top each time before flying away or at the end.
# Approach:
# We'll use Dijkstra with states (node, height)
# But height range is too large, so we use an idea:
# For each node, keep minimal time to reach any height,
# because moving up/down costs 1 s per meter, we can always adjust height after arrival.

# Instead, we store dist[node] = minimal time to reach node at some height, but we record it as the minimal time at top height
# when arriving at node at arbitrary height h, we can always pay (H[node] - h) seconds to climb to top.

# We will consider states only at the top of each tree to simplify.
# From starting point: node 0 at height X, time is X (to climb from 0 to X)

# But initial position is (0, X)
# We can consider the initial time as X (to climb from 0 to X)
# Then from there, for each edge (u,v,t), JOI can fly only if:
# current height h_u satisfies h_u - t >= 0 and h_u - t <= H[v]
# Since we only consider states at top of tree u (height H[u]), we can try to adjust height by going up/down before flying.
# So at node u, if we want to fly to v which costs time t:
# We need height h_u so that:
# h_u - t >= 0
# h_u - t <= H[v]
# So h_u >= t and h_u <= H[v] + t

# Since h_u <= H[u], h_u is in [0,H[u]]
# So feasible h_u must satisfy:
# max(t,0) <= h_u <= min(H[u], H[v] + t)

# To fly, JOI must climb or descend from top H[u] to h_u, then fly, then arrive at height h_u - t in v,
# then after arrival, need to climb from that height to top H[v].

# Total cost to go from node u to node v with current cost dist[u]:
# climb/descend time on u side: abs(H[u]-h_u)
# fly time: t
# climb time on v side: H[v] - (h_u - t) = H[v] - h_u + t
# total = abs(H[u] - h_u) + t + H[v] - h_u + t
#       = abs(H[u] - h_u) + H[v] - h_u + 2t

# We want to minimize total time over h_u in feasible range.

# Try candidates h_u:
# - h_u = t (lowest possible)
# - h_u = H[v] + t (highest possible, capped by H[u])
# - or h_u = H[u] (start from top)

# We'll try h_u = max(t,0), h_u = min(H[u], H[v] + t), and h_u = H[u]

# We'll pick the minimal among them.

INF = 1 << 60
dist = [INF] * N
dist[0] = X  # initial: climb from 0 to X on tree 1, time X

hq = []
heapq.heappush(hq, (X, 0))

while hq:
    cur_time, u = heapq.heappop(hq)
    if dist[u] < cur_time:
        continue
    if u == N-1:
        # we want to be at top of tree N, dist[u] already includes cost to climb to top
        break
    for v, t in graph[u]:
        # feasible h_u range
        low = t
        high = H[v] + t
        high = min(high, H[u])
        low = max(low, 0)
        if low > high:
            continue  # no feasible h_u

        candidates = []
        # candidate 1: low
        candidates.append(low)
        # candidate 2: high
        candidates.append(high)
        # candidate 3: H[u]
        candidates.append(H[u])

        min_cost = INF
        chosen_h = None
        for h_u in candidates:
            if h_u < low or h_u > high:
                continue
            cost = cur_time + abs(H[u] - h_u) + t + (H[v] - (h_u - t)) + t
            # cost explained:
            # - abs(H[u] - h_u): climb/descend on u before flying
            # - t: flying time
            # - H[v] - (h_u - t): climb on v after flying
            # - t: flying time counted again? Wait, flying time t is once only, remove second t
            # Actually, flying time counted twice in above.
            # Correct formula is: abs(H[u] - h_u) + t + (H[v] - (h_u - t))
            cost = cur_time + abs(H[u] - h_u) + t + (H[v] - (h_u - t))
            if cost < min_cost:
                min_cost = cost
                chosen_h = h_u
        if min_cost < dist[v]:
            dist[v] = min_cost
            heapq.heappush(hq, (min_cost, v))

if dist[N-1] == INF:
    print(-1)
else:
    print(dist[N-1])