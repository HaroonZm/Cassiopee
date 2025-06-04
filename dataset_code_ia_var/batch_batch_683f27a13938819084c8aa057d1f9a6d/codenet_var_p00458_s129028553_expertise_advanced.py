from sys import stdin
from collections import deque

def solve():
    get_ints = lambda: map(int, stdin.readline().split())
    while True:
        m = int(stdin.readline())
        n = int(stdin.readline())
        if m == 0:
            break

        ices = [[0] + list(get_ints()) + [0] for _ in range(n)]
        border = [0] * (m + 2)
        ices = [border] + ices + [border]
        score = [[0] * (m + 2) for _ in range(n + 2)]
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        for x in range(1, n + 1):
            for y in range(1, m + 1):
                if ices[x][y]:
                    for dx, dy in directions:
                        score[x + dx][y + dy] += 1

        def bfs(ix, iy):
            q, cnt, to_restore = deque([(ix, iy)]), 0, []
            ices[ix][iy] = 0
            to_restore.append((ix, iy))
            while q:
                x, y = q.popleft()
                cnt += 1
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if ices[nx][ny]:
                        ices[nx][ny] = 0
                        to_restore.append((nx, ny))
                        q.append((nx, ny))
            for x, y in to_restore:
                ices[x][y] = 1
            return cnt

        ans = 0
        for x in range(1, n + 1):
            for y in range(1, m + 1):
                if ices[x][y] and score[x][y] in {1, 2}:
                    ans = max(ans, bfs(x, y))

        print(ans)

solve()