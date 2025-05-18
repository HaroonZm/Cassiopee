import bisect,sys

input=sys.stdin.readline

N,Q=map(int,input().split())
que=[(N,0)]
for i in range(Q):
    q=int(input())
    que.append((q,i+1))

que.sort(reverse=True)

ext=[]
while que:
    q,id=que.pop()
    if not ext:
        ext.append((q,id))
    else:
        if ext[-1][1]<id:
            if ext[-1][0]==q:
                ext.pop()
            ext.append((q,id))

Q=len(ext)
data=[1]*Q
data[0]=ext[0][0]
edge=[[] for i in range(Q)]
nowext=[ext[0][0]]
for i in range(1,Q):
    q=ext[i][0]
    rest=q
    while True:
        id=bisect.bisect_right(nowext,rest)
        if id==0:
            break
        else:
            edge[id-1].append((i,rest//nowext[id-1]))
            rest%=nowext[id-1]
    nowext.append(ext[i][0])
    data[i]=rest

#print(edge)

dp=[1]*Q
for i in range(Q-2,-1,-1):
    temp=0
    for nv,c in edge[i]:
        temp+=dp[nv]*c
    dp[i]=temp

#print(dp)
#print(data)

minus=[0]*(ext[0][0]+1)
for i in range(Q):
    minus[data[i]]+=dp[i]

base=sum(dp)
for i in range(1,N+1):
    if i-1<=ext[0][0]:
        base-=minus[i-1]
    print(base)