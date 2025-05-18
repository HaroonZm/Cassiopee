import sys
input = sys.stdin.readline

X,Y,Z,N,M,S,T=map(int,input().split())

CS=[[0,0,0]]+[list(map(int,input().split()))+[i+1]+[0] for i in range(N)]
CC=[[0,0,0]]+[list(map(int,input().split()))+[i+1]+[1] for i in range(M)]

CS_SLIST=[[] for i in range(X+1)]
CS_CLIST=[[] for i in range(Y+1)]
CC_CLIST=[[] for i in range(Y+1)]
CC_ULIST=[[] for i in range(Z+1)]

for x,y,z,_ in CS[1:]:
    CS_SLIST[x].append(z)
    CS_CLIST[y].append(z)

for x,y,z,_ in CC[1:]:
    CC_CLIST[x].append(z)
    CC_ULIST[y].append(z)

import heapq
MINCOST_CS=[1<<30]*(N+1)
MINCOST_CC=[1<<30]*(M+1)

MINCOST_CS[S]=0

Q=[[0]+CS[S]]
USES=[0]*(X+1)
USEC=[0]*(Y+1)
USEU=[0]*(Z+1)

while Q:
    #print(Q)
    cost,x,y,z,cs=heapq.heappop(Q)
    
    if cs==0:

        if USES[x]==0:
            USES[x]=1
            for to in CS_SLIST[x]:
                if MINCOST_CS[to]>cost+1:
                    MINCOST_CS[to]=cost+1
                    heapq.heappush(Q,[cost+1]+CS[to])

        if USEC[y]==0:
            USEC[y]=1

            for to in CS_CLIST[y]:
                if MINCOST_CS[to]>cost+1:
                    MINCOST_CS[to]=cost+1
                    heapq.heappush(Q,[cost+1]+CS[to])

            for to in CC_CLIST[y]:
                if MINCOST_CC[to]>cost+1:
                    MINCOST_CC[to]=cost+1
                    heapq.heappush(Q,[cost+1]+CC[to])

    else:

        if USEU[y]==0:
            USEU[y]=1
            for to in CC_ULIST[y]:
                if MINCOST_CC[to]>cost+1:
                    MINCOST_CC[to]=cost+1
                    heapq.heappush(Q,[cost+1]+CC[to])

        if USEC[x]==0:
            USEC[x]=1

            for to in CS_CLIST[x]:
                if MINCOST_CS[to]>cost+1:
                    MINCOST_CS[to]=cost+1
                    heapq.heappush(Q,[cost+1]+CS[to])

            for to in CC_CLIST[x]:
                if MINCOST_CC[to]>cost+1:
                    MINCOST_CC[to]=cost+1
                    heapq.heappush(Q,[cost+1]+CC[to])

#print(MINCOST_CS)
#print(MINCOST_CC)

if MINCOST_CC[T]==1<<30:
    print(-1)
else:
    print(MINCOST_CC[T])