class UnionFind:
    """
    Union-Find (Disjoint Set Union) データ構造を実装するクラス。
    部分集合群を効率的に管理し、2 要素が同じ集合に属するかどうかなどを高速に判定できる。

    Attributes:
        parent (list): 各ノードの親ノードのインデックス。
        size (list): 各ノードが属する連結成分の要素数。
    """
    def __init__(self, n):
        """
        クラスの初期化。

        Args:
            n (int): ノード数（0 から n-1 のノードを管理）。
        """
        # 各ノードを自分自身の親に初期化
        self.parent = list(range(n))
        # 各ノードの属するグループのサイズを1に初期化
        self.size = [1] * n

    def root(self, x):
        """
        ノード x の根ノードを返す。経路圧縮を行い、木の高さを抑える。

        Args:
            x (int): 根を求めたいノードのインデックス。

        Returns:
            int: x の属する木の根ノードのインデックス。
        """
        # 根に向かって親をたどりながら経路圧縮
        while self.parent[x] != x:
            # 親の親を自分の親にする（経路圧縮）
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def merge(self, x, y):
        """
        x の属する集合と y の属する集合を1つにまとめる（併合する）。

        Args:
            x (int): マージしたい1つ目のノードのインデックス。
            y (int): マージしたい2つ目のノードのインデックス。

        Returns:
            bool: すでに同じ集合の場合は False、新たにマージした場合は True。
        """
        x_root = self.root(x)
        y_root = self.root(y)
        if x_root == y_root:
            # すでに同じグループなら何もしない
            return False
        # 常に大きいグループに小さいグループを統合
        if self.size[x_root] < self.size[y_root]:
            x_root, y_root = y_root, x_root
        # グループサイズを更新
        self.size[x_root] += self.size[y_root]
        # y_root を x_root の子とする
        self.parent[y_root] = x_root
        return True

    def issame(self, x, y):
        """
        x と y が同じ集合に属するかどうかを判定。

        Args:
            x (int): 1つ目のノードインデックス。
            y (int): 2つ目のノードインデックス。

        Returns:
            bool: 同じ集合なら True、異なる集合なら False。
        """
        return self.root(x) == self.root(y)

    def getsize(self, x):
        """
        x の属する集合の要素数を返す。

        Args:
            x (int): 要素数を知りたいノードのインデックス。

        Returns:
            int: x の属するグループのサイズ。
        """
        return self.size[self.root(x)]

############################################################################
# メイン処理部

import sys

# 再帰上限を大きく設定（深い再帰の局面に備える）
sys.setrecursionlimit(10**6)

readline = sys.stdin.readline
read = sys.stdin.read

# 入力: n（ノード数）, m（辺数）
n, m = [int(i) for i in readline().split()]

# 各ノードの「重み」情報（コストや頂点属性）
d = [int(i) for i in readline().split()]

# グラフの隣接リストをノードごとに用意
g = [[] for _ in range(n)]

# 標準入力から辺データを読み込む
a = map(int, read().split())

# 辺情報（i番目の辺が (u, v) を結ぶ）を隣接リストとして追加
for i, (u, v) in enumerate(zip(a, a)):
    u -= 1  # 0-indexed に変換
    v -= 1
    # 頂点u, v の隣接リストへ (相手ノード, 辺番号) を加える
    g[u].append((v, i))
    g[v].append((u, i))

# 無限大を表す定数
INF = 10 ** 9

# 各辺のコスト（初期値INF）: ans[i] = i番目の辺の答え（問題定義に基づく）
ans = [INF] * m

# UnionFind で 2部グラフ用に 2n+1 頂点分を用意
UF = UnionFind(2 * n + 1)

# 各ノードの (コスト, インデックス) のペアを生成し、コストが小さい順にソート
dd = [(c, i) for i, c in enumerate(d)]
dd.sort()

"""
各ステップでコストが小さい順に処理する:

・各ノードについて、隣接するノードで自分以下のコストのものがあれば、辺を連結し、探索を抜ける。
・どの隣接ノードも条件を満たさない場合は解がない（-1出力して即終了）。
"""
for c, idx in dd:
    for (v, j) in g[idx]:
        if d[v] <= c:
            # 二部グラフのため片側を n ずらして接続
            UF.merge(v, idx + n)
            UF.merge(v + n, idx)
            ans[j] = c
            break
    else:
        # 条件を満たす隣接ノードがなければ失敗
        print(-1)
        exit()

# 超頂点Tを追加し、頂点塗り分け（白黒）を判定する
s = []  # 頂点ごとに色を格納（"W"=White, "B"=Black）
T = 2 * n  # 超頂点のインデックス

for i in range(n):
    if UF.issame(T, i):
        s.append("W")
    elif UF.issame(T, i + n):
        s.append("B")
    else:
        # どちらとも未接続なら自動で白にしてTと連結
        s.append("W")
        UF.merge(T, i)

# 頂点の色、辺コストを出力
print("".join(s))
print(*ans, sep="\n")