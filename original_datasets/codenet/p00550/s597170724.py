from collections import deque

def make_DAG(s,n,g):
    newg=[[] for _ in xrange(n)]
    dist=[float("inf")]*n
    dist[s]=0
    dq=deque([s])
    visited=[False]*n
    visited[s]=True
    indeg=[0]*n
    while len(dq)>0:
        now=dq.popleft()
        for nx in g[now]:
            if dist[nx]>=dist[now]+1:
                if not visited[nx]:
                     visited[nx]=True
                     dq.append(nx)
                newg[now].append(nx)
                dist[nx]=dist[now]+1
                indeg[nx]+=1
    return newg,dist,indeg

def bfs_count(s,DAG,indeg):
    indeg[s]-=1
    if indeg[s]!=0:return 0
    dq=deque([s])
    cnt=1
    while len(dq)>0:
        now=dq.popleft()
        for nx in DAG[now]:
            if ok.has_key((now,nx)):continue
            ok[(now,nx)]=True
            indeg[nx]-=1
            if indeg[nx]==0:
                cnt+=1
                dq.append(nx)
    return cnt

n,m,q=map(int,raw_input().split())
e=[]
g=[[] for _ in xrange(n)]
for i in xrange(m):
    u,v=map(int,raw_input().split())
    u-=1;v-=1
    g[u].append(v)
    g[v].append(u)
    e.append((u,v))
DAG,dist,indeg=make_DAG(0,n,g)
ans=0
ok={}
for i in xrange(q):
    r=int(raw_input())
    r-=1
    u,v=e[r]
    if abs(dist[u]-dist[v])==0:
        print ans
        continue
    if dist[u]<dist[v]:
        if not ok.has_key((u,v)):
            ok[(u,v)]=True
            ans+=bfs_count(v,DAG,indeg)
    else:
        if not ok.has_key((v,u)):
            ok[(v,u)]=True
            ans+=bfs_count(u,DAG,indeg)
    print ans