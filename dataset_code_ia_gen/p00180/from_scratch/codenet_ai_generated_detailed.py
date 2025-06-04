import sys

# Union-Find (Disjoint Set Union) データ構造の実装
class UnionFind:
    def __init__(self, n):
        # 親ノードを管理する配列。初期状態では自分自身が親。
        self.parent = list(range(n))
        # 木の高さ（ランク）を管理する配列。初期値は0。
        self.rank = [0] * n

    def find(self, x):
        # x の根を探す。経路圧縮を行う。
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # x と y の属する集合を併合する。
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            # すでに同じ集合にある
            return False
        # ランクを比較して低い方の木を高い方の下にくっつける
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1
        return True

def main():
    input = sys.stdin.readline
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            # 入力の終わり条件
            break
        edges = []
        for _ in range(m):
            a, b, cost = map(int, input().split())
            # (コスト, 都市a, 都市b) の形で記録
            edges.append((cost, a, b))
        # コストの昇順でソート
        edges.sort()

        uf = UnionFind(n)
        total_cost = 0
        for cost, a, b in edges:
            # 都市aと都市bがまだ連結していなければ、この橋を残す(維持する)
            if uf.union(a, b):
                total_cost += cost
        # 最小全域木のコストを出力
        print(total_cost)

if __name__ == '__main__':
    main()