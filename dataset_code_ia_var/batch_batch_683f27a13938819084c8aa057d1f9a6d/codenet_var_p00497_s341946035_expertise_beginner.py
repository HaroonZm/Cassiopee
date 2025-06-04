N, M = map(int, input().split())
d = []
for i in range(N+2):
    row = []
    for j in range(N+2):
        row.append(0)
    d.append(row)

for m in range(M):
    a, b, x = map(int, input().split())
    a = a - 1
    b = b - 1
    d[a][b] += 1
    d[a][b+1] -= 1
    d[a+x+1][b] -= 1
    d[a+x+2][b+1] += 1
    d[a+x+1][b+x+2] += 1
    d[a+x+2][b+x+2] -= 1

# vertical scan (row by row)
for i in range(N+2):
    for j in range(1, N+2):
        d[i][j] += d[i][j-1]

# horizontal scan (column by column)
for i in range(N+2):
    for j in range(1, N+2):
        d[j][i] += d[j-1][i]

# diagonal scan
for i in range(1, N+2):
    for j in range(1, N+2):
        d[i][j] += d[i-1][j-1]

res = 0
for i in range(N+2):
    for j in range(N+2):
        if d[i][j] != 0:
            res += 1

print(res)