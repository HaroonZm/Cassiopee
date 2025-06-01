c,n=map(int,input().split())
P=[list(map(int,input()))for i in range(n)]
S=[[0]*n for i in range(n)]
T=[[0]*n for i in range(n)]
dS=dT=0
for i in range(n):
    for j in range(n//2):
        S[i][j]=P[i][j]^P[i][n-1-j]
        dS+=S[i][j]
for j in range(n):
    for i in range(n//2):
        T[i][j]=P[i][j]^P[n-1-i][j]
        dT+=T[i][j]
ans=+(dS==dT==0)
for _ in range(c-1):
    d=int(input())
    for _ in range(d):
        r,c=map(int,input().split())
        S[r-1][min(c-1,n-c)]^=1
        if S[r-1][min(c-1,n-c)]:
            dS+=1
        else:
            dS-=1
        T[min(r-1,n-r)][c-1]^=1
        if T[min(r-1,n-r)][c-1]:
            dT+=1
        else:
            dT-=1
    if dS==dT==0:
        ans+=1
print(ans)