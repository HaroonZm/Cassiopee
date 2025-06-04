N,M,D=map(int,input().split())
S=[input() for _ in range(N)]
res=0
if D==1:
    for i in range(N):
        for j in range(M):
            if S[i][j]=='.':
                res+=1
else:
    for i in range(N):
        count=0
        for j in range(M):
            if S[i][j]=='.':
                count+=1
            else:
                count=0
            if count>=D:
                res+=1
    for j in range(M):
        count=0
        for i in range(N):
            if S[i][j]=='.':
                count+=1
            else:
                count=0
            if count>=D:
                res+=1
print(res)