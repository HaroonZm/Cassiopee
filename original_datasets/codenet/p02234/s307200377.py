n = int(input())
p = [0]*(n+1)
for i in range(1,n+1): p[i-1],p[i] = map(int,input().split())
m = [[0]*(n+1) for _ in range(n+1)]
# 対象とする行列の数l
for l in range(2,n+1):
    # for i in range(n+1): print(m[i])    
    # print("/////////////////////////////////")
    # 対象とする行列の範囲i,j
    # iは1からn-(l-1)まで
    for i in range(1,n-l+2):
        j = i+l-1
        m[i][j] = float("inf")
        # (M_iM_i+1...M_k)(M_k+1...M_j)の乗算回数が最小となるkを探す
        for k in range(i,j):
            m[i][j] = min(m[i][j], m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j])
print(m[1][n])