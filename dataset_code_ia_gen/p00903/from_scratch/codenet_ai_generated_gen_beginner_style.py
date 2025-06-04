import sys
import heapq

def dijkstra(n, adj, fees, start, end):
    # distance: dict mapping (town, visited_set) to cost
    # Since visa fees are paid only once, we track which towns have been visited to avoid double counting fees
    # To keep it simple for beginner, we will track visited town with a boolean list compressed into bitmask,
    # but since n <= 50, using a set (or frozenset) of visited is better for readability but less efficient.
    # Here we do a simpler approach without visited sets because visiting same town again doesn't add fees if visited already.
    # To simplify, we will store only minimal cost to reach each town with a visited set of towns fees paid. But that can be complex.
    # So instead we do a simpler approach: for each town, store minimal cost, and assume paying fees the first time.
    # But this can lead to problem with multiple visits and fees. For beginner, do the following:
    # We'll use a visited fees set represented by a bitmask (up to 50 towns).
    # If too complex, then just use normal dijkstra paying fees once per town visited the first time (as we reach it with better cost).
    INF = 10**9
    dist = {}
    # Start with town start, visited includes start (to avoid paying fee)
    start_visited = 1 << (start - 1)
    hq = []
    heapq.heappush(hq, (0, start, start_visited))
    dist[(start, start_visited)] = 0

    while hq:
        cost, u, visited = heapq.heappop(hq)
        if u == end:
            return cost
        if dist.get((u, visited), INF) < cost:
            continue
        for v, c in adj[u]:
            paid = visited & (1 << (v -1))
            fee = 0 if paid else fees[v]
            ncost = cost + c + fee
            nvisited = visited | (1 << (v -1))
            if dist.get((v, nvisited), INF) > ncost:
                dist[(v, nvisited)] = ncost
                heapq.heappush(hq, (ncost, v, nvisited))
    return -1

def main():
    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        n,m = map(int,line.split())
        if n == 0 and m == 0:
            break
        fees = [0]*(n+1)
        alt = [0]*(n+1)
        # Read fees and altitudes for towns 2..n-1, towns 1 and n have 0 fee and alt 0 and 1000
        for i in range(2,n):
            d,e = map(int,input().split())
            fees[i] = d
            alt[i] = e
        fees[1] = 0
        fees[n] = 0
        alt[1] = 0
        alt[n] = 1000
        edges = []
        for _ in range(m):
            a,b,c = map(int,input().split())
            edges.append((a,b,c))
        # Build adjacency for go phase: only edges where alt[a] <= alt[b]
        adj_go = [[] for _ in range(n+1)]
        for a,b,c in edges:
            if alt[a] <= alt[b]:
                adj_go[a].append((b,c))
        # Build adjacency for return phase: only edges where alt[a] >= alt[b]
        adj_ret = [[] for _ in range(n+1)]
        for a,b,c in edges:
            if alt[a] >= alt[b]:
                adj_ret[a].append((b,c))
        cost_go = dijkstra(n, adj_go, fees, 1, n)
        cost_ret = dijkstra(n, adj_ret, fees, n, 1)
        if cost_go == -1 or cost_ret == -1:
            print(-1)
        else:
            # Town 1 and n have no fees, and fees counted on both phases.
            # But fees paid second time are not added because of visited tracking.
            # But towns on go and return phase may overlap, so second visit fees not added on return phase.
            # So total cost is sum of phases minimal costs as computed.
            print(cost_go + cost_ret)

if __name__ == "__main__":
    main()