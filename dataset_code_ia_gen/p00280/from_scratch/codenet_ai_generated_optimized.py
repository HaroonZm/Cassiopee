from collections import deque

j, y = map(int, input().split())

# 判定関数：現在のスコアが試合終了状態かどうか
def is_game_over(j, y):
    if j >= 5 or y >= 5:
        if (j <= 3 and j == 5 and y <= 3) or (y <= 3 and y == 5 and j <= 3):
            return True
    if j == 6 and y == 4:
        return True
    if y == 6 and j == 4:
        return True
    if j == 4 and y == 4:
        return False
    # 4-4以降の判断
    if j >= 4 and y >= 4:
        diff = abs(j - y)
        if diff == 2:
            return True
        if diff == 1:
            return False
    return False

# 4-4特有の条件判定
def next_states(j, y):
    states = []
    # 試合終了なら戻らない
    if is_game_over(j, y):
        return states
    # 4-4以降のルール
    if j >= 4 and y >= 4:
        # 引き分け条件回避のため特別扱い
        # from 4-4
        if j == 4 and y == 4:
            # Aとった場合5-4、Bとった場合4-5
            states.append((j+1, y, 'A'))
            states.append((j, y+1, 'B'))
            return states
        # それ以降
        diff = j - y
        if diff == 1:  # jが1点リード
            # jがもう1点取れば終了
            if j +1 == 6 and y == 4:
                states.append((j+1, y, 'A'))
            else:
                states.append((j+1, y, 'A'))
                states.append((j, y+1, 'B'))
        elif diff == -1:  # yが1点リード
            if y +1 == 6 and j == 4:
                states.append((j, y+1, 'B'))
            else:
                states.append((j+1, y, 'A'))
                states.append((j, y+1, 'B'))
        else:
            # 引き分けかどうか判定→終わり
            # 4-4で双方が１点ずつとったとき(5-5)は引き分け
            # つまり5-5で終了
            if j == 5 and y == 5:
                return []
            # それ以外は両方加点可能（理論上ないが念のため）
            states.append((j+1, y, 'A'))
            states.append((j, y+1, 'B'))
        return states

    # 通常ルール
    if j <= 3 and y <= 3:
        if not is_game_over(j+1, y):
            states.append((j+1, y, 'A'))
        elif (j+1) == 5 and y <= 3:
            states.append((j+1, y, 'A'))
        if not is_game_over(j, y+1):
            states.append((j, y+1, 'B'))
        elif (y+1) == 5 and j <= 3:
            states.append((j, y+1, 'B'))
        # 追加で終わるケース
        if is_game_over(j+1, y):
            states.append((j+1, y, 'A'))
        if is_game_over(j, y+1):
            states.append((j, y+1, 'B'))
        return states
    # 4未満でも片方が4以上の不正状態はないので
    # 通常追加
    states.append((j+1, y, 'A'))
    states.append((j, y+1, 'B'))
    return states

goal = (j, y)
paths = []

memo = dict()
def dfs(cj, cy, path):
    if (cj, cy) == (0,0):
        paths.append(path[::-1])
        return
    if (cj, cy) in memo:
        for p in memo[(cj, cy)]:
            paths.append((path + p)[::-1])
        return
    res = []
    # 左から来た状態を考える
    if cj > 0:
        pj, py = cj-1, cy
        # ここからの遷移でAで現状態になっているか
        if (pj, py, 'A') in prev[(cj, cy)]:
            dfs(pj, py, path+'A')
    if cy > 0:
        pj, py = cj, cy-1
        if (pj, py, 'B') in prev[(cj, cy)]:
            dfs(pj, py, path+'B')

# 逆方向で前状態を記録
# forward探索でグラフ構築し、逆に探索して列挙
max_score = 7
prev = dict()
for i in range(max_score):
    for k in range(max_score):
        prev[(i,k)] = []

queue = deque()
queue.append((0,0))
visited = set()
visited.add((0,0))

while queue:
    cj, cy = queue.popleft()
    for nj, ny, c in next_states(cj, cy):
        if nj > 6 or ny > 6:
            continue
        if (nj, ny) not in visited:
            visited.add((nj, ny))
            queue.append((nj, ny))
        prev[(nj, ny)].append((cj, cy, c))

# 与えられた得点が探索可能かチェック
if (j,y) not in visited:
    exit()

ans = []
def backtrack(x,y,path):
    if (x,y) == (0,0):
        ans.append(path[::-1])
        return
    for pj, py, c in sorted(prev[(x,y)], key=lambda a: a[2], reverse=True):
        backtrack(pj, py, path+c)

backtrack(j,y,'')

ans.sort()
for a in ans:
    print(a)