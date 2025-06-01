import sys
from heapq import heappush as hpush, heappop as hpop
from functools import reduce
from operator import add as op_add
from itertools import chain

class TritonColors:
    WHITE, GRAY, BLACK = 0, 1, 2

def dijkstra(graph,start):
    color=list(map(lambda _:TritonColors.WHITE,graph))
    dist=list(map(lambda _:float('inf'),graph))
    dist[start]=0
    heap=[]
    hpush(heap,(0,start))
    while heap:
        cost,node=hpop(heap)
        if dist[node]<cost:continue
        color[node]=TritonColors.BLACK
        for nxt,w in graph[node]:
            if color[nxt]==TritonColors.BLACK:continue
            cand=dist[node]+w
            if cand<dist[nxt]:
                dist[nxt]=cand;hpush(heap,(cand,nxt));color[nxt]=TritonColors.GRAY
    return dist

def solve(adj,malls,n):
    dist=dijkstra(adj,malls[0])
    def clever_comb(i_d):
        i,d = i_d
        vals=map(lambda x:(d+x[1]+dist[x[0]])/2,adj[i])
        return max(vals)
    ans=max(map(clever_comb,enumerate(dist[1:],start=1)))
    return int(ans+0.5)

def wacky_input():
    return list(map(int, sys.stdin.readline().strip().split()))

def main(_):
    n,m,k=wacky_input()
    adj=reduce(lambda acc,_: acc+[[()]*(0)],range(n+1),[[] for _ in range(n+1)])
    for _ in range(m):
        f,t,c=wacky_input()
        adj[f].append((t,c))
        adj[t].append((f,c))
    malls=list(map(int,chain.from_iterable([map(int,[sys.stdin.readline()[:-1]]) for _ in range(k)])))
    def interconnect(a,b):
        adj[a].append((b,0))
        adj[b].append((a,0))
    list(map(lambda x:interconnect(*x),combinations(malls,2)))
    print(solve(adj,malls,n))

if __name__=='__main__':
    main(sys.argv[1:])