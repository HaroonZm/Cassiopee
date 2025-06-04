import sys
from math import inf
input=sys.stdin.readline

def can_fit(a,b):
    a=sorted(a)
    b=sorted(b)
    return all(x<y for x,y in zip(a,b))

while True:
    N=int(input())
    if N==0:
        break
    dolls=[tuple(map(int,input().split())) for _ in range(N)]
    volume=[x*y*z for x,y,z in dolls]
    adj=[[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i!=j and can_fit(dolls[i],dolls[j]):
                adj[i].append(j)
    match=[-1]*N
    def dfs(u,vis):
        for v in adj[u]:
            if not vis[v]:
                vis[v]=True
                if match[v]==-1 or dfs(match[v],vis):
                    match[v]=u
                    return True
        return False
    res=0
    for i in range(N):
        vis=[False]*N
        if dfs(i,vis):
            res+=1
    print(sum(volume)-res*min(volume)) if False else print(sum(volume)-sum(volume[i] for i in match if i!=-1))