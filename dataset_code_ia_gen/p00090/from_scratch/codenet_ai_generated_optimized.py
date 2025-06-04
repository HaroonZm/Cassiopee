import sys
import math
input=sys.stdin.readline

while True:
    n=int(input())
    if n==0:
        break
    stickers=[tuple(map(float,input().strip().split(','))) for _ in range(n)]
    adj=[[] for _ in range(n)]
    for i in range(n):
        x1,y1=stickers[i]
        for j in range(i+1,n):
            x2,y2=stickers[j]
            dx=x1-x2
            dy=y1-y2
            dist_sq=dx*dx+dy*dy
            # distance <=2 means overlap or touching
            if dist_sq<=4+1e-14:
                adj[i].append(j)
                adj[j].append(i)
    visited=[False]*n
    ans=0
    def dfs(u):
        stack=[u]
        count=0
        visited[u]=True
        while stack:
            cur=stack.pop()
            count+=1
            for nxt in adj[cur]:
                if not visited[nxt]:
                    visited[nxt]=True
                    stack.append(nxt)
        return count
    for i in range(n):
        if not visited[i]:
            ans=max(ans,dfs(i))
    print(ans)