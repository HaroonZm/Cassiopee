from collections import deque

def TopoSort_cnt(n,cnt):
    start=deque()
    for i in xrange(n):
        if indeg[i]==0 :
            start.append(i)
    cnt+=len(start)
    while len(start)>0:
        i=start.popleft()
        ans.append(i)
        tmp=0
        for j in g[i]:
            indeg[j]-=1
            if indeg[j]==0:
                start.append(j)
                tmp+=1
        cnt=max(cnt,cnt*tmp)
    return ans,cnt

def solve(n,m):
    for i in xrange(m):
        wt,lt=map(int,raw_input().split())
        wt-=1;lt-=1
        g[wt].append(lt)
        indeg[lt]+=1
    ans,cnt=TopoSort_cnt(n,0)
    if cnt>1:
        for i in xrange(n):
            print(ans[i]+1)
        print(1)
    else:
        for i in xrange(n):
            print(ans[i]+1)
        print(0)

n=int(raw_input())
m=int(raw_input())
indeg=[0]*n
g=[[] for _ in xrange(n)]
ans=[]

solve(n,m)