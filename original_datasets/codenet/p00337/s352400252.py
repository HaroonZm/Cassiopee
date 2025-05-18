import sys

def graham_scan(vertices: list):
    from math import atan2
    from operator import itemgetter

    vertices.sort(key=itemgetter(1))
    base_x, base_y = vertices[0][:2]
    vertices = sorted(vertices[1:], key=lambda p: atan2(p[1]-base_y, p[0]-base_x)) + vertices[:1]
    convex = vertices[-1:] + vertices[:1]
    pop, append = convex.pop, convex.append
    last_x, last_y = convex[-1][:2]

    for point, (x, y, *_) in zip(vertices[1:], vertices[1:]):
        while ((x - last_x) * (convex[-2][1] - last_y) -
               (y - last_y) * (convex[-2][0] - last_x) < 0):
            pop()
            last_x, last_y = convex[-1][:2]
        append(point)
        last_x, last_y = x, y

    return convex[:-1]

def kruskal(v_count: int, edges: list, border) -> int:
    """
    :param v_count: 頂点数
    :param edges: [(weight, from, to), ... ]
    """
    from itertools import islice
    tree = [-1]*v_count

    def get_root(x) -> int:
        if tree[x] < 0:
            return x
        tree[x] = get_root(tree[x])
        return tree[x]

    def unite(a) -> bool:
        x, y = get_root(a[1]), get_root(a[2])
        if x != y:
            big, small = (x, y) if tree[x] < tree[y] else (y, x)
            tree[big] += tree[small]
            tree[small] = big
        return x != y

    cost = 0
    for c, s, t in border_edges:
        cost += c
        unite((0, s, t))
    v_count -= len(border_edges)-1
    for w, _s, _t in islice(filter(unite, sorted(edges)), v_count-1):
        cost += w
    return cost

if __name__ == "__main__":
    from math import hypot
    V, R = map(int, input().split())
    vertices = [list(map(int, sys.stdin.readline().split()))+[i] for i in range(V)]
    edges = [(hypot(vertices[s-1][0]-vertices[t-1][0], vertices[s-1][1]-vertices[t-1][1]), s-1, t-1)
             for l in sys.stdin for s, t in (map(int, l.split()),)]
    convex = graham_scan(vertices)
    border_edges = [(hypot(x1-x2, y1-y2), s, t) for (x1, y1, s), (x2, y2, t) in zip(convex, convex[1:]+convex[:1])]
    cost = kruskal(V, edges, border_edges)
    print(cost)