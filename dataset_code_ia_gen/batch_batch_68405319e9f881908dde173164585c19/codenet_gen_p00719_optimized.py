import sys
import math
import heapq

def solve():
    input = sys.stdin.readline
    while True:
        n,m,p,a,b = map(int,input().split())
        if n==0 and m==0 and p==0 and a==0 and b==0:
            break
        horses = list(map(int,input().split()))
        adj = [[] for _ in range(m+1)]
        for _ in range(p):
            x,y,z = map(int,input().split())
            adj[x].append((y,z))
            adj[y].append((x,z))
        # state: (cost,time)
        # pos: current city
        # used: bitmask of tickets used
        dist = [[math.inf]*(1<<n) for _ in range(m+1)]
        dist[a][0]=0.0
        hq = [(0.0,a,0)]
        while hq:
            cost,u,used = heapq.heappop(hq)
            if dist[u][used]<cost:
                continue
            if u==b:
                print(f"{cost:.3f}")
                break
            for v,w in adj[u]:
                for i in range(n):
                    if (used&(1<<i))==0:
                        nxt_cost = cost + w/horses[i]
                        nxt_used = used|(1<<i)
                        if dist[v][nxt_used]>nxt_cost:
                            dist[v][nxt_used]=nxt_cost
                            heapq.heappush(hq,(nxt_cost,v,nxt_used))
        else:
            print("Impossible")

if __name__=="__main__":
    solve()