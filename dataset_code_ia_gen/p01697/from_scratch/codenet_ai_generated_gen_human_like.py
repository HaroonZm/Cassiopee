import sys
import heapq

def main():
    input = sys.stdin.readline
    while True:
        N, M, H, K = map(int, input().split())
        if N == 0 and M == 0 and H == 0 and K == 0:
            break

        edges = [[] for _ in range(N+1)]
        for _ in range(M):
            a, b, c, h, r = map(int, input().split())
            edges[a].append((b, c, h, r))
            edges[b].append((a, c, h, r))

        S, T = map(int, input().split())
        P = int(input())
        passports = []
        for _ in range(P):
            data = list(map(int, input().split()))
            l_j, d_j = data[0], data[1]
            companies = data[2:]
            mask = 0
            for comp in companies:
                mask |= 1 << (comp - 1)
            passports.append((mask, d_j))

        # Precompute all possible combined passport sets and minimal cost
        # Use bitmask from 0 to (1<<K)-1 to represent owned company sets
        INF = 10**15
        min_passport_cost = [INF] * (1 << K)
        min_passport_cost[0] = 0
        for mask in range(1 << K):
            # try adding no new passports
            pass
        for mask in range(1 << K):
            if min_passport_cost[mask] == INF:
                continue
            for pmask, pcost in passports:
                new_mask = mask | pmask
                if min_passport_cost[new_mask] > min_passport_cost[mask] + pcost:
                    min_passport_cost[new_mask] = min_passport_cost[mask] + pcost

        # After this, min_passport_cost[mask] is minimal cost to buy passports covering 'mask' companies

        # Now for each mask, try to find minimum travel cost using that set of passports

        # The travel cost depends on which companies' tariffs are covered by passports.
        # For a given mask, all routes managed by companies in mask cost 0,
        # others cost their fare.

        ans = -1

        # We will run a modified Dijkstra for each mask to find minimal travel cost + passport cost
        # But 1<<K can be up to 256 (K<=8), and N up to 100, so total states = 256*100=25600
        # However this is large but feasible.

        # Since cost of buying passports = min_passport_cost[mask]
        # and traveling cost can be computed via Dijkstra with zero fare on companies in mask

        # Use Dijkstra for each mask:
        for mask in range(1 << K):
            if min_passport_cost[mask] == INF:
                continue
            dist = [INF] * (N+1)
            dist[S] = 0
            # Use heap queue (travel cost, current time, node)
            # But time limit is H hours, travel times are added as edges.
            # We'll model time as distance in minutes? but h_i is hour units?

            # Note h_i is in hours, but maximum H is up to 24, and edges up to 500

            # We'll store (cost accumulated, time accumulated, node)
            # Since cost and time are independent, and we want to minimize cost with time constraint,
            # use a state: (cost_so_far, time_so_far, node)
            # But Dijkstra can't handle two criteria directly. We want minimal cost with time <= H

            # Use dist[node][time] = minimal cost to reach node at exactly time
            # Since H <=24 and h_i>=1, max time steps 24.

            # However time can be H hours max, so discretize time on hours:
            max_time = H
            dist2 = [[INF]*(max_time+1) for _ in range(N+1)]
            dist2[S][0] = 0
            hq = []
            heapq.heappush(hq, (0, 0, S))  # (cost, time, node)

            while hq:
                cost_so_far, time_so_far, node = heapq.heappop(hq)
                if dist2[node][time_so_far] < cost_so_far:
                    continue
                if node == T and time_so_far <= H:
                    # Found a possible route, record the total cost (passport + travel)
                    total_cost = cost_so_far + min_passport_cost[mask]
                    if ans == -1 or ans > total_cost:
                        ans = total_cost
                    # We don't break because maybe better path later.
                    # But since we pop from min-heap, first time we pop T with time <= H is minimal cost for this mask.
                    # So we can break here for efficiency
                    break
                for nxt, c, h, r in edges[node]:
                    new_time = time_so_far + h
                    if new_time > H:
                        continue
                    # Cost for this edge is 0 if company covered in passports, else c
                    company_bit = 1 << (r - 1)
                    cost_edge = 0 if (mask & company_bit) != 0 else c
                    new_cost = cost_so_far + cost_edge
                    if dist2[nxt][new_time] > new_cost:
                        dist2[nxt][new_time] = new_cost
                        heapq.heappush(hq, (new_cost, new_time, nxt))

        print(ans)

if __name__ == "__main__":
    main()