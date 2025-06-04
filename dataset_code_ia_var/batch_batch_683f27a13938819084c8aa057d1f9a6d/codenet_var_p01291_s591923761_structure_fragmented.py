from heapq import heappush, heappop
import sys

def get_input():
    return sys.stdin.readline

def get_output():
    return sys.stdout.write

def cross2(p, q):
    return p[0]*q[1] - p[1]*q[0]

def dot2(p, q):
    return p[0]*q[0] + p[1]*q[1]

def dist2(p):
    return p[0]**2 + p[1]**2

def sub_points(a, b):
    return (a[0] - b[0], a[1] - b[1])

def norm2(v):
    return v[0]**2 + v[1]**2

def compute_z0(p0, p1):
    return sub_points(p1, p0)

def compute_z1(x, p0):
    return sub_points(x, p0)

def compute_z2(x, p1):
    return sub_points(x, p1)

def check_in_segment_projection(z0, z1):
    return 0 <= dot2(z0, z1) <= norm2(z0)

def compute_proj_distance(z0, z1):
    return cross2(z0, z1)**2 / norm2(z0)

def get_segment_distances(x, p0, p1):
    z0 = compute_z0(p0, p1)
    z1 = compute_z1(x, p0)
    if check_in_segment_projection(z0, z1):
        return compute_proj_distance(z0, z1)
    z2 = compute_z2(x, p1)
    return min(norm2(z1), norm2(z2))

def segment_line_dist(x, p0, p1):
    return get_segment_distances(x, p0, p1)

def read_W_N(readline):
    return map(int, readline().split())

def check_terminate(W, N):
    return W == 0 and N == 0

def read_polygon(M, readline):
    return [list(map(int, readline().split())) for _ in range(M)]

def read_polygons(N, readline):
    PS = []
    for _ in range(N):
        M = int(readline())
        P = read_polygon(M, readline)
        PS.append(P)
    return PS

def init_graph(N):
    return [[] for _ in range(N+2)]

def update_r_with_p1_q1q2(Pj, nj, p1, r):
    for k in range(nj):
        q1 = Pj[k-1]
        q2 = Pj[k]
        r = min(r, segment_line_dist(p1, q1, q2))
    return r

def update_r_with_q1_p1p2(Pi, ni, q1, r):
    for k in range(ni):
        p1 = Pi[k-1]
        p2 = Pi[k]
        r = min(r, segment_line_dist(q1, p1, p2))
    return r

def process_edges_between(Pi, Pj):
    ni = len(Pi)
    nj = len(Pj)
    r = 10**18
    for p1 in Pi:
        r = update_r_with_p1_q1q2(Pj, nj, p1, r)
    for q1 in Pj:
        r = update_r_with_q1_p1p2(Pi, ni, q1, r)
    return r ** 0.5

def add_polygon_edges(N, PS, G):
    for i in range(N):
        Pi = PS[i]
        ni = len(Pi)
        for j in range(i+1, N):
            Pj = PS[j]
            d = process_edges_between(Pi, Pj)
            G[i].append((j, d))
            G[j].append((i, d))
        d_left = min(x for x, y in Pi)
        G[i].append((N, d_left))
        G[N].append((i, d_left))
        d_right = W_minus_max_x(Pi, W)
        G[i].append((N+1, d_right))
        G[N+1].append((i, d_right))
    return G

def W_minus_max_x(Pi, W):
    return W - max(x for x, y in Pi)

def add_virtual_edges(N, G, W):
    G[N].append((N+1, W))
    G[N+1].append((N, W))
    return G

def dijkstra(N, G):
    que = [(0, N)]
    dist = [10**18] * (N+2)
    dist[N] = 0
    while que:
        cost, v = heappop(que)
        if dist[v] < cost:
            continue
        for w, d in G[v]:
            if cost + d < dist[w]:
                dist[w] = cost + d
                heappush(que, (cost + d, w))
    return dist

def output_result(dist, N, write):
    write("%.16f\n" % dist[N+1])

def process_case(readline, write):
    W, N = read_W_N(readline)
    if check_terminate(W, N):
        return False
    PS = read_polygons(N, readline)
    G = init_graph(N)
    global W_cache
    W_cache = W
    add_polygon_edges(N, PS, G)
    add_virtual_edges(N, G, W)
    dist = dijkstra(N, G)
    output_result(dist, N, write)
    return True

def main():
    readline = get_input()
    write = get_output()
    while process_case(readline, write):
        pass

main()