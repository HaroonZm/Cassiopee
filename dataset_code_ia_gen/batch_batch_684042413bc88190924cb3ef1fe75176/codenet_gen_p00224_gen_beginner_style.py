import sys
sys.setrecursionlimit(10**7)

def main():
    while True:
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
            if not line:
                return
        m, n, k, d = map(int, line.strip().split())
        if m == 0 and n == 0 and k == 0 and d == 0:
            break
        cake_cal = list(map(int, sys.stdin.readline().strip().split()))
        places = []
        # Map place names to ids
        # H = 0, D = 1
        # C1..Cm: 2..m+1
        # L1..Ln: m+2..m+1+n
        place_id = {}
        place_id['H'] = 0
        place_id['D'] = 1
        for i in range(m):
            place_id['C'+str(i+1)] = 2+i
        for i in range(n):
            place_id['L'+str(i+1)] = 2+m+i
        # graph as adjacency list: each node -> list of (neighbor, distance)
        size = 2 + m + n
        graph = [[] for _ in range(size)]
        for _ in range(d):
            s, t, e = sys.stdin.readline().strip().split()
            e = int(e)
            u = place_id[s]
            v = place_id[t]
            graph[u].append((v,e))
            graph[v].append((u,e))

        # We want to find path from H(0) to D(1), visiting any subset of C places at most once,
        # minimizing total cost = distance * k - sum of cake calories eaten (one per visited C)
        # Visiting C places multiple times not allowed.
        # Can revisit other nodes multiple times.

        # State:
        # current position: 0..size-1
        # visited_cake_mask: bitmask of which cakes visited (among m cakes)
        # We'll do DFS with memoization

        from collections import deque

        INF = 10**9
        dp = [[INF]*(1<<m) for _ in range(size)]
        # dp[pos][mask] = minimal total cost from H to pos with cakes visited as mask

        # initial state: at H(0), visited no cakes, cost 0
        dp[0][0] = 0
        # BFS queue: (pos, visited_mask)
        queue = deque()
        queue.append((0,0))

        while queue:
            pos, mask = queue.popleft()
            cost = dp[pos][mask]
            # if pos == 1 (D) we can update answer but continue to explore to find better
            for (nxt, dist) in graph[pos]:
                # calculate next mask and cost
                new_mask = mask
                add_cost = dist * k
                # if nxt is a cake shop
                if nxt >= 2 and nxt <= 1+m:
                    cake_idx = nxt - 2
                    # if not visited yet
                    if (mask & (1<<cake_idx)) == 0:
                        new_mask = mask | (1 << cake_idx)
                        add_cost -= cake_cal[cake_idx]
                new_cost = cost + add_cost
                if new_cost < dp[nxt][new_mask]:
                    dp[nxt][new_mask] = new_cost
                    queue.append((nxt, new_mask))

        ans = min(dp[1])
        print(ans)

if __name__ == '__main__':
    main()