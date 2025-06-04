n = int(input())
p = list(map(float, input().split()))
q = list(map(float, input().split()))

e = [[0.0]*(n+1) for _ in range(n+1)]
w = [[0.0]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    e[i][i] = q[i]
    w[i][i] = q[i]

for l in range(1, n+1):
    for i in range(n-l+1):
        j = i + l
        e[i][j] = 1e9
        w[i][j] = w[i][j-1] + p[j-1] + q[j]
        for r in range(i, j):
            t = e[i][r] + e[r+1][j] + w[i][j]
            if t < e[i][j]:
                e[i][j] = t

print(f"{e[0][n]:.8f}")