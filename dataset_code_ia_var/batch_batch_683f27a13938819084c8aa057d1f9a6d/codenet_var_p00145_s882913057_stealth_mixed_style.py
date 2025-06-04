from functools import reduce

INF = float('inf')

n = int(input())
c = [[INF] * n for _ in range(n)]
a = []
i = 0
while i < n:
    l = input().split()
    a.append([int(l[0]), int(l[1])])
    c[i][i] = 0
    i += 1

def update(i, j):
    minv = INF
    for k in range(i, j):
        cur = c[i][k] + a[i][0] * a[k][1] * a[k+1][0] * a[j][1] + c[k+1][j]
        if cur < minv: minv = cur
    c[i][j] = minv

l = 1
while l < n:
    for start in range(n - l):
        end = start + l
        update(start, end)
    l += 1

print((lambda m: m[0][n-1])(c))