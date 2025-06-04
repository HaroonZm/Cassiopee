from collections import deque

# 操作後のインデックス変換
# 4種類の操作ごとに、30面の位置をどう入れ替えるかを定義
# 各操作は、端3つのキューブの3面ずつ(計9面)を180度回転する動作
# 30面のうち、対象面を180度回転で入れ替えるインデックスマップを作る

# 面番号の割り振り(1-based)
# ここでは0-basedに変換して管理

# 操作１～４対応配列（0-basedでの位置対応）
# 操作1 : (0,1,2)(对应第1キューブ)
# 操作2 : (3,4,5)(第2キューブ)
# 操作3 : (6,7,8)(第3キューブ)
# 操作4 : (27,28,29)(第10キューブ)
# ただし各キューブは3面ずつで、その3面を180度回転させると、色の入れ替えが起こる

# 操作で回る9面の位置リスト(0-indexed)
actions = [
    [0,1,2, 9,10,11, 18,19,20],     # 操作1の3つキューブ9面
    [3,4,5, 12,13,14, 21,22,23],    # 操作2
    [6,7,8, 15,16,17, 24,25,26],    # 操作3
    [27,28,29,  6,7,8, 3,4,5]       # 操作4
]

# 各アクションでの180度回転は、対象9面の180度回転
# 具体的には各キューブの3面のインデックスの交換
# それぞれ3つのキューブで、3面の位置を180度回転させる対応を定義
# 1個のキューブの3面の180度回転は、0->2,1->1,2->0の入れ替え

def rotate180(state, indices):
    # indicesは9個
    arr = list(state)
    # 3つのキューブに分けて、それぞれ3面の180度回転: (a,b,c) -> (c,b,a)
    for i in range(3):
        idx = indices[i*3:(i+1)*3]
        arr[idx[0]], arr[idx[2]] = arr[idx[2]], arr[idx[0]]
    return tuple(arr)

# 解完成条件
# 全ての面が同じ色で揃う 6面それぞれ3つずつの面色が一致
# 面の構成は以下 (0-based)
faces = [
    [0,1,2],       # 上面
    [9,10,11],     # 下面
    [18,19,20],    # 右前面
    [3,4,5],       # 左前面
    [21,22,23],    # 右奥面
    [12,13,14],    # 左奥面
]

def is_solved(state):
    for face in faces:
        c = state[face[0]]
        if any(state[i] != c for i in face):
            return False
    return True

def solve_puzzle(start):
    start = tuple(start)
    if is_solved(start):
        return 0
    visited = {start}
    queue = deque([(start,0)])
    while queue:
        state, depth = queue.popleft()
        if depth == 8:
            continue
        for indices in actions:
            nxt = rotate180(state, indices)
            if nxt not in visited:
                if is_solved(nxt):
                    return depth+1
                visited.add(nxt)
                queue.append((nxt, depth+1))
    return 8  # それ以上は解なしとして8を返す

N=int(input())
for _ in range(N):
    p=list(map(int,input().split()))
    print(solve_puzzle(p))