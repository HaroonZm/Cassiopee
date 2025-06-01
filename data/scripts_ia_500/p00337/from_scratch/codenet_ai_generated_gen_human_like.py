import math
import sys
sys.setrecursionlimit(10**7)

def distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def ccw(p1, p2, p3):
    # p1, p2, p3 はそれぞれ(x, y)
    return (p2[0]-p1[0])*(p3[1]-p1[1]) - (p2[1]-p1[1])*(p3[0]-p1[0])

def segments_intersect(a1, a2, b1, b2):
    # ２つの線分(a1,a2)と(b1,b2)が交差するか判定
    c1 = ccw(a1, a2, b1)
    c2 = ccw(a1, a2, b2)
    c3 = ccw(b1, b2, a1)
    c4 = ccw(b1, b2, a2)
    if c1*c2 < 0 and c3*c4 < 0:
        return True
    return False

class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
    def find(self, x):
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        self.par[y] = x
        return True

V, R = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(V)]
edges = []
for _ in range(R):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    d = distance(points[s], points[t])
    edges.append((d, s, t))

# 境界線は凸包上で、境界線上の辺は必ず道でなければならない
# 凸包上の辺が道にない場合、国が新たに作るが、
# 村人たちは道の総長を最小にしたいため、
# 凸包の辺は元道にあるか、新たに作られても必ず含める

# 1. 凸包を求める
# Graham Scanで凸包を作る
points_with_idx = list(enumerate(points))
points_sorted = sorted(points_with_idx, key=lambda x: (x[1][0], x[1][1]))

def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])

lower = []
for i, p in points_sorted:
    while len(lower) >= 2 and cross(points[lower[-2]], points[lower[-1]], p) <= 0:
        lower.pop()
    lower.append(i)
upper = []
for i, p in reversed(points_sorted):
    while len(upper) >= 2 and cross(points[upper[-2]], points[upper[-1]], p) <= 0:
        upper.pop()
    upper.append(i)
convex_hull = lower[:-1] + upper[:-1]  # 重複ポイント除去
ch_set = set(convex_hull)

# 2. 凸包の辺が元々道に含まれているか確かめる
# 辺がない場合は新道を作る必要があるのでそれらも合わせて最低コストの道を選ぶ
# 凸包の辺にある道は必須で選ぶ（境界線上の道）
# 新道は既存にない凸包辺として追加する

road_map = [[False]*V for _ in range(V)]
for _, s, t in edges:
    road_map[s][t] = True
    road_map[t][s] = True

hull_edges = []
for i in range(len(convex_hull)):
    a = convex_hull[i]
    b = convex_hull[(i+1) % len(convex_hull)]
    if a > b:
        a, b = b, a
    hull_edges.append((a, b))

hull_edge_set = set(hull_edges)

# hullにある辺が元道にあればコストそのまま、なければ新道として加える
hull_edges_cost = {}
for a, b in hull_edges:
    if road_map[a][b]:
        # 元道
        d = distance(points[a], points[b])
        hull_edges_cost[(a, b)] = d
    else:
        # 新道
        d = distance(points[a], points[b])
        hull_edges_cost[(a, b)] = d

# 3. MSTを作るが、凸包辺は必ず含める必要がある
# 凸包辺で元道であれば最初にUFに繋ぎ、コストに加える
# 新道である凸包辺も必ず含めてコストに加える

uf = UnionFind(V)
ans = 0.0
# 凸包の辺は必ず使う
for (a,b), d in hull_edges_cost.items():
    uf.union(a, b)
    ans += d

# 4. 凸包辺以外で元道の辺をコスト順に並べ、
#   MST的にスパニングツリー完成まで追加していく
other_edges = []
for d, s, t in edges:
    a, b = s, t
    if a > b:
        a, b = b, a
    if (a, b) in hull_edge_set:
        # 凸包辺はすでに加えたのでスキップ
        continue
    other_edges.append((d, s, t))
other_edges.sort()

for d, s, t in other_edges:
    if uf.union(s, t):
        ans += d

print(f"{ans:.10f}")