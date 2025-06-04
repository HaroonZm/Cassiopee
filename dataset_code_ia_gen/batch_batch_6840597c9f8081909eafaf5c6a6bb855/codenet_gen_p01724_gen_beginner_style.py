board = [list(input()) for _ in range(19)]
h, w = 19, 15

# 探索用の方向ベクトル(8方向)
dirs = [(-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)]

# 白石の位置を探す
for i in range(h):
    for j in range(w):
        if board[i][j] == 'O':
            start = (i, j)

from collections import deque

def in_board(x, y):
    return 0 <= x < h and 0 <= y < w

def can_jump(sx, sy, dx, dy, stones):
    # (dx, dy) はジャンプ方向の単位ベクトル
    x, y = sx + dx, sy + dy
    if not in_board(x, y):
        return None
    if (x, y) not in stones:
        return None
    # 黒石が連続してる部分を飛び越え、次の位置を探す
    while (x, y) in stones:
        x += dx
        y += dy
        if x >= h:
            break
    # 飛び越え先は碁盤内またはゴール地点（h以上はゴール）
    if x < h and y >= 0 and y < w:
        if (x, y) in stones:
            return None
        else:
            return (x, y)
    elif x >= h:
        return (x, y)  # ゴール判定用にh以上は許可
    else:
        return None

def serialize(stone_set, pos):
    return (pos, tuple(sorted(stone_set)))

# 石の位置集合
stones = set()
for i in range(h):
    for j in range(w):
        if board[i][j] == 'X':
            stones.add((i,j))

# 幅優先探索
from collections import deque
queue = deque()
visited = set()

queue.append( (start, stones, 0) )
visited.add(serialize(stones, start))

ans = -1

while queue:
    pos, stones, dist = queue.popleft()
    x0, y0 = pos
    # ゴール判定：x >= h ならゴール
    if x0 >= h:
        ans = dist
        break
    # 1回以上ジャンプできる必要があるのでdist=0のときはゴール判定しない
    if dist == 0:
        pass

    for dx, dy in dirs:
        res = can_jump(x0, y0, dx, dy, stones)
        if res is None:
            continue
        nx, ny = res
        # jumpしたら飛び越した黒石は取り除く
        # 飛び越した黒石群を見つける
        tx, ty = x0 + dx, y0 + dy
        removed = []
        while (tx, ty) in stones:
            removed.append((tx, ty))
            tx += dx
            ty += dy

        new_stones = stones - set(removed)
        # ジャンプ先に黒石があってはいけない
        if (nx, ny) in new_stones:
            continue
        # 新しい状態
        state = serialize(new_stones, (nx, ny))
        if state not in visited:
            visited.add(state)
            queue.append( ((nx, ny), new_stones, dist + 1) )

print(ans)