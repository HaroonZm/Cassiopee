# Union-Find (Disjoint Set Union) データ構造を使って連結成分（市）を管理します。
# 各村は最初は自分自身が代表者（親）で、それぞれ独立しています。
# M 組の合併情報により、村同士を一つの集合にまとめます。
# 最終的に、グループ（市）の数を数え、それを元の村の数と比較して差の絶対値を出力します。

class UnionFind:
    def __init__(self, n):
        # 親ノードを自分自身に初期化（各ノードは独立）
        self.parent = list(range(n))
        # 各集合のサイズ（代表者のみに有効）
        self.size = [1] * n

    def find(self, x):
        # 経路圧縮を用いた親の検索
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        # x, y を同じ集合にまとめる
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False  # すでに同じ集合
        # サイズが大きい方を親にする（ランクによる最適化）
        if self.size[x_root] < self.size[y_root]:
            x_root, y_root = y_root, x_root
        self.parent[y_root] = x_root
        self.size[x_root] += self.size[y_root]
        return True

def main():
    import sys
    input = sys.stdin.readline

    # 村の数 N と合併情報の数 M
    N, M = map(int, input().split())

    uf = UnionFind(N)

    for _ in range(M):
        a, b = map(int, input().split())
        # 0-indexに変換して unite
        uf.unite(a - 1, b - 1)

    # 代表者の数 = 市の数
    # 代表者は自身が親であるノード
    city_count = sum(1 for i in range(N) if uf.find(i) == i)

    # 結果は |村の数 - 市の数|
    result = abs(N - city_count)
    print(result)

if __name__ == "__main__":
    main()