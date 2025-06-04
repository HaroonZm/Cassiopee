import sys
sys.setrecursionlimit(10**7)

# 入力を受け取る
H, W = map(int, input().split())
M = [list(map(int, input().split())) for _ in range(H)]

# ディレクトリション (上下左右)
directions = [(-1,0), (1,0), (0,-1), (0,1)]

# 標高はすべて異なるので座標ごとの標高はユニーク
# (i, j) の領域の雨水の流れ先を保存するリスト
flow_to = [[[] for _ in range(W)] for __ in range(H)]

# 各区域から水が流れ落ちる先を決める
for i in range(H):
    for j in range(W):
        current_height = M[i][j]
        # 流れ落ちる先候補
        lower_neighbors = []
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < H and 0 <= nj < W:
                if M[ni][nj] < current_height:
                    lower_neighbors.append((ni, nj))
        # 流れがある区域を登録
        flow_to[i][j] = lower_neighbors

# 各区域に水が最終的に溜まる区域（標高で一意の場所）の集合を求めるメモ化再帰
# 戻り値はこの区域に降った雨水が最終的に溜まる区域群（座標の集合）
from functools import lru_cache

@lru_cache(maxsize=None)
def find_sinks(i, j):
    if not flow_to[i][j]:
        # 流れ先無し -> ここに水が溜まる（底）
        return frozenset({(i,j)})
    res = frozenset()
    # 流れる先すべての溜まり場を結合
    for ni, nj in flow_to[i][j]:
        res |= find_sinks(ni, nj)
    return res

ridge_count = 0
for i in range(H):
    for j in range(W):
        sinks = find_sinks(i, j)
        # 溜まる場所が複数ある場合は尾根
        if len(sinks) > 1:
            ridge_count += 1

print(ridge_count)