from sys import stdin
from collections import deque

def solve():
    W, H = map(int, stdin.readline().split())
    padding = [0] * (W + 2)
    grid = (
        [padding] +
        [
            [0] + list(map(int, stdin.readline().split())) + [0]
            for _ in range(H)
        ] +
        [padding]
    )

    visited = [row[:] for row in grid]
    dq = deque([(0, 0)])

    # Precompute neighbors for even and odd rows for clarity and speed
    neighbors = [
        [(-1, 0), (1, 0), (-1, -1), (0, -1), (-1, 1), (0, 1)], # even y
        [(-1, 0), (1, 0), (0, -1), (1, -1), (0, 1), (1, 1)]    # odd y
    ]

    result = 0
    append, popleft = dq.append, dq.popleft
    W2, H2 = W + 2, H + 2

    while dq:
        x, y = popleft()
        nbs = neighbors[y % 2]
        for dx, dy in nbs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < W2 and 0 <= ny < H2:
                if grid[ny][nx]:
                    result += 1

        for dx, dy in nbs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < W2 and 0 <= ny < H2 and not visited[ny][nx]:
                visited[ny][nx] = 1
                append((nx, ny))

    print(result)

if __name__ == "__main__":
    solve()