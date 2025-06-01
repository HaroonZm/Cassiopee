from collections import deque
n,m=map(int,input().split())
abx=[[0]*(n+2) for _ in range(n+2)]
for _ in range(m):
    ai,bi,xi=map(int,input().split())
    if xi>abx[ai][bi]:
        abx[ai][bi]=xi
pp=[[0]*(n+2) for _ in range(n+2)]
for j in range(1,n+2):
    dq=deque()
    for i in range(j,n+2):
        if abx[i][j]>0:
            dq.append([i,abx[i][j]])
    iiii=j-1
    while dq:
        ii,xi=dq.popleft()
        if ii+xi>iiii:
            start=max(ii,iiii+1)
            end=ii+xi+1
            for iii in range(start,end):
                pp[iii][j]=iii-ii+1
                iiii=iii
icnt=0
for i in range(1,n+1):
    for j in range(1,i+1):
        abij=pp[i][j-1]-1
        if abij>pp[i][j]:
            pp[i][j]=abij
        if pp[i][j]>0:
            icnt+=1
print(icnt)