import sys

# sysモジュールを使って、標準入力への低レベルアクセスを可能にする
readline = sys.stdin.buffer.readline

# 偶数なら1を、奇数なら0を返す関数
def even(n):
    # %演算子で2で割った余りを求める。0なら偶数なので1を返す
    return 1 if n % 2 == 0 else 0

# readline()で一行読み取って、それをsplitで空白区切りにし、mapでint型に変換してn, m, fに割り当てる
n, m, f = map(int, readline().split())
"""
n頂点m辺の重み付き有向グラフに流量fを流したい。
コストの最小値を出力せよ。
但しsource = 0, sink = n-1とし、
そもそも流量f流せるだけcapacityがない場合は-1を出力せよ。
"""

# 最小費用流(minimum cost flow)を扱うクラスを定義する
class MinCostFlow:
    # クラスのインスタンス生成時に呼ばれる初期化メソッド
    # n: グラフの頂点数
    def __init__(self, n):
        self.n = n  # グラフの頂点数を属性として保持
        # n個の空リストを各頂点の初期化用に用意。G[v]は頂点vから出ている辺のリストとなる
        self.G = [[] for i in range(n)]

    # グラフに辺（エッジ）を追加するメソッド
    # f: 始点, t: 終点, cap: 容量, cost: 単位容量ごとのコスト
    def addEdge(self, f, t, cap, cost):
        # 辺の情報をリストで格納：[to, cap, cost, rev]
        # revは逆辺のインデックスを指す
        self.G[f].append([t, cap, cost, len(self.G[t])])
        # 逆向きの辺も追加。初期容量は0、コストは逆なので-cost
        self.G[t].append([f, 0, -cost, len(self.G[f]) - 1])

    # 最小費用流を計算するメソッド
    # s: ソース頂点番号, t: シンク頂点番号, f: 流したい流量
    def minCostFlow(self, s, t, f):
        n = self.n  # 頂点数
        G = self.G  # 辺リスト
        # prevv: 各頂点への直前の頂点番号を保存
        prevv = [0] * n
        # preve: 直前の辺（インデックス）を保存
        preve = [0] * n
        # 非常に大きな数値で無限大INFを表現。パスが見つからない時に使う
        INF = 10 ** 18

        res = 0  # コストの合計を保持する変数。最終的な答えとなる

        # 流すべき流量fが残っている限りループ
        while f:
            # 各頂点までの最短コスト（距離）を格納するリスト。最初は全て無限大
            dist = [INF] * n
            # 始点の距離は0
            dist[s] = 0
            # 更新フラグ：新たな短縮パスを見つけたかどうか
            update = 1

            # ベルマンフォード法を用いた最短経路探索
            while update:
                update = 0  # 一旦更新フラグを落とす
                # 各頂点vについて
                for v in range(n):
                    # まだ到達していない頂点はスキップ
                    if dist[v] == INF:
                        continue
                    gv = G[v]  # 頂点vから出る全ての辺のリスト
                    # 頂点vから出る全ての辺を順に調べる
                    for i in range(len(gv)):
                        to, cap, cost, rev = gv[i]
                        # cap > 0なら残容量がある・dist経由で今より短縮されれば更新
                        if cap > 0 and dist[v] + cost < dist[to]:
                            dist[to] = dist[v] + cost  # コストを更新
                            prevv[to] = v  # toへ来る直前の頂点を記録
                            preve[to] = i  # 使った辺番号（インデックス）を記録
                            update = 1  # 更新フラグON
            # sink頂点まで到達不可（距離INF）なら、容量不足なので-1を返す
            if dist[t] == INF:
                return -1

            # 見つかったパスで実際に流せる最小容量dを計算
            d = f  # dは残り流量fと現在経路上の残容量との最小値
            v = t  # 最後（シンク）からソースに遡る
            while v != s:
                # prevv[v]は一つ前の頂点、preve[v]はそのedge番号
                # G[prevv[v]][preve[v]][1]が辺の残容量
                d = min(d, G[prevv[v]][preve[v]][1])
                v = prevv[v]
            # この経路で流す分だけ残量を減らす
            f -= d
            # 経路全体の単位コストをdist[t]にまとめて持っている
            res += d * dist[t]  # 合計コストに加算

            # 経路上の残容量を実際に更新。逆辺側も増やす（フロー保存則のため）
            v = t
            while v != s:
                e = G[prevv[v]][preve[v]]  # 現在の辺データ
                e[1] -= d  # 順向きの容量をd分減らす
                # 逆方向の辺（rev）がどこにつながっているか
                G[v][e[3]][1] += d  # 逆方向（戻り方向）の容量をd分増やす
                v = prevv[v]  # 一つ前の頂点へ

        # 全ての流量を流しきったら合計コストresを返す
        return res

# MinCostFlowのインスタンスをn頂点で作る
MCF = MinCostFlow(n)

# m本の辺について、1本ずつ標準入力からデータを読み込んでグラフに追加する
for i in range(m):
    # 辺の始点u, 終点v, 容量cap, コストcostを順に読み込む
    u, v, cap, cost = map(int, readline().split())
    # グラフにこの辺を加える
    MCF.addEdge(u, v, cap, cost)

# ソース(0)からシンク(n-1)まで、fの流量を流すときの最小コストを計算し出力
print(MCF.minCostFlow(0, n - 1, f))