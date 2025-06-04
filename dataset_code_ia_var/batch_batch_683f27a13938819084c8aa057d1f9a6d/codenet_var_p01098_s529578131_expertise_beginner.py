from collections import deque

# Directions for black and white cells
db = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
dw = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def make():
    h_w = raw_input().split()
    h = int(h_w[0])
    w = int(h_w[1])
    if h == 0 and w == 0:
        return None

    # Build padded board
    board = []
    board.append("." * (w + 2))
    for i in range(h):
        row = raw_input()
        board.append("." + row + ".")
    board.append("." * (w + 2))

    h += 2
    w += 2

    used = []
    for i in range(h):
        used.append([0] * w)

    group = [None]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if used[i][j]:
                continue
            cnt += 1
            c = board[i][j]
            if c == ".":
                dirs = dw
            else:
                dirs = db
            stack = []
            stack.append((j, i))
            used[i][j] = cnt
            q = deque()
            q.append((j, i))
            while q:
                cx, cy = q.popleft()
                for dx, dy in dirs:
                    nx = cx + dx
                    ny = cy + dy
                    if 0 <= nx < w and 0 <= ny < h:
                        if used[ny][nx] == 0 and board[ny][nx] == c:
                            used[ny][nx] = cnt
                            stack.append((nx, ny))
                            q.append((nx, ny))
            group.append(stack)

    visited = set()

    def dfs(num):
        nodes = []
        for x, y in group[num]:
            for dx, dy in dw:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < w and 0 <= ny < h:
                    gnum = used[ny][nx]
                    if gnum not in visited:
                        visited.add(gnum)
                        nodes.append(dfs(gnum))
        nodes.sort()
        return nodes

    visited.add(1)
    return dfs(1)


while True:
    A = make()
    if A is None:
        break
    B = make()
    if A == B:
        print("yes")
    else:
        print("no")