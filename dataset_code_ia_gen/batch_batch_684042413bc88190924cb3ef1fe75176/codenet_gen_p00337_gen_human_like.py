import sys
import math
sys.setrecursionlimit(10**7)

def dist(a, b):
    return math.hypot(x[a]-x[b], y[a]-y[b])

def cross(u, v):
    return u[0]*v[1] - u[1]*v[0]

def on_segment(p, q, r):
    # qがp-r上にあるか判定 (閉区間)
    return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))

def segments_intersect(a1, a2, b1, b2):
    # a1, a2, b1, b2 は座標
    v1 = (a2[0]-a1[0], a2[1]-a1[1])
    v2 = (b2[0]-b1[0], b2[1]-b1[1])
    v3 = (b1[0]-a1[0], b1[1]-a1[1])
    v4 = (b2[0]-a1[0], b2[1]-a1[1])
    v5 = (a1[0]-b1[0], a1[1]-b1[1])
    v6 = (a2[0]-b1[0], a2[1]-b1[1])

    c1 = cross(v1, v3)
    c2 = cross(v1, v4)
    c3 = cross(v2, v5)
    c4 = cross(v2, v6)

    if c1*c2 < 0 and c3*c4 < 0:
        return True
    # 端点が重なる場合等
    if c1 == 0 and on_segment(a1, b1, a2):
        return True
    if c2 == 0 and on_segment(a1, b2, a2):
        return True
    if c3 == 0 and on_segment(b1, a1, b2):
        return True
    if c4 == 0 and on_segment(b1, a2, b2):
        return True
    return False

def is_inside_convex_polygon(p, polygon):
    # 凸多角形の内部判定（境界含む）
    n = len(polygon)
    prev = 0
    for i in range(n):
        a = polygon[i]
        b = polygon[(i+1)%n]
        v1 = (b[0]-a[0], b[1]-a[1])
        v2 = (p[0]-a[0], p[1]-a[1])
        c = cross(v1, v2)
        if c == 0:
            # 辺上なら内部とみなす
            return True
        if c*prev < 0 and prev != 0:
            return False
        if c != 0:
            prev = c
    return True

def segment_inside_polygon(a, b, polygon):
    # 線分abが多角形の内部か境界上にあるか
    # 点a,bが内部または境界上にあることは前提とする
    # 線分と多角形の辺との交差をチェック（端点同士の接触除く）
    n = len(polygon)
    for i in range(n):
        c = polygon[i]
        d = polygon[(i+1)%n]
        # もしabとcdが交差して、共通端点でなければダメ
        if segments_intersect(a, b, c, d):
            # 共通端点なら問題ないがそうでなければ境界越え
            pts = {a,b,c,d}
            # 端点が共有している場合を許す
            endpoints = 0
            if a == c or a == d: endpoints += 1
            if b == c or b == d: endpoints += 1
            if endpoints < 1: # 共有端点なしで交差 -> 内部を越える
                return False
            # 交差点が共通端点なら許す
            # ただし、まったく接触は問題ないので交差とした場合はFalseにしない
    return True

def find_boundary_polygon(edges):
    # 辺群が単純な多角形の境界線だと仮定し、その順序を得る
    adjacency = {}
    for a,b in edges:
        adjacency.setdefault(a, []).append(b)
        adjacency.setdefault(b, []).append(a)
    # 各頂点は2本の辺
    start = min(adjacency.keys())
    polygon = [start]
    prev = None
    current = start
    while True:
        neighbors = adjacency[current]
        nextv = neighbors[0] if neighbors[0] != prev else neighbors[1]
        if nextv == start:
            break
        polygon.append(nextv)
        prev, current = current, nextv
    return polygon

