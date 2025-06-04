import sys
import heapq

input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    natsume,renon=map(int,input().split())
    adj=[[] for __ in range(n+1)]
    for __ in range(m):
        a,b,c=input().split()
        a=int(a);b=int(b)
        cost=0 if c=='L' else 1
        adj[a].append((b,cost))
        adj[b].append((a,cost))

    # On graph: edges cost 1 if human door (N), 0 if cat door (L)
    # Need to find minimal re-opening cost for Natsume so that Renon can reach room 0
    # Both natsume and renon can move on open doors.
    # Once human doors opened, they remain open

    # Idea: minimal cost to connect natsume and renon paths to 0 through opened human doors

    # We'll run 0-1 BFS from natsume and from renon to all rooms to get minimal human doors opened to reach that room
    def zero_one_bfs(start):
        dist=[float('inf')]*(n+1)
        dist[start]=0
        dq=[]
        heapq.heappush(dq,(0,start))
        while dq:
            c,u=heapq.heappop(dq)
            if dist[u]<c:
                continue
            for v,w in adj[u]:
                nc=c+w
                if dist[v]>nc:
                    dist[v]=nc
                    if w==0:
                        heapq.heappush(dq,(nc,v))
                    else:
                        heapq.heappush(dq,(nc,v))
        return dist

    dist_natsume=zero_one_bfs(natsume)
    dist_renon=zero_one_bfs(renon)
    dist_goal=zero_one_bfs(0)

    # minimal sum of dist_natsume[x]+dist_renon[x]+dist_goal[x] over x in [0,n].
    # But each human door opening counted thrice, so subtract 2 * number of times human doors opened

    res=float('inf')
    for x in range(n+1):
        val=dist_natsume[x]+dist_renon[x]+dist_goal[x]
        if val<res:
            res=val
    print(res)