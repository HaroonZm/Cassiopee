import sys
import math
import fractions
import itertools
from collections import deque
import copy
import bisect
import heapq

# 定数定義
MOD = float('inf')        # 無限大を表す浮動小数点数
INF = 10 ** 18 + 7        # 十分大きな値：グラフ内の距離の "無限大" を表現
input = lambda: sys.stdin.readline().strip()  # 入力の簡易化（標準入力1行をstrip付きで取る）

def warshall_floyd(d):
    """
    全点対間最短経路を求めるWarshall-Floyd (フロイド-ワーシャル) アルゴリズムを実装する。
    
    Args:
        d (list of list of int): 隣接行列。d[i][j]はノードiからjへのコスト。コストが存在しなければ "INF" など大きな値。
    
    Returns:
        list of list of int: 各ノードペア i, j 間の最小コストに更新された隣接行列
    """
    n = len(d)
    # 中間ノードi, 開始ノードl, 終点ノードk を全探索
    for i in range(n):
        for l in range(n):
            for k in range(n):
                # l->k よりも l->i->k の方がコストが小さい場合は更新
                d[l][k] = min(d[l][k], d[l][i] + d[i][k])
    return d

while True:
    # 都市同士の接続数の取得
    n = int(input())
    if n == 0:
        break   # 0なら入力終了

    # 都市間の接続情報読み取り
    abc = [list(map(int, input().split())) for _ in range(n)]  # [始点, 終点, コスト] のリスト

    # 隣接行列の初期化
    # info[i][j]: 都市iから都市jへのコスト。直接繋がれていなければ INF
    info = [[INF for _ in range(10)] for _ in range(10)]  # 最大で都市番号0~9

    # 自分自身へのコストは0
    for i in range(10):
        info[i][i] = 0

    # 与えられた辺のコスト設定 (無向グラフ)
    for edge in abc:
        src, dest, cost = edge
        info[src][dest] = cost
        info[dest][src] = cost

    # 全点対間の最短コストを計算
    result = warshall_floyd(info)

    # 到達不能なペアは0に修正し合計を計算できるようにする
    for i in result:
        for l in range(len(i)):
            if i[l] == INF:
                i[l] = 0  # 到達不能

    # 各都市からの到達可能なコスト合計を求める
    ans = []
    for i in range(10):
        total = sum(result[i])
        if total != 0:  # ひとつでも繋がっている場合
            ans.append([total, i])  # [コスト合計, 都市番号] で保存

    # コスト合計が最小となる都市を探索
    ans.sort()  # コスト合計, 都市番号 の昇順
    print(ans[0][1], ans[0][0])  # 最小コスト都市番号とその合計コストを出力