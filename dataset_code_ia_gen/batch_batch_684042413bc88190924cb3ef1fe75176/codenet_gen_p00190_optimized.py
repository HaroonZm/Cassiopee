from collections import deque

# 盤面の行ごとのマスのインデックス (0-12)
# 入力の構造に対応させるために、行ごとの幅を保持
row_lengths = [1, 3, 5, 3, 1]

# 各行の開始インデックス（平坦化した状態に割り当てるとき用）
# 状態は長さ13のタプルとして管理
start_indices = [0, 1, 4, 9, 12]

# 行毎にアクセスするときのマップを作成
# 実際は簡単のため、各行のすべての位置を1次元インデックスにマップしておく。
# 入力は13要素だが0を含むケースがあるため保持を工夫
# 状態はリスト長13、各要素が数字0-11のいずれか。
# 0は空白を示す。空白の数は常に2。

# 13マスの座標を定義し、各マスの隣を列挙する
# 盤面 layout:  0行目(1),1行目(3),2行目(5),3行目(3),4行目(1)
# インデックスは 0~12
# 行ごとの位置：(行,列)
positions = []
for r, length in enumerate(row_lengths):
    for c in range(length):
        positions.append( (r,c) )

pos_count = len(positions)  # 13

# 隣接マスを計算
adj = [[] for _ in range(pos_count)]

for i,(r,c) in enumerate(positions):
    for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr,nc = r+dr,c+dc
        if 0 <= nr < 5 and 0 <= nc < row_lengths[nr]:
            j = sum(row_lengths[:nr]) + nc
            adj[i].append(j)

goal = (1,2,3,4,5,6,7,8,9,10,11,0,0)  # 完成型

def input_dataset():
    lines = []
    for _ in range(5):
        line = input()
        if line == '-1':
            return None
        lines.append(line)
    # 5行を読み、13要素に詰める
    nums = []
    for idx,line in enumerate(lines):
        parts = list(map(int,line.split()))
        # 入力の行ごとの数とnumsへの追加インデックスを調整
        # row_lengths=[1,3,5,3,1]
        # 1+3+5+3+1=13
        nums.extend(parts)
    if len(nums) != 13:
        raise ValueError("Input length error")
    return tuple(nums)

def solve(start):
    if start == goal:
        return 0
    visited = set()
    visited.add(start)
    q = deque()
    q.append( (start,0) )
    while q:
        state, dist = q.popleft()
        if dist > 20:
            return "NA"
        # 空白0は2つある
        zeros = [i for i,x in enumerate(state) if x == 0]

        # 2つの空白の隣接にあるタイルは動かせる
        # 1ステップは1マスの移動なので、0と隣接するカードを入れ替えて1ステップとする
        moves = set()
        for z in zeros:
            for nb in adj[z]:
                if state[nb] != 0:
                    moves.add( (nb,z) )  # nbのタイルをz(空白)へ動かす

        for nb,z in moves:
            lst = list(state)
            lst[z], lst[nb] = lst[nb], lst[z]
            new_state = tuple(lst)
            if new_state == goal:
                return dist+1
            if new_state not in visited:
                visited.add(new_state)
                q.append( (new_state, dist+1) )
    return "NA"

while True:
    start = input_dataset()
    if start is None:
        break
    print(solve(start))