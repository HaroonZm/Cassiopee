n, m, d = map(int, input().split())
floor = [list(input()) for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if floor[i][j] == ".":
            for k in range(1, d):
                if j + k >= m or floor[i][j + k] != ".":
                    break
            else:
                cnt += 1
            for k in range(1, d):
                if i + k >= n or floor[i + k][j] != ".":
                    break
            else:
                cnt += 1
print(cnt)