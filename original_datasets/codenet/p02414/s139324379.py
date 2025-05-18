n, m, l = map(int, input().split())
a = [[0 for i in range(m)] for j in range(n)]
b = [[0 for i in range(l)] for j in range(m)]
c = [[0 for i in range(l)] for j in range(n)]

for i in range(n):
    s = list(map(int, input().split()))
    for j in range(m): a[i][j] = s[j]
for i in range(m):
    s = list(map(int, input().split()))
    for j in range(l): b[i][j] = s[j]
for i in range(n):
    for j in range(l):
        s = 0
        for x in range(m):
            s += a[i][x] * b[x][j]
        c[i][j] = s
for i in range(n):
    for j in range(l):
        if j == (l - 1):
            print(c[i][j])
        else:
            print(c[i][j], "", end = "")