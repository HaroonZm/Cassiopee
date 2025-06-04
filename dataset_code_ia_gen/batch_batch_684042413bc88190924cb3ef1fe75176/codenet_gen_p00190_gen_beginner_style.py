from collections import deque

# 11パズルの形状（各行のマス数）
shape = [1, 3, 5, 3, 1]

# 座標リストを1次元インデックスに変換するための累積和
pos_index = []
index = 0
for length in shape:
    pos_index.append([index + i for i in range(length)])
    index += length
total_positions = index  # 13

# 隣接関係を作る
# 各マスについて上下左右に隣接するマスのインデックスを記録する
adj = [[] for _ in range(total_positions)]
for i, length in enumerate(shape):
    for j in range(length):
        current = pos_index[i][j]
        # 上の行に同じ列、または左隣の列（存在すれば）
        if i > 0:
            upper_line = shape[i-1]
            # 上の行のjかj-1が隣接？
            for dj in [j, j-1]:
                if 0 <= dj < upper_line:
                    adj[current].append(pos_index[i-1][dj])
        # 下の行に同様に
        if i < len(shape)-1:
            lower_line = shape[i+1]
            for dj in [j, j-1]:
                if 0 <= dj < lower_line:
                    adj[current].append(pos_index[i+1][dj])
        # 同じ行左
        if j > 0:
            adj[current].append(pos_index[i][j-1])
        # 同じ行右
        if j < length-1:
            adj[current].append(pos_index[i][j+1])

def read_dataset():
    board = []
    for line_idx in range(13):
        line = input()
        if line == '-1':
            return None
        nums = list(map(int, line.split()))
        board.append(nums)
    return board

def flatten_board(board):
    # boardは13行。shapeの列数に対応。0が空きのカード。
    flat = [0]*total_positions
    pos = 0
    idx = 0
    for i, length in enumerate(shape):
        line = board[i]
        for j in range(length):
            flat[idx] = line[j]
            idx += 1
    return tuple(flat)

def find_zeros(state):
    return [i for i, v in enumerate(state) if v == 0]

def solve(start):
    # ゴールは 1~11のカードが左から上から順に並ぶ形、空きは最後2つの位置
    # 13個の場所があり、11枚の数字+2空き(0)
    goal_nums = [1,2,3,4,5,6,7,8,9,10,11]
    goal = []
    # shape == [1,3,5,3,1] で合計13
    # 左上から順にカード1~11を埋めて残り2は0
    for i in range(11):
        goal.append(i+1)
    goal.append(0)
    goal.append(0)
    goal = tuple(goal)

    if start == goal:
        return 0

    visited = set()
    visited.add(start)
    queue = deque()
    queue.append((start,0))

    while queue:
        state, steps = queue.popleft()
        if steps > 20:
            break

        # 空きを探す
        zeros = [i for i, v in enumerate(state) if v == 0]

        # 空きは2箇所
        zero1 = zeros[0]
        zero2 = zeros[1]

        # 空きに隣接するカードを動かすことができる
        # 移動は隣接するカードが空きの位置に1つずつ動く
        # つまり、2つの空きの隣接マスの中でカードを動かす動きを作る

        # 空きに隣接するカードを求める（0でないもの）
        moves = []
        for zero_pos in zeros:
            for nei in adj[zero_pos]:
                if state[nei] != 0:
                    # stateのneiのカードをzero_posに移動する動き
                    moves.append((nei, zero_pos))  # (動かすカードの位置, 空き位置)

        # moves から次の状態を作る
        for frm, to in moves:
            # カード一枚をzeroまで動かす＝1ステップ
            # stateをリスト化して交換
            new_state = list(state)
            new_state[to], new_state[frm] = new_state[frm], new_state[to]
            new_state = tuple(new_state)
            if new_state == goal:
                return steps + 1
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, steps + 1))

    return "NA"

while True:
    dataset = []
    first_line = input()
    if first_line == '-1':
        break
    dataset.append(list(map(int, first_line.split())))
    for _ in range(12):
        line = input()
        dataset.append(list(map(int, line.split())))
    start_state = flatten_board(dataset)
    ans = solve(start_state)
    print(ans)