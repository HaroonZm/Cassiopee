from collections import deque

def Topologicalsort(v):
    start=deque()
    for i in xrange(v):
        if indeg[i]==0 :
            start.append(i)
    if len(start)>1:
        flag=True
    else:
        flag=False
    while len(start)>0:
        i=start.popleft()
        ans.append(i)
        tmp=[]
        for j in g[i]:
            indeg[j]-=1
            if indeg[j]==0:
                tmp.append(j)
                start.append(j)
                if len(tmp)>1:
                    flag=True
    return ans,flag

def solve(n,m):
    for i in xrange(m):
        wt,lt=map(int,raw_input().split())
        wt-=1;lt-=1
        g[wt].append(lt)
        indeg[lt]+=1
    ans,flag=Topologicalsort(n)
    return ans,flag

n=int(raw_input())
m=int(raw_input())
indeg=[0]*n
g=[[] for _ in xrange(n)]
ans=[]

ans,flag=solve(n,m)

if flag:
    for i in xrange(n):
        print(ans[i]+1)
    print(1)
else:
    for i in xrange(n):
        print(ans[i]+1)
    print(0)