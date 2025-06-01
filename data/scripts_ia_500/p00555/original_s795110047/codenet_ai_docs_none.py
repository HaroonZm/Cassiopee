N,M,D=map(int,input().split())
S=[list(input()) for _ in range(N)]
ans=0
for i in range(N):
    count=0
    for j in range(M):
        if S[i][j]==".":
            count+=1
            if count>=D:
                ans+=1
        else:
            count=0
T=[["" for _ in range(N)] for _ in range(M)]
for i in range(N):
    for j in range(M):
        T[j][i]=S[i][j]
for j in range(M):
    count=0
    for i in range(N):
        if T[j][i]==".":
            count+=1
            if count>=D:
                ans+=1
        else:
            count=0
print(ans)