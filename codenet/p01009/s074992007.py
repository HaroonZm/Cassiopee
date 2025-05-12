# python template for atcoder1
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

class WeightedUnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        # 根への距離を管理
        self.weight = [0] * (n+1)
        self.added = [0]*(n+1)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            y = self.find(self.par[x])
            # 親への重みを追加しながら根まで走査
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y

    # 併合
    def union(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)
        self.added[x] += w
        self.added[y] += w
        # xの木の高さ < yの木の高さ
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
            #self.weight[rx] = w - self.weight[x] + self.weight[y]
            self.weight[rx] = w - self.diff(x, y)
        # xの木の高さ ≧ yの木の高さ
        else:
            self.par[ry] = rx
            #self.weight[ry] = -w - self.weight[y] + self.weight[x]
            self.weight[ry] = -w + self.diff(x, y)
            # 木の高さが同じだった場合の処理
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    # 同じ集合に属するか
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # xからyへのコスト
    def diff(self, x, y):
        return self.weight[x] - self.weight[y]+self.added[x]-self.added[y]

    def added_diff(self, x, y):
        return self.diff(x, y)

def dealIn(l):
    a, b, c = l
    Un.union(b, a, c)

def compare(l):
    a, b = l
    if Un.same(a, b):
        diff = Un.added_diff(b, a)
        return diff
    else:
        return "WARNING"

N, Q = map(int, input().split())
Un = WeightedUnionFind(N+1)
ans = []
for _ in range(Q):
    s, *l = input().split()
    if s == "IN":
        dealIn(list(map(int, l)))
    else:
        ret = compare(list(map(int, l)))
        ans.append(ret)
if ans:
    print("\n".join(map(str, ans)))