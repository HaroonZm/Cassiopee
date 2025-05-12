V, E = map(int, input().split())
inf = float('inf')
graphs = [[inf for _ in range(V)] for _ in range(V)]

for i in range(E):
    s, t, d = map(int, input().split())
    graphs[s][t] = d
# print(graphs)

dps = [[inf for _ in range(V)] for _ in range(1 << V)]

dps[0][0] = 0

for S in range(1, 1 << V):
    for i in range(V):
        # 両方とも1のやつのみ残る。
        # 1100 と0100(1<<2)だったら0100になる。
        # 訪問済みであることがこれで確認できる。
        if S & (1 << i) == 0:
            continue
        prev_bit = S - (1 << i)
        for j in range(V):
            # print(S, prev_bit, i, j)
            dps[S][i] = min(dps[S][i], dps[prev_bit][j] + graphs[j][i])
# print(dps)
if dps[(1 << V) - 1][0] == inf:
    print(-1)
else:
    print(dps[(1 << V) - 1][0])