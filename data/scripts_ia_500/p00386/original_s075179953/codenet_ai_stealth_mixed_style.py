from collections import deque
import sys
sys.setrecursionlimit(10**6)

def iterative_dfs(n, edges):
    height = [None] * n
    dist = [None] * n
    parent = [[None] * 20 for _ in range(n)]
    stack = [(0, 0, 0)]
    while stack:
        x, h, d = stack.pop()
        height[x] = h
        dist[x] = d
        for to, w in edges[x]:
            if height[to] is None:
                parent[to][0] = x
                stack.append((to, h + 1, d + w))
    return height, dist, parent

def build_sparse_table(n, height, parent):
    for j in range(1, 20):
        for i in range(1, n):
            if height[i] is not None and height[i] >= (1 << j):
                parent[i][j] = parent[parent[i][j-1]][j-1]

def adj_height(x, n, parent):
    # tail recursive style: convert to loop for clarity
    for i in range(19, -1, -1):
        if n >= (1 << i) and parent[x][i] is not None:
            x = parent[x][i]
            n -= (1 << i)
    return x

def _lca_recursive(x, y, parent):
    if x == y:
        return x
    for i in reversed(range(1, 20)):
        if parent[x][i] != parent[y][i]:
            return _lca_recursive(parent[x][i - 1], parent[y][i - 1], parent)
    return parent[x][0]

def lca(x, y, height, parent):
    diff = height[x] - height[y]
    if diff < 0:
        y = adj_height(y, -diff, parent)
    elif diff > 0:
        x = adj_height(x, diff, parent)
    if x == y:
        return x
    # iterative binary lift
    for i in reversed(range(20)):
        if parent[x][i] is not None and parent[y][i] is not None and parent[x][i] != parent[y][i]:
            x = parent[x][i]
            y = parent[y][i]
    return parent[x][0]

def bs(index, target, dist, parent):
    # iterative binary search variant
    if index == 0:
        return 0
    if dist[index] >= target >= dist[parent[index][0]]:
        return index
    for i in reversed(range(20)):
        if parent[index][i] is None or dist[parent[index][i]] <= target:
            index = parent[index][i if i - 1 < 0 else i - 1]
            if index == 0 or index is None:
                break
    return index if index is not None else 0

def max_dist(x, y, z, r, dist, height, parent):
    # functional style with map and lambdas
    lcas = list(map(lambda node: lca(node, r, height, parent), [x, y, z]))
    distances = list(map(lambda i: dist[[x, y, z][i]] + dist[r] - 2 * dist[lcas[i]], range(3)))
    return max(distances)

def _score(x, y, z, xy, yz, dist, parent):
    dist_x = dist[x]
    dist_y = dist[y]
    dist_z = dist[z]
    dist_xy = dist[xy]
    dist_yz = dist[yz]
    dx = dist_x + dist_yz - 2 * dist_xy
    dy = dist_y - dist_yz
    dz = dist_z - dist_yz

    def helper(r, d1, d2, val1, val2, base):
        if r == 0:
            return base
        res1 = max(val1 - dist[r], val2 + dist[r] - 2 * d1)
        res2 = max(val1 - dist[parent[r][0]], val2 + dist[parent[r][0]] - 2 * d1)
        return min(res1, res2)

    if dx >= dy >= dz:
        if dist_x >= dist_y:
            r = bs(x, dist_xy + (dist_x - dist_y) / 2, dist, parent)
            return helper(r, dist_xy, dist_yz, dist_x, dist_y, dist_x)
        else:
            r = bs(yz, dist_xy + (dist_y - dist_x) / 2, dist, parent)
            return helper(r, dist_xy, dist_yz, dist_y, dist_x, dist_y)
    elif dx >= dz >= dy:
        if dist_x >= dist_z:
            r = bs(x, dist_xy + (dist_x - dist_z) / 2, dist, parent)
            return helper(r, dist_xy, dist_yz, dist_x, dist_z, dist_x)
        else:
            r = bs(yz, dist_xy + (dist_z - dist_x) / 2, dist, parent)
            return helper(r, dist_xy, dist_yz, dist_z, dist_x, dist_z)
    elif dy >= dx >= dz:
        r = bs(y, dist_yz + (dy - dx) / 2, dist, parent)
        return helper(r, dist_xy, dist_yz, dist_y, dist_x, dist_y)
    elif dy >= dz >= dx:
        r = bs(y, dist_yz + (dy - dz) / 2, dist, parent)
        return helper(r, dist_yz, dist_yz, dist_y, dist_z, dist_y)
    elif dz >= dx >= dy:
        r = bs(z, dist_yz + (dz - dx) / 2, dist, parent)
        return helper(r, dist_xy, dist_yz, dist_z, dist_x, dist_z)
    elif dz >= dy >= dx:
        r = bs(z, dist_yz + (dz - dy) / 2, dist, parent)
        return helper(r, dist_yz, dist_yz, dist_z, dist_y, dist_z)

def score(a, b, c, lca, dist, height, parent):
    a -= 1; b -= 1; c -= 1
    ab = lca(a, b, height, parent)
    ac = lca(a, c, height, parent)
    bc = lca(b, c, height, parent)
    if ab == ac:
        return _score(a, b, c, ab, bc, dist, parent)
    elif ab == bc:
        return _score(b, a, c, ab, ac, dist, parent)
    else:
        return _score(c, a, b, ac, ab, dist, parent)

def main():
    n,q = map(int, input().split())
    edges = [[] for _ in range(n)]
    for _ in range(n-1):
        u,v,w = map(int, input().split())
        u -= 1; v -= 1
        edges[u].append((v,w))
        edges[v].append((u,w))

    height, dist, parent = iterative_dfs(n, edges)
    build_sparse_table(n, height, parent)

    for _ in range(q):
        a,b,c = map(int, input().split())
        res = score(a,b,c, lca, dist, height, parent)
        print(res)

if __name__ == '__main__':
    main()