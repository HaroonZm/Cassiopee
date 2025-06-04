INF = float('inf')
VE = input().split()
V = int(VE[0])
E = int(VE[1])
D = []
for i in range(V):
    row = []
    for j in range(V):
        if i == j:
            row.append(0)
        else:
            row.append(INF)
    D.append(row)
for _ in range(E):
    line = input().split()
    s = int(line[0])
    t = int(line[1])
    d = int(line[2])
    D[s][t] = d
k = 0
while k < V:
    i = 0
    while i < V:
        j = 0
        while j < V:
            if D[i][j] > D[i][k] + D[k][j]:
                D[i][j] = D[i][k] + D[k][j]
            j += 1
        i += 1
    k += 1
negative = False
i = 0
while i < V:
    if D[i][i] < 0:
        negative = True
    i += 1
if negative:
    print('NEGATIVE CYCLE')
else:
    i = 0
    while i < V:
        row = []
        j = 0
        while j < V:
            if D[i][j] == INF:
                row.append('INF')
            else:
                row.append(str(D[i][j]))
            j += 1
        print(' '.join(row))
        i += 1