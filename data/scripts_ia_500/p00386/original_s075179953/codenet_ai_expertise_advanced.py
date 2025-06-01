import sys
sys.setrecursionlimit(10**7)
from operator import itemgetter
input = sys.stdin.readline

def main():
    n, q = map(int, input().split())
    edges = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        u -= 1; v -= 1
        edges[u].append((v, w))
        edges[v].append((u, w))

    LOG = 20
    height = [-1] * n
    dist = [0] * n
    parent = [[-1] * n for _ in range(LOG)]
    stack = [(0, 0)]
    height[0] = 0
    while stack:
        u, d = stack.pop()
        for v, w in edges[u]:
            if height[v] == -1:
                height[v] = height[u] + 1
                dist[v] = dist[u] + w
                parent[0][v] = u
                stack.append((v, d + w))

    for k in range(1, LOG):
        p = parent[k-1]
        for v in range(n):
            if p[v] != -1:
                parent[k][v] = p[p[v]]

    def lift_node(u, diff):
        for i in range(LOG):
            if diff & (1 << i):
                u = parent[i][u]
        return u

    def lca(u, v):
        if height[u] < height[v]:
            u, v = v, u
        u = lift_node(u, height[u] - height[v])
        if u == v:
            return u
        for i in reversed(range(LOG)):
            if parent[i][u] != parent[i][v]:
                u, v = parent[i][u], parent[i][v]
        return parent[0][u]

    def bs(u, target):
        if u == -1 or dist[u] < target:
            return 0
        for i in reversed(range(LOG)):
            p = parent[i][u]
            if p != -1 and dist[p] >= target:
                u = p
        return u

    def max_dist(x, y, z, r):
        xr = lca(x, r)
        yr = lca(y, r)
        zr = lca(z, r)
        return max(dist[x] + dist[r] - 2 * dist[xr],
                   dist[y] + dist[r] - 2 * dist[yr],
                   dist[z] + dist[r] - 2 * dist[zr])

    def _score(x, y, z, xy, yz):
        dx = dist[x] + dist[yz] - 2 * dist[xy]
        dy = dist[y] - dist[yz]
        dz = dist[z] - dist[yz]

        if dx >= dy and dy >= dz:
            if dist[x] >= dist[y]:
                r = bs(x, dist[xy] + (dist[x] - dist[y]) / 2)
                if r == 0:
                    return dist[x]
                pr = parent[0][r]
                return min(max(dist[x] - dist[r], dist[y] + dist[r] - 2 * dist[xy]),
                           max(dist[x] - dist[pr], dist[y] + dist[pr] - 2 * dist[xy]))
            else:
                r = bs(yz, dist[xy] + (dist[y] - dist[x]) / 2)
                if r == 0:
                    return dist[y]
                pr = parent[0][r]
                return min(max(dist[y] - dist[r], dist[x] + dist[r] - 2 * dist[xy]),
                           max(dist[y] - dist[pr], dist[x] + dist[pr] - 2 * dist[xy]))

        if dx >= dz and dz >= dy:
            if dist[x] >= dist[z]:
                r = bs(x, dist[xy] + (dist[x] - dist[z]) / 2)
                if r == 0:
                    return dist[x]
                pr = parent[0][r]
                return min(max(dist[x] - dist[r], dist[z] + dist[r] - 2 * dist[xy]),
                           max(dist[x] - dist[pr], dist[z] + dist[pr] - 2 * dist[xy]))
            else:
                r = bs(yz, dist[xy] + (dist[z] - dist[x]) / 2)
                if r == 0:
                    return dist[z]
                pr = parent[0][r]
                return min(max(dist[z] - dist[r], dist[x] + dist[r] - 2 * dist[xy]),
                           max(dist[z] - dist[pr], dist[x] + dist[pr] - 2 * dist[xy]))

        if dy >= dx and dx >= dz:
            r = bs(y, dist[yz] + (dy - dx) / 2)
            if r == 0:
                return dist[y]
            pr = parent[0][r]
            return min(max(dist[y] - dist[r], dist[x] + dist[r] - 2 * dist[xy]),
                       max(dist[y] - dist[pr], dist[x] + dist[pr] - 2 * dist[xy]))

        if dy >= dz and dz >= dx:
            r = bs(y, dist[yz] + (dy - dz) / 2)
            if r == 0:
                return dist[y]
            pr = parent[0][r]
            return min(max(dist[y] - dist[r], dist[z] + dist[r] - 2 * dist[yz]),
                       max(dist[y] - dist[pr], dist[z] + dist[pr] - 2 * dist[yz]))

        if dz >= dx and dx >= dy:
            r = bs(z, dist[yz] + (dz - dx) / 2)
            if r == 0:
                return dist[z]
            pr = parent[0][r]
            return min(max(dist[z] - dist[r], dist[x] + dist[r] - 2 * dist[xy]),
                       max(dist[z] - dist[pr], dist[x] + dist[pr] - 2 * dist[xy]))

        if dz >= dy and dy >= dx:
            r = bs(z, dist[yz] + (dz - dy) / 2)
            if r == 0:
                return dist[z]
            pr = parent[0][r]
            return min(max(dist[z] - dist[r], dist[y] + dist[r] - 2 * dist[yz]),
                       max(dist[z] - dist[pr], dist[y] + dist[pr] - 2 * dist[yz]))

    def score(a, b, c):
        a, b, c = a - 1, b - 1, c - 1
        ab = lca(a, b)
        ac = lca(a, c)
        bc = lca(b, c)
        if ab == ac:
            return _score(a, b, c, ab, bc)
        elif ab == bc:
            return _score(b, a, c, ab, ac)
        else:
            return _score(c, a, b, ac, ab)

    print(*(score(*map(int, input().split())) for _ in range(q)), sep='\n')

main()