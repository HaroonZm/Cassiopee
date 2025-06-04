def solve():
    from itertools import combinations
    from heapq import heappush, heappop
    from sys import stdin

    # -- Geometry helpers --
    def to_complex(x, y):
        return x + y * 1j

    def dot(c1, c2):
        return c1.real * c2.real + c1.imag * c2.imag

    def cross(c1, c2):
        return c1.real * c2.imag - c1.imag * c2.real

    def vector_from_points(p1, p2):
        return p2 - p1

    def distance_point_point(p1, p2):
        return abs(p1 - p2)

    def distance_point_segment(sp1, sp2, p):
        a = vector_from_points(sp1, sp2)
        b = vector_from_points(sp1, p)
        if dot(a, b) < 0:
            return abs(b)
        c = vector_from_points(sp2, sp1)
        d = vector_from_points(sp2, p)
        if dot(c, d) < 0:
            return abs(d)
        return abs(cross(a, b) / a)

    def segment_edges(polygon):
        return zip(polygon[1:], polygon[2:])

    def min_distance_between_segments(p1, p2, p3, p4):
        return min(
            distance_point_segment(p1, p2, p3),
            distance_point_segment(p1, p2, p4),
            distance_point_segment(p3, p4, p1),
            distance_point_segment(p3, p4, p2)
        )

    def distance_between_polygons(poly1, poly2):
        dists = []
        for v1, v2 in segment_edges(poly1):
            for u1, u2 in segment_edges(poly2):
                d = min_distance_between_segments(v1, v2, u1, u2)
                dists.append(d)
        return min(dists)

    # -- Parsing input and building polygons/graph --
    def parse_line_of_ints():
        return list(map(int, stdin.readline().split()))

    def parse_one_polygon(M):
        verts = []
        s_d = None
        g_d = None
        min_left = None
        min_right = None
        for _ in range(M):
            x, y = parse_line_of_ints()
            verts.append(to_complex(x, y))
            if min_left is None or x < min_left:
                min_left = x
            if min_right is None or (W - x) < min_right:
                min_right = W - x
        s_d = min_left
        g_d = min_right
        return verts, s_d, g_d

    def build_graph(W, N, polygon_datas):
        polygons = []
        # adj[0] is start, adj[i] is polygon i, adj[N+1] is goal
        adj = [[] for _ in range(N + 2)]
        goal = N + 1
        for idx, (pverts, s_d, g_d) in enumerate(polygon_datas, 1):
            p = [idx]
            p.extend(pverts)
            # For easier edge looping: close polygon
            p.append(pverts[0])
            polygons.append(p)
            adj[0].append((idx, s_d))
            adj[idx].append((goal, g_d))
        # Inter-polygon edges
        for p1, p2 in combinations(polygons, 2):
            i = p1[0]
            j = p2[0]
            d = distance_between_polygons(p1, p2)
            adj[i].append((j, d))
            adj[j].append((i, d))
        return adj

    def read_polygons(N, W):
        polygon_datas = []
        for _ in range(N):
            M = int(stdin.readline())
            verts, s_d, g_d = parse_one_polygon(M)
            polygon_datas.append((verts, s_d, g_d))
        return polygon_datas

    # -- Dijkstra --
    def dijkstra(W, N, adj):
        goal = N + 1
        PQ = [(0, 0)]
        isVisited = [False] * (N + 2)
        distance = [W] * (N + 2)
        distance[0] = 0
        while PQ:
            u_cost, u = heappop(PQ)
            if u == goal:
                return int(u_cost)
            if u_cost > distance[u]:
                continue
            if isVisited[u]:
                continue
            isVisited[u] = True
            for v, v_cost in adj[u]:
                if isVisited[v]:
                    continue
                t_cost = distance[u] + v_cost
                if t_cost < distance[v]:
                    distance[v] = t_cost
                    heappush(PQ, (t_cost, v))
        return None

    # -- Main loop --
    def process_case(W, N):
        if N == 0:
            print(W)
            return
        polygon_datas = read_polygons(N, W)
        adj = build_graph(W, N, polygon_datas)
        answer = dijkstra(W, N, adj)
        print(answer)

    def should_stop(line):
        W, N = map(int, line.split())
        if W == 0:
            return True
        return False

    def process_input():
        while True:
            line = stdin.readline()
            if not line:
                break
            W_N = line.strip()
            if not W_N:
                continue
            if should_stop(W_N):
                break
            W, N = map(int, W_N.split())
            process_case(W, N)

    process_input()