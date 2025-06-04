import sys
import heapq

def main():
    input = sys.stdin.readline
    while True:
        N, M, H, K = map(int, input().split())
        if N == 0 and M == 0 and H == 0 and K == 0:
            break

        graph = [[] for _ in range(N + 1)]
        for _ in range(M):
            a, b, c, h_, r = map(int, input().split())
            graph[a].append((b, c, h_, r))
            graph[b].append((a, c, h_, r))

        S, T = map(int, input().split())
        P = int(input())
        passports = []
        for _ in range(P):
            tmp = list(map(int, input().split()))
            l = tmp[0]
            d = tmp[1]
            companies = tmp[2:]
            bitmask = 0
            for comp in companies:
                bitmask |= 1 << (comp - 1)
            passports.append((bitmask, d))

        # Precompute minimal cost to cover any set of companies with passports
        INF = 10**9
        max_mask = 1 << K
        dp_cover = [INF] * max_mask
        dp_cover[0] = 0
        for mask in range(max_mask):
            for bitmask, cost in passports:
                nxt = mask | bitmask
                if dp_cover[mask] + cost < dp_cover[nxt]:
                    dp_cover[nxt] = dp_cover[mask] + cost

        # Dijkstra with state: (cost, time, station, covered_companies)
        # For cost feasibility and pruning, store minimal cost for (station, covered_companies, time)
        # But time is bounded H <= 24, so we can store minimal cost for (station, covered_companies, time)
        # Actually store min cost per (station, covered_companies), for time prune when > H

        dist = [[INF] * max_mask for _ in range(N + 1)]
        dist[S][0] = 0
        hq = [(0, 0, S, 0)]  # total_cost, time, station, covered_mask

        res = INF
        while hq:
            cost, time, v, covered = heapq.heappop(hq)
            if dist[v][covered] < cost:
                continue
            if v == T and time <= H:
                # Add passport cost to cover lines used
                total_cost = cost + dp_cover[covered]
                if total_cost < res:
                    res = total_cost
                continue
            for nv, c, h_, r in graph[v]:
                ntime = time + h_
                if ntime > H:
                    continue
                comp_bit = 1 << (r - 1)
                # If we have a passport covering r, no additional fare needed, else pay fare c
                pay = 0 if (covered & comp_bit) else c
                ncovered = covered
                # Can choose to buy passport to cover this company now? No, we buy passports at start.
                # So just update with current covered mask
                ncost = cost + pay
                if dist[nv][ncovered] > ncost:
                    dist[nv][ncovered] = ncost
                    heapq.heappush(hq, (ncost, ntime, nv, ncovered))
            # Also try buying a new passport to cover more companies here (before the next step)
            # Actually, passport buying only once at start (pays dp_cover at end), no mid-route buy.

            # To consider buying passports, we just compute dp_cover at the end for covered mask, no mid-route updates.

        print(res if res != INF else -1)

if __name__ == "__main__":
    main()