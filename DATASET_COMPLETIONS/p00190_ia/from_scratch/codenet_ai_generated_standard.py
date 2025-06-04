from collections import deque

# パズルの形状（各行の要素数）
shape = [1,3,5,3,1]
# 各位置のインデックスを1次元化（行と列）
pos_map = []
for r, cnt in enumerate(shape):
    for c in range(cnt):
        pos_map.append((r,c))
# 総マス目数
N = len(pos_map)  # 13

# 隣接リスト作成
adj = [[] for _ in range(N)]
idx_map = [[-1]*5 for _ in range(5)]  # 最大5列まで、行は5行ぐらい確保
for i,(r,c) in enumerate(pos_map):
    idx_map[r][c] = i
for i,(r,c) in enumerate(pos_map):
    # 左右上下の隣接（斜めなし）
    for dr,dc in [(0,-1),(0,1),(-1,0),(1,0)]:
        nr,nc = r+dr, c+dc
        if 0 <= nr < 5 and 0 <= nc < 5:
            ni = idx_map[nr][nc]
            if ni != -1:
                adj[i].append(ni)

# 完成形（最終目標）を定義
# 図2の完成形: 1~11が決まった位置に入る
# 問題文での完成形は以下の図2と同じ（問題例の図より推測）
# 完成形の数字配置
goal_nums = [0]*N
goal_line = [
  [1],
  [2,3,4],
  [5,6,7,8,9],
  [10,11,0],
  [0]
]
idx = 0
for r, line in enumerate(goal_line):
    for c, v in enumerate(line):
        goal_nums[idx] = v
        idx += 1
goal_state = tuple(goal_nums)

def solvable(state):
    # 11パズルのな特別な判定は不要。問題中の制限なしに最短探索を行う
    return True

def bfs(start):
    # start: tuple(13要素)
    if start == goal_state:
        return 0
    visited = {start:0}
    q = deque([start])
    while q:
        state = q.popleft()
        dist = visited[state]
        if dist > 20:
            return "NA"
        # 空きスペース2つを探す
        zeros = [i for i,v in enumerate(state) if v==0]
        # それぞれ隣接するカードを動かせる
        # 空きスペースのいずれかに隣接する位置のカードをスライドさせ0と入れ替える
        neighbors_pos = set()
        for z in zeros:
            for nb in adj[z]:
                # nbはカードの位置
                neighbors_pos.add(nb)
        for nb in neighbors_pos:
            # nbのカードを空きスペースに動かすステップ数は1ステップ
            # 入れ替え先は0の位置のうち隣接しているもの
            for z in zeros:
                if z in adj[nb]:
                    # nbのカードをzに移動：入れ替え
                    l = list(state)
                    l[z], l[nb] = l[nb], l[z]
                    new_state = tuple(l)
                    if new_state == goal_state:
                        return dist+1
                    if new_state not in visited:
                        visited[new_state] = dist+1
                        q.append(new_state)
    return "NA"

import sys
input=sys.stdin.readline

while True:
    lines = []
    for _ in range(13):
        line = input()
        if line == '':
            break
        if line.strip() == '-1':
            print()
            exit()
        lines.append(line.strip())
    if len(lines)<13:
        break
    nums=[]
    for l in lines:
        nums.extend(map(int,l.split()))
    start = tuple(nums)
    ans = bfs(start)
    print(ans)