n, m, d = map(int, input().split())

floor = []
for _ in range(n):
    floor.append(list(input()))

cnt = 0
for i in range(n):
    for j in range(m):
        if floor[i][j] == ".":
            for k in range(1, d):
                if j+k >= m:
                    break
                elif floor[i][j+k] != ".":
                    break
            else:
                cnt += 1

            for k in range(1, d):
                if i+k >= n:
                    break
                elif floor[i+k][j] != ".":
                    break
            else:
                cnt += 1

print(cnt)