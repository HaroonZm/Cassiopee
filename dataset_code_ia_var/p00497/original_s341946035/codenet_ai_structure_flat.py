N, M = map(int, input().split())
d = []
for _ in range(N + 2):
    d.append([0] * (N + 2))

i = 0
while i < M:
    a, b, x = map(int, input().split())
    a -= 1
    b -= 1
    d[a][b] += 1
    d[a][b + 1] -= 1
    d[a + x + 1][b] -= 1
    d[a + x + 2][b + 1] += 1
    d[a + x + 1][b + x + 2] += 1
    d[a + x + 2][b + x + 2] -= 1
    i += 1

i = 0
while i < N + 2:
    j = 1
    while j < N + 2:
        d[i][j] += d[i][j - 1]
        j += 1
    i += 1

i = 0
while i < N + 2:
    j = 1
    while j < N + 2:
        d[j][i] += d[j - 1][i]
        j += 1
    i += 1

i = 1
while i < N + 2:
    j = 1
    while j < N + 2:
        d[i][j] += d[i - 1][j - 1]
        j += 1
    i += 1

res = 0
i = 0
while i < N + 2:
    j = 0
    while j < N + 2:
        if d[i][j] != 0:
            res += 1
        j += 1
    i += 1

print(res)