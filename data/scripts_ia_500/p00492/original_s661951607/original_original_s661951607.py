def solve():
    from collections import deque
    from copy import deepcopy
    W, H = map(int, input().split())
    a = [[0]*(W+2)] + [list(map(int, ("0 "+input()+" 0").split())) for _ in [0]*H] + [[0]*(W+2)]
    result = 0

    visited = deepcopy(a)
    dq = deque([(0, 0)])
    append, popleft = dq.append, dq.popleft

    while dq:
        x, y = popleft()
        neighbour = [(-1, 0), (1, 0)] + ([(-1, -1), (0, -1), (-1, 1), (0, 1)] if y%2 == 0 else [(0, -1), (1, -1), (0, 1), (1, 1)])
        for dx, dy in neighbour:
            nx, ny = dx+x, dy+y
            if 0 <= nx < W+2 and 0 <= ny < H+2:
                result += a[ny][nx]

        for dx, dy in neighbour:
            nx, ny = x+dx, y+dy
            if 0 <= nx < W+2 and 0 <= ny < H+2 and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                append((nx, ny))

    print(result)

if __name__ == "__main__":
    solve()