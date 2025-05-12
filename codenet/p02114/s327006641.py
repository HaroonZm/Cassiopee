from collections import deque
n = int(input())
A = [input() for i in range(n)]

cnt = 0
dd = [[-1, 0], [0, -1], [1, 0], [0, 1]]
used = {}
for i in range(n):
    for j in range(n):
        if A[i][j] == 'x' or (i, j) in used:
            continue
        deq = deque([(j, i)])
        used[i, j] = 1
        cnt += 1
        while deq:
            x, y = deq.popleft()
            for dx, dy in dd:
                nx = x + dx; ny = y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if A[ny][nx] == 'o' and (ny, nx) not in used:
                        used[ny, nx] = 1
                        deq.append((nx, ny))
print(cnt//3)