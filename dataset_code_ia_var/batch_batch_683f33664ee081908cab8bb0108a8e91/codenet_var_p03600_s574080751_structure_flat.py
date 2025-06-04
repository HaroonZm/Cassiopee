n = int(input())
INF = float("inf")
g = []
for i in range(n):
    row = []
    for j, c in enumerate(map(int, input().split())):
        if i != j:
            row.append(c)
        else:
            row.append(INF)
    g.append(row)
ans = 0
i = 0
while i < n:
    j = 0
    while j < i:
        m = INF
        k = 0
        while k < n:
            s = g[i][k] + g[j][k]
            if s < m:
                m = s
            k += 1
        if g[i][j] > m:
            print(-1)
            exit()
        if g[i][j] < m:
            ans += g[i][j]
        j += 1
    i += 1
print(ans)