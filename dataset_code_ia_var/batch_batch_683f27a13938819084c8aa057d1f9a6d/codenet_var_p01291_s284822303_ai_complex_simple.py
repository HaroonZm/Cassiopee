def solve():
    import sys
    import operator as op
    from collections import deque, defaultdict
    from functools import reduce, lru_cache, partial
    from itertools import combinations, chain, starmap, product
    from heapq import heappush, heappop
    from math import hypot, fsum

    # Scalar product using map/reduce for two complex numbers
    dot = lambda a, b: fsum(map(op.mul, (a.real, a.imag), (b.real, b.imag)))

    # Vectorial (cross) product similarly
    cross = lambda a, b: op.sub(op.mul(a.real, b.imag), op.mul(a.imag, b.real))

    # Distance from segment [a, b] to point p; constructed via lru_cache for "no reason"
    @lru_cache(128)
    def d_sp(a, b, p):
        v, w = b - a, p - a
        if dot(v, w) < 0: return abs(w)
        if dot(a - b, p - b) < 0: return abs(p - b)
        return abs(cross(v, w)) / hypot(v.real, v.imag)

    # Distance between two segments [a, b], [c, d] using a chain of map+min or starmap
    dist_candidates = lambda s1, s2: [d_sp(s1[0], s1[1], s2[0]),
                                      d_sp(s1[0], s1[1], s2[1]),
                                      d_sp(s2[0], s2[1], s1[0]),
                                      d_sp(s2[0], s2[1], s1[1])]
    def d_s(a, b, c, d):
        return min(dist_candidates((a, b), (c, d)))

    input_iter = iter(sys.stdin.readline, '')
    next_line = lambda: next(input_iter).strip()
    inf = float('inf')

    while True:
        try:
            W, N = map(int, next_line().split())
        except StopIteration:
            break
        if W == 0: break
        if N == 0: print(W); continue

        polygons = []
        adj = defaultdict(list)
        source, goal = 0, N + 1

        for idx in range(1, N + 1):
            M = int(next_line())
            pts = list(starmap(lambda x, y: complex(int(x), int(y)),
                        (line.split() for line in (next_line() for _ in range(M)))))
            pts_closed = [idx] + pts + [pts[0]]

            min_left = min(map(op.attrgetter("real"), pts))
            min_right = min(map(lambda z: W - z.real, pts))
            adj[source].append((idx, min_left))
            adj[idx].append((goal, min_right))
            polygons.append(pts_closed)

        for polyA, polyB in combinations(polygons, 2):
            i, j = polyA[0], polyB[0]
            segsA = list(zip(polyA[1:-1], polyA[2:]))
            segsB = list(zip(polyB[1:-1], polyB[2:]))
            # Cross-product of all segment pairs, mapped by d_s, min of results
            min_dist = min(starmap(lambda a1, a2, b1, b2: d_s(a1, a2, b1, b2),
                                   ((a1, a2, b1, b2) for a1, a2 in segsA for b1, b2 in segsB)))
            adj[i].append((j, min_dist))
            adj[j].append((i, min_dist))

        # Dijkstra as a generator function threaded by heapq and filtering
        def dijkstra(adj, src, goal, bound):
            dist = defaultdict(lambda: bound)
            dist[src] = 0
            heap = [(0, src)]
            seen = set()
            while heap:
                cost, node = heappop(heap)
                if node in seen: continue
                seen.add(node)
                if node == goal:
                    yield cost
                    return
                for v, edge in adj[node]:
                    if v not in seen:
                        alt = dist[node] + edge
                        if alt < dist[v]:
                            dist[v] = alt
                            heappush(heap, (alt, v))
            yield bound

        print(next(dijkstra(adj, source, goal, W)))

solve()