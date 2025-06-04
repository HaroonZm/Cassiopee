#!/usr/bin/env python3

# インポートするモジュールの宣言
import sys        # sysモジュールはシステム特有のパラメータや関数を扱うためにインポートされる
import heapq      # heapqモジュールはヒープキューアルゴリズム(優先度付きキュー)のための関数を提供する
import functools  # functoolsモジュールは高階関数や関数オブジェクト向けツールをまとめたモジュール
# 今回はfunctoolsを使用していないが元のコードにあったためそのまま残している

# 無限大を表現するため、float("inf")を使用してINFという名前で定義
INF = float("inf")  # INFは無限大を表しており、距離などの比較時に使われる

# 無向グラフを想定したクラス定義
class Graph(object):
    # コンストラクタ(初期化メソッド)
    def __init__(self, N):
        # グラフに含まれるノード(頂点)の個数をNとしてメンバ変数に格納
        self.N = N
        # 隣接リスト(各ノードについて接続されているノードと重みのペアを管理)
        # [[] for _ in range(N)] でN個の空リストを生成し、それぞれの頂点ごとにエッジリストを割り当てる
        self.E = [[] for _ in range(N)]

    # 無向グラフなのでadd_edgeで両方向にエッジを追加
    def add_edge(self, s, t, w=1):
        # sからtへのエッジ(重みw)を追加
        self.E[s].append((t, w))
        # 無向グラフなのでtからsへのエッジ(重みw)も追加
        self.E[t].append((s, w))

# ワーシャル-フロイド(全点対間最短距離)アルゴリズムの実装
def Warshall_Floyd(g: Graph):
    # グラフgに含まれるノード数
    N = g.N
    # dist[i][j]はノードiからノードjへの最短距離。初期状態では全て無限大。
    dist = [[INF]*N for _ in range(N)]
    # グラフgの隣接リストから、直接つながっているノードについてその重みをdistに設定
    for from_, toweights in enumerate(g.E):
        # from_は現在の頂点、towweightsは(from_,と接続した頂点,重み)のリスト
        for to_, w in toweights:
            # from_からto_への距離はw
            dist[from_][to_] = w
    # 三重ループでワーシャル-フロイド法を適用
    for k in range(N):            # 中継ノードkを全て試す
        for i in range(N):        # 始点i
            for j in range(N):    # 終点j
                # dist[i][j]よりも、i→k→j経由の方が距離が短い場合は更新する
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    # 最短距離テーブルを返す
    return dist

# 実際の問題を解く解決関数
def solve(N: int,
          M: int,
          L: int,
          A: "List[int]",
          B: "List[int]",
          C: "List[int]",
          Q: int,
          s: "List[int]",
          t: "List[int]"):
    # N: ノード数
    # M: エッジ数
    # L: 一度に走行可能距離
    # A,B,C: 各エッジの情報（AとBはノード、Cは重み）
    # Q: クエリ数
    # s,t: クエリの始点と終点

    # グラフのインスタンスを作成（最初の初期状態グラフ）
    g = Graph(N)
    # 入力エッジ情報を使ってエッジを追加
    for i in range(M):
        # 問題文で1-indexedならば0-indexedに変換(A[i]-1, B[i]-1)
        g.add_edge(A[i]-1, B[i]-1, C[i])
    # ワーシャル-フロイド法で全頂点間の最短距離を計算
    dist = Warshall_Floyd(g)

    # 新しくグラフを生成し直す（各エッジの重みは1にして、距離L以下ならば有向辺が張れるとみなす）
    g = Graph(N)
    for i in range(N):
        # j>i すなわちi < jペアでのみ考慮->重複回避と効率化のため
        for j in range(i+1, N):
            # iとj間の最短距離がL以下ならば（スタンドの給油だけで移動できる）、重み1の辺を張る
            if dist[i][j] <= L:
                g.add_edge(i, j, 1)
    # 「1回の給油でたどり着けるなら辺を張る」という仮想グラフで、再びワーシャル-フロイド法
    dist = Warshall_Floyd(g)

    # 各クエリについて「何回給油すれば良いか」を出力
    for i in range(Q):
        # s[i],t[i]への経路の長さ（st間の辺の個数）から1引いたものが必要な給油回数
        ans = dist[s[i]-1][t[i]-1] - 1  # -1は「出発時には給油不要」のため
        # 到達不能（無限大）の場合は-1を出力
        if ans == INF:
            print(-1)
        else:
            print(ans)

    # returnは特に意味はない（空リターンしているだけ）
    return

# メイン関数（実行のエントリポイント）
def main():

    # 入力ストリームからトークン（一つ一つの入力値）をyieldで順に返すイテレータの定義
    def iterate_tokens():
        # sys.stdin（標準入力）から一行ずつ取得する
        for line in sys.stdin:
            # 取得した文字列を空白で分割し、それぞれの単語（入力値）をyieldで返す
            for word in line.split():
                yield word
    # イテレータのインスタンスを作成（これから入力を順次取得していく）
    tokens = iterate_tokens()

    # 以下、入力を1つずつ読み込んで、int型で対応変数に格納していく
    N = int(next(tokens))  # 頂点数
    M = int(next(tokens))  # エッジ数
    L = int(next(tokens))  # 一回の給油あたりの最大距離
    # 長さMのリストを初期化
    A = [int()] * (M)  # A: 各エッジの始点
    B = [int()] * (M)  # B: 各エッジの終点
    C = [int()] * (M)  # C: 各エッジの重み
    for i in range(M):
        # エッジ情報を読み込む
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    Q = int(next(tokens))  # クエリの数
    # クエリに対応する始点・終点リストを初期化
    s = [int()] * (Q)
    t = [int()] * (Q)
    for i in range(Q):
        # クエリs[i], t[i]を読み込む
        s[i] = int(next(tokens))
        t[i] = int(next(tokens))
    # 以上で入力全て読み込み完了したので、問題を解く
    solve(N, M, L, A, B, C, Q, s, t)

# Pythonスクリプトが直接実行されたときだけmain()を呼び出す
if __name__ == '__main__':
    main()