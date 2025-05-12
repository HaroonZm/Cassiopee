# https: // onlinejudge.u-aizu.ac.jp/problems/GRL_1_C
INF = float('inf')

V, E = list(map(int, input().split()))

D = [[INF for _ in range(V)] for _ in range(V)]
for i in range(V):
    D[i][i] = 0

for _ in range(E):
    s, t, d = list(map(int, input().split()))
    D[s][t] = d

for k in range(V):
    for i in range(V):
        for j in range(V):
            D[i][j] = min(D[i][j], D[i][k] + D[k][j])

has_negative_cycle = False
for i in range(V):
    for j in range(V):
        if i == j and D[i][j] < 0:
            has_negative_cycle = True
        if D[i][j] == INF:
            D[i][j] = 'INF'
        else:
            D[i][j] = str(D[i][j])

if has_negative_cycle:
    print('NEGATIVE CYCLE')
else:
    for row in D:
        print(' '.join(row))