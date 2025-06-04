n = int(raw_input())
C = [[] for _ in range(n)]
W = {}
for i in range(n):
    C[i] = map(int, raw_input().split())
    W[(i, i)] = 0
for i in range(1, n):
    for j in range(n - i):
        a = j + i
        W[(j, a)] = min([C[j][0] * C[k][1] * C[k+1][0] * C[a][1] + W[(j, k)] + W[(k+1, a)] for k in range(j, a)])
print W[(0, n - 1)]