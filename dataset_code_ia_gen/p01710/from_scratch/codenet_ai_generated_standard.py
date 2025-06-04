import sys
import threading

def main():
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.readline

    while True:
        N, M, T = map(int, input().split())
        if N == 0 and M == 0 and T == 0:
            break

        p, t, k = [], [], []
        for _ in range(N):
            pi, ti, ki = map(int, input().split())
            p.append(pi)
            t.append(ti)
            k.append(ki)
        adj = [[] for _ in range(N)]
        for _ in range(M):
            a, b = map(int, input().split())
            adj[a-1].append(b-1)

        # Precompute max points can get by watching ads in one website up to k[i] times within T
        max_watch = [0]*N
        max_k = [min(k[i], T//t[i]) for i in range(N)]
        # For each site i, max point = max n*(p[i]) where n ≤ max_k[i] and n*t[i] ≤ T
        for i in range(N):
            max_watch[i] = p[i]*max_k[i]

        # Because watching ads takes time, and moving costs no time,
        # and we can watch each ad at most k[i] times in total,
        # and we can't watch repeatedly without moving in between,
        # we can model states as (site, time, watch_state) is too big,
        # so we use DP: dp[node][time] = max points up to time at node, with zero or one watch per stay.

        # But given constraints, a full DP over time and nodes is large.
        # We optimize by noting:
        # From any website, we can watch ads 0 to k[i] times,
        # but cannot watch twice without moving.
        # So, if we watch once at a website before leaving, we cannot watch again until we moved away and returned.

        # We define two DP arrays:
        # dp0[node][time]: max points at node at time 'time' without watching ad now
        # dp1[node][time]: max points at node at time 'time' with watching ad now (ad watched once for this stay)
        # Transition:
        # From dp0[u][time], we can:
        #   - watch ad at u once, get p[u], costs t[u], go to dp1[u][time + t[u]]
        #   - move to adjacent v without time cost, go to dp0[v][time]
        # From dp1[u][time], can only move to adjacents (can't watch again at this stay).

        # Also, we must limit number of watches per site to k[i] times total.
        # We'll track watches count per site with a list (since k[i] ≤ 10,000 but time limit T ≤ 10,000, watching ads cost t_i ≥ 1)
        # Maximum watches per node is limited by both k[i] and time limit.

        # We'll store dp as a list of dicts to save memory
        # but to keep code efficient, we keep dp arrays of size N x (T+1)
        dp0 = [-1]*(N*(T+1))
        dp1 = [-1]*(N*(T+1))
        def idx(u, time):
            return u*(T+1)+time
        # Initialize dp0: starting at any node with 0 time no points
        for i in range(N):
            dp0[idx(i,0)] = 0

        ans = 0

        # For each time from 0 to T
        for time in range(T+1):
            for u in range(N):
                i0 = idx(u,time)
                if dp0[i0]>=0:
                    val = dp0[i0]
                    ans = max(ans,val)
                    # try watch ad at u if possible (consider time and k[u])
                    if time + t[u] <= T:
                        i1 = idx(u,time + t[u])
                        # watching one ad at this stay
                        if dp1[i1]<val + p[u]:
                            dp1[i1] = val + p[u]
                            ans = max(ans, dp1[i1])
                    # move to adjacent nodes without time cost
                    for v in adj[u]:
                        iv = idx(v,time)
                        if dp0[iv]<val:
                            dp0[iv] = val
                            ans = max(ans,val)
                if dp1[i0]>=0:
                    val = dp1[i0]
                    ans = max(ans,val)
                    # cannot watch ad again at same stay
                    # move to adjacents, which resets watch capability for u and other nodes
                    for v in adj[u]:
                        iv = idx(v,time)
                        # since moved, watch capability resets, so we come to dp0[v][time]
                        if dp0[iv]<val:
                            dp0[iv] = val
                            ans = max(ans,val)

        # We have no explicit checks for k[i] limit except watching count tracking,
        # but above DP can watch unlimited times, which is incorrect.

        # To fix this, we must add count of watches per node: exploding DP

        # Since T ≤ 10_000 and max k[i] ≤ 10_000, and N ≤ 100, full DP with watch counts impossible.

        # Alternative approach:
        # For each node, precompute all possible watching sequences:
        # watching ads from 0 to k[i] times costs multiples of t[i], points multiples of p[i]
        # For each node, create dp[node][times_watched] = cost, points
        # Then run a shortest path style DP to combine

        # Let's implement BFS + DP with state: (node, watches_count per node) and time used up to T.

        # But impossible as k[i] can be 10,000.

        # New idea: For each node, we can watch ads multiple times in sequence, but have to move away and back to watch again.
        # Since watching ads in one stay only once, multiple watches require multiple visits.

        # So each visit to node, can watch ad at most once.

        # So total maximum watches at node i is min(k[i], number of visits to i)

        # Let's transform graph to an expanded graph where each node has "visited count" dimension up to k[i].

        # But that's too large.

        # So, we relax: only keep track of how many times watched in total per node.
        # For each state: (node, watches_counts array, time, watched_this_stay bool)
        # This is prohibitive.

        # Final approach: Limit watching times to k[i].
        # We do DP with states: (node, watches_counts per node but approximate by ignoring counts per node; rely on checking watching count is not surpassed) - fail.

        # But since all t[i] and p[i], and k[i] are large, we must approximate:

        # Since watching ads cost time, and k[i], watching ads more than k[i] times is impossible.

        # We'll keep a cache: count of how many times ads watched for each node (capped by k[i])
        # Because watching ads only once per stay, we must move away before watching again.

        # So max times watched at node i is min(k[i], number of visits).

        # Since moving no time cost, unlimited moves are possible within time limit.

        # So for any node i, the maximum watches possible is min(k[i], floor(T / t[i])).

        # Then max points achievable by watching ads at i is p[i]*min(k[i], T//t[i]) = max_watch[i] computed early.

        # So ultimate upper bound of points is sum over nodes of max_watch[i].

        # But points must be collected by moving.

        # To get max points under time T, we find the best path(s) and watches under constraints.

        # We'll model DP as 3 dimentions: dp[node][time][watched_last] where watched_last in {0,1} to control watching once per stay.

        # But also to keep track of how many times watched per node, store watched_counts per node compressed as a dictionary of (node,times) is impossible.

        # So finally, because M <= 1000, T <= 10000, N <= 100, we try this:

        from collections import deque

        max_k = [min(k[i], T//t[i]) for i in range(N)]

        # State: (node, time, watched_last), watched_times = dict(node->times watched, max k[i])
        # We'll store watched_times as a tuple of tuples sorted by node, only storing nodes watched >0.

        # Because number of times watching ads can be very large, we only store per node watched count in a dict and
        # represent watched_times as tuple of (node, count) to use as key.

        # Use BFS with pruning.

        # To reduce memory, only store the watched_times per node for nodes watched nonzero.

        from collections import defaultdict

        dp = dict()  # key: (node, time, watched_last, watched_times_key) -> max point
        # At start, no watches, time=0, watched_last=0
        # watched_times_key = empty tuple ()

        from heapq import heappush, heappop

        heap = []
        # Use max-heap by storing negative points
        heappush(heap, (0, 0, 0, 0, ()))  # (-point, time, node, watched_last, watched_times_key)

        dp_key = lambda n,t,w,wt: (n,t,w,wt)

        def inc_watch(wt, node):
            d = dict(wt)
            d[node] = d.get(node,0)+1
            return tuple(sorted(d.items()))

        ans = 0

        visited = dict()

        while heap:
            neg_p, time_, u, watched_last, watched_times_key = heappop(heap)
            pnt = -neg_p
            key = (u, time_, watched_last, watched_times_key)
            if key in visited and visited[key]>=pnt:
                continue
            visited[key] = pnt
            ans = max(ans,pnt)
            # two options: watch ad if watched_last==0 and watched_times[node]<k[node] and time + t[u] <= T 
            watched_count = dict(watched_times_key)
            c = watched_count.get(u, 0)
            if watched_last ==0 and c < k[u] and time_ + t[u] <= T:
                new_wt = inc_watch(watched_times_key, u)
                new_pnt = pnt + p[u]
                new_time = time_ + t[u]
                new_key = (u, new_time, 1, new_wt)
                if new_key not in visited or visited[new_key]<new_pnt:
                    heappush(heap, (-new_pnt, new_time, u,1,new_wt))
            # move to adjacents with watched_last reset to 0 (because we moved)
            for v in adj[u]:
                new_key = (v, time_, 0, watched_times_key)
                if new_key not in visited or visited[new_key]<pnt:
                    heappush(heap, (-pnt, time_, v, 0, watched_times_key))

        print(ans)

threading.Thread(target=main).start()