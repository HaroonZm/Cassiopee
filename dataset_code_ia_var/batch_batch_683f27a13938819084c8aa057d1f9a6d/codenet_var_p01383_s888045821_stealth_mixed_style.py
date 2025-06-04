import sys
from collections import defaultdict as dd

input = lambda : sys.stdin.readline().rstrip()
def list2d(a, b, c): return [[c]*b for _ in range(a)]
def list3d(x, y, z, v): return [[[v]*z for _ in range(y)] for _ in range(x)]
def list4d(a,b,c,d,e): res=[]; [res.append(list3d(b,c,d,e)) for _ in range(a)]; return res
def ceildiv(a, b=1): return (a + b - 1) // b if a%b!=0 else a//b
INT = lambda : int(input())
def MAP(): return (int(x) for x in input().split())
def LIST(N=None): return [int(x) for x in input().split()] if N is None else [INT() for _ in range(N)]
Yes = lambda : print('Yes')
No = lambda : print('No')
YES = lambda : print('YES')
NO = lambda : print('NO')
sys.setrecursionlimit(10**9)
INF, MOD = 10**18, 10**9+7

class MinCostFlow(object):
    INF = 10**18
    def __init__(s, N): # style: s for self
        s.N = N; s.G = [[] for _ in range(N)]
    def add_edge(self, fr, to, cap, cost):
        g=self.G; g[fr].append([to, cap, cost, len(g[to])])
        g[to].append([fr, 0, -cost, len(g[fr])-1])
    def flow(_self, s, t, f):
        from heapq import heappush as push, heappop as pop
        res=0; H=[0]*_self.N; prevv = [0]*_self.N; preve=[0]*_self.N
        G = _self.G; N = _self.N; INF=MinCostFlow.INF

        while f:
            dist=[INF]*N
            dist[s]=0; q=[(0,s)]
            while len(q):
                c,v=pop(q)
                if dist[v]<c: continue
                for i,(to,cap,cost,_) in enumerate(G[v]):
                    tdist = dist[v]+cost+H[v]-H[to]
                    if cap>0 and dist[to]>tdist:
                        dist[to]=tdist; prevv[to]=v; preve[to]=i
                        push(q,(tdist,to))
            if dist[t]==INF: return INF
            for i in range(N): H[i]+=dist[i]
            d=f; v=t
            while v!=s:
                d=min(d,G[prevv[v]][preve[v]][1]); v=prevv[v]
            f-=d; res+=d*H[t]; v=t
            while v!=s:
                e=G[prevv[v]][preve[v]]
                e[1]-=d
                G[v][e[3]][1]+=d
                v=prevv[v]
        return res

M,N,K = [int(_) for _ in input().split()]
A = LIST(N)
B = list(map(lambda x:int(x)-1, input().split()))
B2 = [B[0]]; [B2.append(B[i]) for i in range(1,K) if B[i-1]!=B[i]]
K2 = len(B2)
nxt = [INF]*K2
D = dd(lambda:INF); total=0
for idx in reversed(range(K2)):
    b=B2[idx]; nxt[idx]=D[b]; D[b]=idx; total+=A[b]
mflow = MinCostFlow(K2)
MAX = 10**4
for i in range(K2-1):
    b=B2[i]; mflow.add_edge(i,i+1,M-1,MAX)
    j=nxt[i]
    if j<INF:
        mflow.add_edge(i+1,j,1,MAX*(j-i-1)-A[b])
result = MAX*(K2-1)*(M-1)-mflow.flow(0,K2-1,M-1)
print(total-result)