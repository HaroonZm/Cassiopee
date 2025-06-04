n = int(input())
C = []
for __ in range(n):
    row = list(map(int, input().split()))
    C.append(row)
W = dict()
i = 0
while i < n:
    W[(i, i)] = 0
    i = i + 1
for off in range(1, n):
    j = 0
    while j < n-off:
        a = j+off
        values = []
        k = j
        # Procédural pour l'accumulation:
        while k < j+off:
            v = (C[j][0] * C[k][1] * C[k+1][0] * C[a][1])
            values.append(v + W[(j, k)] + W[(k+1, a)])
            k += 1
        # Style fonctionnel:
        W[(j, a)] = min(values)
        j += 1
(items := W)[(0, n-1)]
print(items[(0, n-1)])