def find_convex_hull(points):
    points = sorted(points)
    if len(points) <= 1:
        return points[:]
    lower = []
    for p in points:
        while len(lower) >= 2 and cross((lower[-1][0]-lower[-2][0], lower[-1][1]-lower[-2][1]),
                                        (p[0]-lower[-1][0], p[1]-lower[-1][1])) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross((upper[-1][0]-upper[-2][0], upper[-1][1]-upper[-2][1]),
                                        (p[0]-upper[-1][0], p[1]-upper[-1][1])) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

V,R = map(int,input().split())
x = [0]*V
y = [0]*V
for i in range(V):
    xi, yi = map(int,input().split())
    x[i] = xi
    y[i] = yi

edges_original = []
for _ in range(R):
    s,t = map(int,input().split())
    edges_original.append((s-1,t-1))

points = [(x[i], y[i]) for i in range(V)]

# 凸包を求め境界線を確定する
hull = find_convex_hull(points)

# 凸包の頂点リストを頂点番号に置き換え（凸包上の集落の番号）
hull_set = set(hull)
hull_indices = []
for i, p in enumerate(points):
    if p in hull_set:
        hull_indices.append(i)
hull_indices.sort(key=lambda i: (points[i][0], points[i][1]))
# hullは凸包の点リスト(座標), hull_indicesはそのインデックス（座標版で演算したので単純に保持）

# hullは凸包の頂点を順番に並べた座標リストなので、hull_indicesはそれに合わせて順序を得る必要がある
# hullと同じ順序でhull_indicesを並べ替え
pos_map = {p:i for i,p in enumerate(hull)}
hull_indices = sorted([i for i in range(V) if points[i] in hull_set],
                      key=lambda i: pos_map[points[i]])

# 凸包上の辺を境界線の道とする（新規道は追加不要）
boundary_edges = []
for i in range(len(hull_indices)):
    a = hull_indices[i]
    b = hull_indices[(i+1)%len(hull_indices)]
    boundary_edges.append((a,b))

# DFSで凸包の内側にある集落を判定するため、境界のポリゴン座標リストを用いる
polygon_coords = [points[i] for i in hull_indices]

# convex hull内にあるか判定する関数をおいた

# 辺の中に凸包の辺を固定で入れる
# また、境界線上の辺は村の境界線上にある道として必ず残す必要がある
# 他の辺は自由に選べ村の内側にあり、すべての集落を繋ぐようにする

# 問題は最終的に村の境界線上に道を置き、かつ
# 全ての集落が繋がるようにしつつ、維持費の合計(道の総長)を最小化すること

# アプローチ：
# 1. 凸包の辺は必ず残す（境界線上の道）
# 2. 内側の辺は元の道の中から選べる
# 3. すべての集落が連結であることを満たしつつ、辺の長さの和を最小化する
# 4. 凸包の各辺の間は境界線上なのでその辺は内側として問題ない

# よって、与えられたグラフに凸包の辺を固定的に入れた上で、
# 追加の辺は元の道から選び最小全域木を作る問題になる

# あとはUnion-Findを用いたクラスカル法で解く

# Union-Find
class UnionFind:
    def __init__(self,n):
        self.par = list(range(n))
        self.rank = [0]*n
    def find(self,x):
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        return True

uf = UnionFind(V)

lengths = {}
for s,t in edges_original:
    length = dist(s,t)
    lengths[(s,t)] = length
    lengths[(t,s)] = length

total = 0.0
# まず凸包辺をつなぐ
for a,b in boundary_edges:
    uf.union(a,b)
    total += lengths.get((a,b), dist(a,b))

# 辺を長さ順に並べる（凸包辺は除く）
edges_rest = []
for s,t in edges_original:
    # 凸包辺を除く
    if (s,t) in boundary_edges or (t,s) in boundary_edges:
        continue
    edges_rest.append((lengths[(s,t)], s, t))
edges_rest.sort()

# コスト最小で連結になるように辺を足す
for length, s, t in edges_rest:
    # 辺stが境界線上になければ良いが、境界線上にある辺は全部凸包辺なのでここでは除外済み
    if uf.find(s) != uf.find(t):
        uf.union(s,t)
        total += length

print(total)