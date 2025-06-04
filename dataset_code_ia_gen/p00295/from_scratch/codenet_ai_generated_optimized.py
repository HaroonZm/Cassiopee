from collections import deque

# 操作定義：4種類の操作によるインデックス変換
# 各操作は端の3つのキューブ(各キューブ3面,計9面)を180度回転させる
# インデックスは0始まりで30個の面を表す

# 操作による面の入れ替え（180度回転）の定義
# 各操作の対象となる9面の番号配列と、その中での交換ルールを示す
ops = [
    [0,1,2, 9,10,11, 18,19,20],      # 左端3キューブの回転
    [6,7,8, 15,16,17, 24,25,26],     # 右端3キューブの回転
    [0,1,2, 3,4,5, 6,7,8],           # 上3キューブの回転
    [18,19,20, 21,22,23, 24,25,26],  # 下3キューブの回転
]

# 180度回転は、その9面の順序を逆にすることで実現できる
# 位置の入れ替えを返す変換マップを作成
def make_move_map(indices):
    m = list(range(30))
    for i, idx in enumerate(indices):
        m[idx] = indices[-1 - i]
    return m

move_maps = [make_move_map(op) for op in ops]

def apply_move(state, move_map):
    # state: tuple(30), move_map: list(30)
    return tuple(state[move_map[i]] for i in range(30))

# ゴール状態は全6面が揃っている状態、各キューブ3面ずつ3個、合計9キューブ
# キューブの行列配置は固定なので、6面のどの面の色がどのキューブのどの面かは固定
# 入力で与えられた状態の面の色からゴールを判定：
# 各キューブの3面は固定位置で与えられているので、それぞれの面が揃っていることを確認する
# 具体的には、6つの面ごとに各3つのキューブの3面で同じ色
# 問題文の初期状態色配置の約束はないが、揃っている条件は面の各3つのキューブの3面の色が同じであること

# キューブごとの面のインデックス
cubes = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [9,10,11],
    [12,13,14],
    [15,16,17],
    [18,19,20],
    [21,22,23],
    [24,25,26]
]

# 6面それぞれの色は、各面に属する3つのキューブの面で決まる
# 問題文の図や色分布から各面の面に対するインデックスを確定するのは困難なので、
# 入力が揃っている状態なら、全キューブの3面が同じ色である必要があることから、
# 盤面が「揃っている」= 各キューブの3面が一致している状態をゴールとみなすことにする
# 実際サンプルの解などから推測

def is_solved(state):
    # stateは長さ30のタプル
    # 各キューブの3面の色が全て同じであれば解とする
    for c in cubes:
        colors = {state[i] for i in c}
        if len(colors) != 1:
            return False
    return True

def solve(puzzle):
    start = tuple(puzzle)
    if is_solved(start):
        return 0
    visited = set([start])
    queue = deque([(start,0)])
    while queue:
        cur, depth = queue.popleft()
        if depth == 8:
            continue
        for m in move_maps:
            nxt = apply_move(cur, m)
            if nxt not in visited:
                if is_solved(nxt):
                    return depth+1
                visited.add(nxt)
                queue.append((nxt, depth+1))
    # 問題文の仮定で解けるはずなのでここには到達しないはず
    return -1

import sys
input=sys.stdin.readline

N=int(input())
for _ in range(N):
    puzzle = list(map(int,input().split()))
    print(solve(puzzle))