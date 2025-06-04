N = int(input())
A = list(map(int, input().split()))
if N == 1:
    print(1)
    exit()
DP = [[-1] * (N + 1) for _ in range(N + 1)]
D = [-1] * (N + 1)
R = {}
for i in range(5):
    a = A[i]
    if a in R:
        R[a] += 1
    else:
        R[a] = 1
Flag = 0
for i in R.keys():
    if R[i] >= 3:
        Flag = 1
        R[i] -= 3
L = []
for i in R.keys():
    if R[i] == 2:
        L.append(i)
        DP[i][i] = Flag
        D[i] = Flag
    elif R[i] == 1:
        L.append(i)
        D[i] = Flag

for i in range(len(L) - 1):
    for j in range(i + 1, len(L)):
        DP[L[i]][L[j]] = Flag

common = 0
for i in range(5, N * 3 - 3, 3):
    L2 = []
    for j in range(i, i + 3):
        found = False
        for k in range(len(L2)):
            if L2[k][1] == A[j]:
                L2[k][0] += 1
                found = True
                break
        if not found:
            L2.append([1, A[j]])
    L2.sort()
    RR = {}
    # 3 of a kind
    if len(L2) == 1:
        common += 1
    # 1:2 split
    elif len(L2) == 2:
        a = L2[0][1]
        b = L2[1][1]
        # matching the singleton
        if DP[a][a] != -1:
            if b not in RR: RR[b] = {}
            if b not in RR[b]: RR[b][b] = 0
            RR[b][b] = max([RR[b][b], DP[b][b], DP[a][a] + 1])
        # matching the pair
        for jj in range(N + 1):
            n = max(DP[b][jj], DP[jj][b])
            if n == -1: continue
            if a not in RR: RR[a] = {}
            if jj not in RR[a]: RR[a][jj] = 0
            RR[a][jj] = max([RR[a][jj], DP[a][jj], n + 1])
        # not matching
        for jj in range(N + 1):
            n = D[jj]
            if n == -1: continue
            if a not in RR: RR[a] = {}
            if jj not in RR[a]: RR[a][jj] = 0
            RR[a][jj] = max(RR[a][jj], n)
            if b not in RR: RR[b] = {}
            if jj not in RR[b]: RR[b][jj] = 0
            RR[b][jj] = max(RR[b][jj], n)
        n = max(D)
        if a not in RR: RR[a] = {}
        if b not in RR[a]: RR[a][b] = 0
        RR[a][b] = max(RR[a][b], n)
        if b not in RR: RR[b] = {}
        if b not in RR[b]: RR[b][b] = 0
        RR[b][b] = max(RR[b][b], n)
    # 1:1:1 split
    elif len(L2) == 3:
        a = L2[0][1]
        b = L2[1][1]
        c = L2[2][1]
        for aa, bb in [(b, c), (a, c), (a, b)]:
            if aa not in RR: RR[aa] = {}
            if bb not in RR[aa]: RR[aa][bb] = 0
        # matching
        if DP[a][a] != -1:
            RR[b][c] = max(RR[b][c], DP[a][a] + 1)
        if DP[b][b] != -1:
            RR[a][c] = max(RR[a][c], DP[b][b] + 1)
        if DP[c][c] != -1:
            RR[a][b] = max(RR[a][b], DP[c][c] + 1)
        # not matching
        for jj in range(N + 1):
            n = D[jj]
            if n == -1: continue
            if a not in RR: RR[a] = {}
            if jj not in RR[a]: RR[a][jj] = 0
            RR[a][jj] = max(RR[a][jj], n)
            if b not in RR: RR[b] = {}
            if jj not in RR[b]: RR[b][jj] = 0
            RR[b][jj] = max(RR[b][jj], n)
            if c not in RR: RR[c] = {}
            if jj not in RR[c]: RR[c][jj] = 0
            RR[c][jj] = max(RR[c][jj], n)
        n = max(D)
        RR[a][b] = max(RR[a][b], n)
        RR[b][c] = max(RR[b][c], n)
        RR[a][c] = max(RR[a][c], n)
    for k in RR.keys():
        for kk in RR[k].keys():
            n = RR[k][kk]
            if DP[k][kk] < n: DP[k][kk] = n
            if DP[kk][k] < n: DP[kk][k] = n
            if D[k] < n: D[k] = n
            if D[kk] < n: D[kk] = n

a = A[-1]
if DP[a][a] != -1:
    DP[a][a] += 1

ans = 0
for i in DP:
    for j in i:
        if ans < j: ans = j

ans += common
print(ans)