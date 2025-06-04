import sys
sys.setrecursionlimit(10**7)
N,K=map(int,input().split())
P=list(map(int,input().split()))
target=sorted(P)
pos=[0]*(N+1)
for i,v in enumerate(P):
    pos[v]=i
g=[[] for _ in range(N)]
for v in range(1,N+1):
    i=pos[v]
    if i-K+1>=0:
        g[i-K+1].append(i)
    if i+K-1<N:
        g[i+K-1].append(i)
visited=[False]*N
components=[]
def dfs(u,c):
    stack=[u]
    c.append(u)
    visited[u]=True
    while stack:
        x=stack.pop()
        for nx in g[x]:
            if not visited[nx]:
                visited[nx]=True
                c.append(nx)
                stack.append(nx)
for i in range(N):
    if not visited[i]:
        c=[]
        dfs(i,c)
        components.append(c)
for c in components:
    orig=[P[i] for i in c]
    targ=[target[i] for i in c]
    if sorted(orig)!=sorted(targ):
        print("No")
        exit()
print("Yes")