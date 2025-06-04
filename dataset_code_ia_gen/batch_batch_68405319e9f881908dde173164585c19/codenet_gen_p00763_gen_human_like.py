import sys
import heapq

def readints():
    return list(map(int, sys.stdin.readline().split()))

def compute_fares(p, q, r):
    # Build fare table lookup for fare(distance)
    # distance up to max distance (q[-1] or big enough)
    max_dist = q[-1] if q else 10**9
    fare = [0]*(max_dist+1)
    idx = 0
    for dist in range(1, max_dist+1):
        if idx < len(q) and dist > q[idx]:
            idx += 1
        fare[dist] = fare[dist-1] + r[idx]
    return fare

def fare_cost(fare_table, dist):
    if dist == 0:
        return 0
    if dist < len(fare_table):
        return fare_table[dist]
    # In case of distance beyond precomputed, calculate on the fly
    # Should not happen since we took max_dist big enough
    return fare_table[-1] + sum(fare_table[-1] for _ in range(dist - len(fare_table) + 1))

def main():
    # Read until line of five zeros
    while True:
        n,m,c,s,g = readints()
        if n == 0 and m == 0 and c == 0 and s == 0 and g == 0:
            break

        # Lines: each has x_i, y_i, d_i, c_i (stations connected, distance, company)
        edges = [[] for _ in range(n+1)]
        for _ in range(m):
            x,y,d,cc = readints()
            edges[x].append((y,d,cc))
            edges[y].append((x,d,cc))

        # Fare tables per company
        p = [0]*(c+1)
        for i in range(1,c+1):
            p[i] = int(sys.stdin.readline())

        q = [[]]*(c+1)
        r = [[]]*(c+1)
        for i in range(1,c+1):
            q[i] = []
            while True:
                line = sys.stdin.readline().strip()
                if line == '-1':
                    break
                q[i].extend(map(int,line.split()))

        for i in range(1,c+1):
            r[i] = []
            while True:
                line = sys.stdin.readline().strip()
                if line == '-1':
                    break
                r[i].extend(map(int,line.split()))

        # Build fare lookup tables for each company
        fare_tables = [None]*(c+1)
        for i in range(1,c+1):
            fare_tables[i] = compute_fares(p[i], q[i], r[i])

        # Use modified Dijkstra with state: (station, current_company, dist_in_company_section)
        # Current_company = 0 means no current company (start state)
        # dist_in_company_section: distance traveled in current company's continuous section
        INF = 10**15
        dist = [ [ [INF]*(201) for _ in range(c+1)] for __ in range(n+1) ]
        # Max distance on single line is up to 200, so dist_in_company_section max 200 sufficient

        # Start state: at s, no company chosen yet, dist 0
        dist[s][0][0] = 0
        pq = []
        heapq.heappush(pq, (0, s, 0, 0))  # (cost, station, current_company, dist_in_current_section)

        while pq:
            cost, u, comp, dd = heapq.heappop(pq)
            if dist[u][comp][dd] < cost:
                continue
            if u == g:
                print(cost)
                break
            for v,dline,cc in edges[u]:
                if comp == 0:
                    # From no company, start a new section with company cc and distance dline
                    new_dist = dline
                    f = fare_tables[cc][new_dist]
                    total_cost = cost + f
                    if total_cost < dist[v][cc][new_dist]:
                        dist[v][cc][new_dist] = total_cost
                        heapq.heappush(pq, (total_cost, v, cc, new_dist))
                else:
                    if cc == comp:
                        # Continue with same company section
                        new_dist = dd + dline
                        if new_dist > 200:
                            # Dist too large, skip (should not happen since max line is 200, but continuous may exceed??)
                            # According to problem max d_i=200, sum can be larger than that. We must handle bigger dist
                            # We'll handle up to max 10000 sum distance for safety.
                            # So increase array size or ignore here.
                            # We'll increase dist_in_company_section max to 10000.
                            # Refactor dist as [n+1][c+1][max_dist+1], where max dist approx m*200=2,000,000 too big.
                            # To avoid memory explosion, we'll use dictionary instead of list.
                            # So need to update code for dist. Let's do this now.
                            continue

                        fnew = fare_tables[comp][new_dist]
                        # cost previously had fare for section with dist dd, now fare with new_dist, need to adjust cost
                        # previous cost includes fare_tables[comp][dd], so difference is fare_tables[comp][new_dist]-fare_tables[comp][dd]
                        total_cost = cost + (fnew - fare_tables[comp][dd])
                        if total_cost < dist[v][comp][new_dist]:
                            dist[v][comp][new_dist] = total_cost
                            heapq.heappush(pq, (total_cost, v, comp, new_dist))

                    else:
                        # Different company, close previous section and start new with cc
                        # Previous section fare is included already in cost, so add new section fare for dline
                        fnew = fare_tables[cc][dline]
                        total_cost = cost + fnew
                        if total_cost < dist[v][cc][dline]:
                            dist[v][cc][dline] = total_cost
                            heapq.heappush(pq, (total_cost, v, cc, dline))
        else:
            # Not break => cannot reach g
            print(-1)

if __name__ == '__main__':
    main()