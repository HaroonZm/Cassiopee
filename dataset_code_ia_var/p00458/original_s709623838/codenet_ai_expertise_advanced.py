from sys import stdin
from itertools import product

def main():
    input_iter = iter(stdin.read().splitlines())
    while True:
        try:
            M = int(next(input_iter))
            N = int(next(input_iter))
        except StopIteration:
            break
        if M == N == 0:
            break
        S = [list(map(int, next(input_iter).split())) for _ in range(N)]
        used = [[False] * M for _ in range(N)]
        def dfs(x, y, dirs=((-1,0),(0,-1),(1,0),(0,1))):
            stack = [(x, y, 1)]
            maxlen = 1
            while stack:
                cx, cy, clen = stack.pop()
                for dx, dy in dirs:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < M and 0 <= ny < N and S[ny][nx] and not used[ny][nx]:
                        used[ny][nx] = True
                        stack.append((nx, ny, clen+1))
                        maxlen = max(maxlen, clen+1)
                        used[ny][nx] = False
            return maxlen
        ans = 0
        for i, j in product(range(N), range(M)):
            if S[i][j]:
                used[i][j] = True
                ans = max(ans, dfs(j, i))
                used[i][j] = False
        print(ans)

if __name__ == '__main__':
    main()