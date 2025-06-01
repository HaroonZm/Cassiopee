c,n=map(int,input().split())
P=[]
for _ in range(n):
    line = input()
    P.append([int(ch) for ch in line])
S = []
for i in range(n):
    row = [0]*n
    S.append(row)
T = [[0]*n for _ in range(n)]
dS,dT=0,0

i=0
while i<n:
    j=0
    while j<n//2:
        S[i][j]=P[i][j]^P[i][n-1-j]
        dS+=S[i][j]
        j+=1
    i+=1

j=0
while j<n:
    for i in range(n//2):
        T[i][j]=P[i][j]^P[n-1 - i][j]
        dT+=T[i][j]
    j+=1

ans = int(dS == 0 and dT == 0)

for _ in range(c-1):
    d=int(input())
    for __ in range(d):
        r,c = map(int,input().split())
        x=min(c-1,n-c)
        y=min(r-1,n-r)
        S[r-1][x]^=1
        if S[r-1][x]: dS+=1
        else: dS-=1
        T[y][c-1]^=1
        dT = dT+1 if T[y][c-1] else dT-1
    ans += (dS==0 and dT==0)

print(ans)