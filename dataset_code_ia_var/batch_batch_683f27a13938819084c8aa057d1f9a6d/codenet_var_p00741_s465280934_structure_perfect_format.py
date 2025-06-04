def inputlist():
    return [int(j) for j in input().split()]

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

from collections import deque

def dfs(x, y, w, h, lis, flag):
    if lis[x][y] == 1:
        flag = 1
        lis[x][y] = 0
        stack = deque([])
        l = [x, y]
        stack.appendleft(l)
        while len(stack) != 0:
            li = stack.popleft()
            xa = li[0]
            ya = li[1]
            for i in range(8):
                nx = xa + dx[i]
                ny = ya + dy[i]
                if nx < 0 or ny < 0 or nx > h - 1 or ny > w - 1:
                    continue
                if lis[nx][ny] == 0:
                    continue
                stack.appendleft([nx, ny])
                lis[nx][ny] = 0
    if flag:
        return 1
    else:
        return 0

while True:
    w, h = inputlist()
    if w == 0 and h == 0:
        break
    maze = [[0] for _ in range(h)]
    for i in range(h):
        maze[i] = inputlist()
    ans = 0
    for x in range(h):
        for y in range(w):
            ans += dfs(x, y, w, h, maze, 0)
    print(ans)