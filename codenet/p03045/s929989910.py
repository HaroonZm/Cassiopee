# UnionFind、0-indexであることに注意
#############################################################

class UnionFind:

    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, v):  # vが属する集合の根を返す
        if self.parents[v] < 0:
            return v
        else:
            self.parents[v] = self.find(self.parents[v])
            return self.parents[v]

    def unite(self, u, v):  # 「uが属する集合」と「vが属する集合」を併合（根同士を結ぶ）
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return
        if self.parents[u] > self.parents[v]:  # u < v に統一する
            u, v = v, u
        self.parents[u] += self.parents[v]
        self.parents[v] = u

    def size(self, v):  # vが属する集合の要素数
        return -self.parents[self.find(v)]

    def same(self, u, v):  # uとvが同じ集合に属するか否か
        return self.find(u) == self.find(v)

#############################################################
N, M = map(int, input().split())

uf = UnionFind(N)

# a+bの偶奇が分かる
# ここで、実際の偶奇や、zの値は必要ない
# 一方が分かれば他方も分かる、ということが本質
for _ in range(M):
    a, b, z = map(int, input().split())
    uf.unite(a - 1, b - 1)

# A_1 + A_2の偶奇, A_2 + A_3の偶奇が分かった時、
# 1つだけ魔法で確定させれば他の値は確定する。

# M個の条件についてUnionFindを生成する。
# 連結成分ごとに1回魔法を使えばあとは芋づる式に求まる。

# (連結成分の個数) = (rootの値が何種類存在するか)

root_list = []

for i in range(N):
    root_list.append(uf.find(i))

root_set = set(root_list)

print(len(root_set))