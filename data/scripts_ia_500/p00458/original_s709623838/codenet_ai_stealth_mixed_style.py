def main():
    while True:
        M = int(input())
        N = int(input())
        if M == 0 and N == 0:
            return
        S = []
        for _ in range(N):
            row = list(map(int, input().split()))
            S.append(row)
        used = [[False for _ in range(M)] for __ in range(N)]

        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        def dfs(x, y):
            max_length = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < M and 0 <= ny < N:
                    if S[ny][nx] != 0 and not used[ny][nx]:
                        used[ny][nx] = True
                        candidate = dfs(nx, ny) + 1
                        max_length = candidate if candidate > max_length else max_length
                        used[ny][nx] = False
            return max_length

        res = 0
        for i in range(N):
            for j in range(M):
                if S[i][j] != 0:
                    used[i][j] = True
                    res = max(res, dfs(j, i) + 1)
                    used[i][j] = False
        print(res)

main()