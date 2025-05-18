import sys
input = sys.stdin.readline

N = int(input())

imos = [[0 for j in range(1001)] for i in range(1001)]

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    imos[x1][y1] += 1
    imos[x2][y2] += 1
    imos[x2][y1] -= 1
    imos[x1][y2] -= 1

for i in range(1001):
    for j in range(1000):
        imos[i][j + 1] += imos[i][j]

for j in range(1001):
    for i in range(1000):
        imos[i + 1][j] += imos[i][j]

res = 0

for i in range(1001):
    res = max(res, max(imos[i]))

print(res)