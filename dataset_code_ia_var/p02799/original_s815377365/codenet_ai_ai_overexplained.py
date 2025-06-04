class UnionFind:
    # クラスUnionFindの定義。これは、素集合データ構造（Disjoint Set Union, DSU）とも呼ばれる。
    def __init__(self, n):
        # コンストラクタ。n: 要素の個数。
        # 各要素が属する集合を管理するために、親ノードを保持するリストを作成。
        # 最初は各要素が自分自身を親とする（独立した集合）。
        self.parent = list(range(n))  # [0,1,2,...,n-1]となるリスト。親を管理。
        # 各集合の要素数を管理するリストを作成。初期値はすべて1。
        self.size = [1] * n  # 各要素1個なので1で初期化

    def root(self, x):
        # 要素xが属する集合の根（親）を返す
        # 跡置き圧縮（パス圧縮）によって経路上の全ノードの親を根に直すことで効率化
        while self.parent[x] != x:  # xがまだ根でない場合繰り返す
            self.parent[x] = self.parent[self.parent[x]]  # 親の親を直親に設定（2段階まとめて進める）
            x = self.parent[x]  # xを親に進める
        return x  # 根ノードを返す

    def merge(self, x, y):
        # xとyが属する集合を１つにまとめる
        x, y = self.root(x), self.root(y)  # それぞれの根を求める
        if x == y:
            return False  # すでに同じ集合の場合は何もしない（マージできないのでFalseを返す）
        # 要素数が大きい集合に小さい集合をつなぐようにする（ランク付き合併：効率化のため）
        if self.size[x] < self.size[y]:
            x, y = y, x  # xを大きい集合にする（変数を入れ替える）
        self.size[x] += self.size[y]  # x側の集合にy側の要素数を加える
        self.parent[y] = x  # yの根をxに付け替える
        return True  # マージできたのでTrue

    def issame(self, x, y):
        # xとyが同じ集合かどうか（根が同じか）をTrue/Falseで返す
        return self.root(x) == self.root(y)

    def getsize(self, x):
        # xが所属する集合の要素数を返す。根のサイズを見る。
        return self.size[self.root(x)]

############################################################################
############################################################################

# ライブラリのインポート。標準入力、再帰上限の設定。
import sys
# Pythonではデフォルトで再帰の上限が低いので、再帰関数を多用する場合は増やす必要がある
sys.setrecursionlimit(10 ** 6)  # 再帰呼び出し可能な回数を100万回に設定

# 標準入力を高速で行うための設定
readline = sys.stdin.readline  # １行ずつ標準入力を読み込む関数を用意
read = sys.stdin.read  # ファイル全体もしくは標準入力全体を読み込む関数

# 1行目を読み取り、空白で区切って整数（ノード数n、辺の数m）に変換
n, m = [int(i) for i in readline().split()]

# 2行目を読み取り、空白で区切って整数（各ノードのコストd）に変換
d = [int(i) for i in readline().split()]

# 各ノードに接続する辺のリスト（隣接リスト）を初期化。空リストをn個作るので [[] for _ in range(n)]
g = [[] for _ in range(n)]

# 入力された残りすべての整数をaとして読み取る。これは各辺（エッジ）についての情報。
a = map(int, read().split())  # ここではエッジリストとしてaを使っている

# a（エッジリスト）から2つずつ（u,v）ペアを取り、辺として扱う
for i, (u, v) in enumerate(zip(a, a)):
    # 入力が1-indexedのため、-1して0-indexedに変換
    u -= 1
    v -= 1
    # 辺iをノードu, vそれぞれの隣接リストに追加
    g[u].append((v, i))  # uからvへの辺（i番目）を登録
    g[v].append((u, i))  # vからuへの辺（i番目）も登録（無向グラフ）

# 無限大に相当する大きな値。コストの初期値として使う
INF = 10 ** 9

# 答えとなる辺ごとのコストをINFで初期化。ans[i]はi番目の辺に割り当てたコスト
ans = [INF] * m

# UnionFind木を2n+1ノードで初期化。二部グラフにするため2n個に加え超頂点1個
UF = UnionFind(2 * n + 1)  # 0..n-1, n..2n-1, 2n（超頂点）

# ノードのコストとノード番号のペアを作る（dd[i]=(d[i],i)）
dd = [(c, i) for i, c in enumerate(d)]

# ノードのコストが小さい順にソート
dd.sort()  # （c,idx）のcの昇順になる

"""
アルゴリズムの説明
最小コストから順に、次のことを行う（貪欲法的な処理）：
    そのコスト以下の点があれば、その点同士を繋いでbreakする。
    なければ失敗（-1出力して終了）。
"""

# ddはコスト昇順。各ノード（idx）について処理を行う
for c, idx in dd:
    # idxの隣接ノード(v,j)について列挙。jは辺の番号、vは対するノード
    for (v, j) in g[idx]:
        # 隣接ノードvのコストが現在のc以下か判定
        if d[v] <= c:
            # 二部グラフなので、vをidx+nに、v+nをidxにつなぐ
            UF.merge(v, idx + n)
            UF.merge(v + n, idx)
            # 辺jにこのコストcを割り当てる
            ans[j] = c
            break  # 処理したので次へ進む
    else:
        # breakしなかった（どれも条件を満たさなかった）時は、答え無し
        print(-1)  # -1出力して
        exit()     # 終了する

# 超頂点（仮想的な頂点番号2n）を使って、二部グラフのグループ分け
s = []  # 各ノードの色分け("W"または"B")を格納するリスト
T = 2 * n  # 超頂点の番号を定義

for i in range(n):
    # iが超頂点Tと同じグループか判定
    if UF.issame(T, i):
        s.append("W")  # 超頂点と同じグループなら"W"に分ける
    elif UF.issame(T, i + n):
        s.append("B")  # n番目以降の二部側なら"B"に分ける
    else:
        # どちらにも属していない場合は、"W"にして超頂点とつなぐ
        s.append("W")
        UF.merge(T, i)

# 機械的にノードの色分けを出力
print("".join(s))
# 辺ごとのコストを改行区切りで出力
print(*ans, sep="\n")