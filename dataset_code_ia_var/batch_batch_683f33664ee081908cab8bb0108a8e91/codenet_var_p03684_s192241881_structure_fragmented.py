from heapq import heappush, heappop, heapify

class UnionFind():
    def __init__(self, n):
        self._init_parents(n)
    def _init_parents(self, n):
        self.n = n
        self.parents = [-1] * n
    def find(self, x):
        return self._find_internal(x)
    def _find_internal(self, x):
        if self.parents[x] < 0:
            return x
        self.parents[x] = self._find_internal(self.parents[x])
        return self.parents[x]
    def union(self, x, y):
        self._union_internal(x, y)
    def _union_internal(self, x, y):
        x = self._find_internal(x)
        y = self._find_internal(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

def get_input_N():
    return int(input())

def get_input_points(N):
    return [_get_xyi(i) for i in range(N)]

def _get_xyi(i):
    x, y = map(int, input().split())
    return (x, y, i)

def sort_points_by_x(points):
    return sorted(points, key=lambda pt: pt[0])

def sort_points_by_y(points):
    return sorted(points, key=lambda pt: pt[1])

def initialize_heap():
    return []

def build_edges_by_x(points, H):
    _build_edges_generic(points, H, idx=0)

def build_edges_by_y(points, H):
    _build_edges_generic(points, H, idx=1)

def _build_edges_generic(points, H, idx):
    N = len(points)
    for i in range(N-1):
        _process_edge(points, H, i, idx)

def _process_edge(points, H, i, idx):
    coord1, j1 = points[i][idx], points[i][2]
    coord2, j2 = points[i+1][idx], points[i+1][2]
    cost = coord2 - coord1
    heappush(H, (cost, j1, j2))

def process_edges(H, N):
    uf = _make_unionfind(N)
    ans = [0]
    _process_heap(H, uf, ans)
    return ans[0]

def _make_unionfind(N):
    return UnionFind(N)

def _process_heap(H, uf, ans):
    while H:
        w,s,t = heappop(H)
        if _need_union(uf, s, t):
            _do_union_and_add(uf, s, t, w, ans)

def _need_union(uf, s, t):
    return uf.find(s) != uf.find(t)

def _do_union_and_add(uf, s, t, w, ans):
    uf.union(s, t)
    ans[0] += w

def main():
    N = get_input_N()
    points = get_input_points(N)
    points_x_sorted = sort_points_by_x(points)
    points_y_sorted = sort_points_by_y(points)
    H = initialize_heap()
    build_edges_by_x(points_x_sorted, H)
    build_edges_by_y(points_y_sorted, H)
    result = process_edges(H, N)
    print(result)

main()