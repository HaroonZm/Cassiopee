N = int(input())
A = list(map(int, input().split()))
DPLIST = []
for i in range(N):
    DPLIST.append([None] * N)
for i in range(N):
    DPLIST[i][i] = 0
SUM = [0]
for i in range(N):
    SUM.append(SUM[-1] + A[i])
for d in range(1, N):
    for l in range(N - d):
        r = l + d
        ANS = float("inf")
        for k in range(l, r):
            val = DPLIST[l][k] + DPLIST[k+1][r] + SUM[r+1] - SUM[l]
            if val < ANS:
                ANS = val
        DPLIST[l][r] = ANS
print(DPLIST[0][N-1])