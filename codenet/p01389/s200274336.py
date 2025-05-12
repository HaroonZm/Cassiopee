M_lis = []  
H,W = map(int,input().split())
DP = [[0 for j in range(W)] for i in range(H)]
for i in range(H):
    M_lis.append(list(map(int,list(str(input())))))
for j in range(1,W):
    DP[0][j] += M_lis[0][j] + DP[0][j - 1]
for k in range(1,H):
    DP[k][0] += M_lis[k][0] + DP[k - 1][0]
for i in range(1,H):
    for j in range(1,W):
        DP[i][j] = min(DP[i - 1][j],DP[i][j - 1]) + M_lis[i][j]

print(DP[H - 1][W - 1])