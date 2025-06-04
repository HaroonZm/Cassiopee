import sys
import heapq
from itertools import product

def main():
    input_lines = iter(sys.stdin.read().splitlines())
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
    while True:
        try:
            n, m = map(int, next(input_lines).split())
        except StopIteration:
            break
        if n == 0:
            break

        X_row = "X" * (n + 2)
        rows = ["X" + next(input_lines) + "X" for _ in range(m)]
        mp = [X_row, *rows, X_row]

        visited = [bytearray(n + 2) for _ in range(m + 2)]
        queue = []
        sur_flag = any(mp[1][i] == "&" or mp[m][i] == "&" for i in range(1, n + 1)) or \
                   any(mp[i][1] == "&" or mp[i][n] == "&" for i in range(1, m + 1))
        if sur_flag:
            print(0)
            continue

        for i in range(1, n + 1):
            for y in (1, m):
                cell = mp[y][i]
                c, s = (1, 0) if cell == "#" else (0, 1)
                heapq.heappush(queue, (c, s, i, y))
                visited[y][i] = 1
        for i in range(1, m + 1):
            for x in (1, n):
                cell = mp[i][x]
                c, s = (1, 0) if cell == "#" else (0, 1)
                heapq.heappush(queue, (c, s, x, i))
                visited[i][x] = 1

        while queue:
            cost, status, x, y = heapq.heappop(queue)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if not visited[ny][nx]:
                    visited[ny][nx] = 1
                    sym = mp[ny][nx]
                    if sym == "&":
                        print(cost)
                        queue.clear()
                        break
                    elif sym == "#":
                        heapq.heappush(queue, (cost + (status == 1), 0, nx, ny))
                    elif sym == ".":
                        heapq.heappush(queue, (cost, 1, nx, ny))

if __name__ == "__main__":
    main()