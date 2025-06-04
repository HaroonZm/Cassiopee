import sys
import math
from heapq import heappush, heappop

def solve():
    input = sys.stdin.readline
    while True:
        n,m,p,a,b = map(int,input().split())
        if n==0 and m==0 and p==0 and a==0 and b==0:
            break
        tickets = list(map(int,input().split()))
        adj = [[] for _ in range(m+1)]
        for _ in range(p):
            x,y,z = map(int,input().split())
            adj[x].append((y,z))
            adj[y].append((x,z))
        INF = float('inf')
        dist = [[INF]*(1<<n) for _ in range(m+1)]
        dist[a][(1<<n)-1] = 0.0
        heap = [(0.0,a,(1<<n)-1)]
        while heap:
            time,u,mask = heappop(heap)
            if dist[u][mask]<time - 1e-12:
                continue
            if u==b:
                print("{0:.3f}".format(time))
                break
            for v,d in adj[u]:
                for i in range(n):
                    if mask & (1<<i):
                        nt = time + d / tickets[i]
                        nmask = mask & ~(1<<i)
                        if dist[v][nmask] > nt:
                            dist[v][nmask] = nt
                            heappush(heap,(nt,v,nmask))
        else:
            print("Impossible")

if __name__=="__main__":
    solve()