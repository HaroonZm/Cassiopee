n = int(input())
a = []
for i in range(1001):
    a.append([0] * 1001)

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    a[x1][y1] += 1
    a[x1][y2] -= 1
    a[x2][y1] -= 1
    a[x2][y2] += 1

# Calcul des préfixes horizontaux
for i in range(1001):
    for j in range(1, 1001):
        a[i][j] += a[i][j-1]

# Calcul des préfixes verticaux
for j in range(1001):
    for i in range(1, 1001):
        a[i][j] += a[i-1][j]

ans = 0
for i in range(1001):
    for j in range(1001):
        if a[i][j] > ans:
            ans = a[i][j]

print(ans)