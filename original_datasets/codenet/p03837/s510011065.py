import heapq
from collections import deque
N,M=map(int,input().split())
table=[[float("inf") for _ in range(N)] for _ in range(N)]
used=[[-float("inf") for _ in range(N)] for _ in range(N)]
tree=[[] for _ in range(N)]
for i in range(M):
    a,b,c=map(int,input().split())
    table[a-1][b-1]=c
    table[b-1][a-1]=c
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)
    used[a-1][b-1]=0
    used[b-1][a-1]=0
for i in range(N):
    table[i][i]=0
#print(used)
for i in range(N):
    d=[float("inf") for _ in range(N)]
    d[i]=0
    q=[]
    prev=[-1]*N
    q.append([0,i])
    heapq.heapify(q)
    while len(q)>0:
        dist,u=heapq.heappop(q)
        if d[u]<dist: continue
        piv=prev[u]
        v=u
        while piv!=-1:
            #print(piv)
            used[piv][v] = 1
            used[v][piv] = 1
            v = piv
            piv=prev[piv]
        for i in tree[u]:
            alt=d[u]+table[u][i]
            if d[i]>alt:
                d[i]=alt
                heapq.heappush(q,[alt,i])
                prev[i]=u
        #print(q,d,prev)
        #input()
    #print(d)
#print(used)
ans=0
for i in range(N):
    for j in range(N):
        if used[i][j]==0:
            ans=ans+1
print(ans//2)