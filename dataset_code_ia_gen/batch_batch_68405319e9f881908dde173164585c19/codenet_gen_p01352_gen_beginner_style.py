import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, k = map(int, input().split())
edges = {}
queries = []

for _ in range(k):
    t, u, v = map(int, input().split())
    if u > v:
        u, v = v, u
    queries.append((t, u, v))
    if t == 1:
        edges[(u, v)] = edges.get((u, v), 0) + 1
    elif t == 2:
        edges[(u, v)] = edges.get((u, v), 0) - 1

# いま建っている全ての通路の状態を管理
# 質問段階での通路の状態を管理するのが難しいため
# 一番簡単な方法は各質問の時点で現在の通路でグラフを作って
# DFSやUnion-Findで繋がりを確認することだが、
# k=40000なので単純なやり方でやってみる。

# 素朴なUnionFind実装
class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0]*n
    def find(self, x):
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
    def same(self, x, y):
        return self.find(x) == self.find(y)

# 現在の通路の状態を管理するためのセット
current_edges = set()
uf = UnionFind(n)

for q in queries:
    t, u, v = q
    if t == 1:
        # 通路建設
        current_edges.add((u, v))
        uf.unite(u, v)
    elif t == 2:
        # 通路破壊
        # 素朴に破壊しようとしてもUnionFindは戻せないので、やり直しする
        # 通路を一旦削除し、UnionFindを初期化して残りの通路で再構築する
        if (u, v) in current_edges:
            current_edges.remove((u, v))
            uf = UnionFind(n)
            for (a, b) in current_edges:
                uf.unite(a, b)
    else:
        # 質問
        if uf.same(u, v):
            print("YES")
        else:
            print("NO")