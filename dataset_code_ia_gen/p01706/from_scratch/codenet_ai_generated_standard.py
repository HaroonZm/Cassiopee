import sys
import threading
from collections import deque

sys.setrecursionlimit(10**7)

def main():
    input = sys.stdin.readline

    while True:
        N,M,S,T = map(int,input().split())
        if N==0 and M==0 and S==0 and T==0:
            break
        edges = []
        graph = [[] for _ in range(N+1)]
        rev_graph = [[] for _ in range(N+1)]
        for _ in range(M):
            a,b = map(int,input().split())
            edges.append((a,b))
            graph[a].append(b)
            rev_graph[b].append(a)

        # Step 1: Compute max flow with unit capacities (max number of edge-disjoint paths)
        # Use Dinic's algorithm with edges having capacity 1

        class Edge:
            __slots__ = ['to','rev','cap']
            def __init__(self,to,rev,cap):
                self.to = to
                self.rev = rev
                self.cap = cap

        def add_edge(g,a,b,c):
            g[a].append(Edge(b,len(g[b]),c))
            g[b].append(Edge(a,len(g[a])-1,0))

        def bfs(level,s,t,g):
            queue = deque()
            level[s] = 0
            queue.append(s)
            while queue:
                v = queue.popleft()
                for e in g[v]:
                    if e.cap >0 and level[e.to]<0:
                        level[e.to] = level[v]+1
                        queue.append(e.to)
            return level[t]>=0

        def dfs(level,iter,v,t,f,g):
            if v==t:
                return f
            while iter[v]<len(g[v]):
                e = g[v][iter[v]]
                if e.cap>0 and level[v]<level[e.to]:
                    d = dfs(level,iter,e.to,t,min(f,e.cap),g)
                    if d>0:
                        e.cap-=d
                        g[e.to][e.rev].cap+=d
                        return d
                iter[v]+=1
            return 0

        g = [[] for _ in range(N+1)]
        for a,b in edges:
            add_edge(g,a,b,1)

        flow=0
        level = [-1]*(N+1)
        while True:
            for i in range(N+1):
                level[i]=-1
            if not bfs(level,S,T,g):
                break
            iter = [0]*(N+1)
            while True:
                f=dfs(level,iter,S,T,10**9,g)
                if f==0:
                    break
                flow+=f

        # Step 2: Build residual graph (forward edges with cap>0 and backward edges with cap>0)
        # Mark reachable from S in residual graph -> A set
        # Mark nodes that can reach T in residual graph (reverse graph) -> B set

        residual = [[] for _ in range(N+1)]
        for v in range(1,N+1):
            for e in g[v]:
                if e.cap>0:
                    residual[v].append(e.to)
        reachable = [False]*(N+1)
        def dfs_res1(u):
            reachable[u]=True
            for w in residual[u]:
                if not reachable[w]:
                    dfs_res1(w)
        dfs_res1(S)

        residual_rev = [[] for _ in range(N+1)]
        for v in range(1,N+1):
            for e in g[v]:
                rev_cap = g[e.to][e.rev].cap
                if rev_cap>0:
                    residual_rev[e.to].append(v)
        can_reach_t = [False]*(N+1)
        def dfs_res2(u):
            can_reach_t[u]=True
            for w in residual_rev[u]:
                if not can_reach_t[w]:
                    dfs_res2(w)
        dfs_res2(T)

        # Now find edges that when reversed can increase max flow by 1
        # Conditions: edge (u->v) where u in set A (reachable from S), v not in A
        # and v in set B (can reach T), u not in B
        # For such edges, reversal opens new augmenting path increasing flow by 1

        candidates=0
        for a,b in edges:
            if reachable[a] and not reachable[b] and can_reach_t[b] and not can_reach_t[a]:
                candidates+=1

        if candidates==0:
            print(flow,0)
        else:
            print(flow+1,candidates)

threading.Thread(target=main).start()