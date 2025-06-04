import sys, os
import numpy as np

# Variable globale
POOL = []

def blit(p, q):
    return (p << 9) | q

def split(z): return z >> 9, z & ((1 << 9) - 1)

def Build(n):
    arr = []
    for _ in range(n): arr.append([])
    return arr

class Network(object):
    def __init__(self, siz):
        self.n, self.g = siz, Build(siz)
    def link(self, u, v, cap):
        self.g[u].append([v, cap, len(self.g[v])])
        self.g[v].append([u, 0, len(self.g[u])-1])
    def bfs(self, s):
        lev = np.full(self.n, -1, np.int64)
        lev[s] = 0
        Q = [s]
        for x in Q:
            for y in self.g[x]:
                t = y[0]
                if y[1] and lev[t] == -1:
                    lev[t] = lev[x] + 1
                    Q.append(t)
        return lev
    def dfs(self, lev, curr, u, t, f):
        if u==t: return f
        for i in range(curr[u], len(self.g[u])):
            v, cap, ridx = self.g[u][i]
            if cap>0 and lev[v]==lev[u]+1:
                pushed = self.dfs(lev,curr,v,t,min(f,cap))
                if pushed:
                    self.g[u][i][1] -= pushed
                    self.g[v][ridx][1] += pushed
                    return pushed
            curr[u] += 1
        return 0
    def maxflow(self, s, t):
        fl = 0
        while 1:
            levels = self.bfs(s)
            if levels[t]==-1: return fl
            proc = np.zeros(self.n, np.int32)
            while True:
                add = self.dfs(levels, proc, s, t, 1<<30)
                if not add: break
                fl += add

def solve(n, m, G):
    X = []; Y = [] ; Yix = {}
    for x in range(1,n+1):
        for y in range(1,m+1):
            if G[x,y]:continue
            coords = blit(x,y)
            if (x ^ y)&1: X.append(coords)
            else:
                Yix[coords]=len(Y)
                Y.append(coords)
    LN, RN = len(X), len(Y)
    NET = Network(LN+RN+2)
    SRC,SNK = LN+RN, LN+RN+1
    for i,q in enumerate(X):
        for d in [-(1<<9),-1,1,1<<9]:
            z=q+d
            if z in Yix:
                NET.link(i, Yix[z]+LN, 1)
        NET.link(SRC, i, 1)
    for j in range(RN): NET.link(j+LN, SNK,1)
    flow = NET.maxflow(SRC,SNK)
    for i in range(LN):
        for v in NET.g[i]:
            if v[0]==SRC or v[1]:
                continue
            j=v[0]-LN
            ir,ic = split(X[i]);  jr,jc = split(Y[j])
            if ir==jr:
                a,b=sorted([ic, jc])
                G[ir,a]=4; G[jr,b]=5
            else:
                a,b=sorted([ir, jr])
                G[a,ic]=2; G[b,jc]=3
            break
    return flow

SIG = '(i8,i8,i1[:,:],)'
if sys.argv[-1]=='ONLINE_JUDGE':
    from numba.pycc import CC
    _cc = CC('M')
    _cc.export('solve', SIG)(solve)
    _cc.compile()
    exit()

if os.name=='posix':
    from M import solve
else:
    from numba import njit
    solve = njit(SIG, cache=True)(solve)
    print('compiled',file=sys.stderr)
N,M = map(int,input().split())
A = np.ones((N+2, M+2), np.int8)
for i in range(N): A[i+1,1:M+1] = list(map('.#'.index, input()))
r=solve(N,M,A)
print(r)
C = '.#v^><'.__getitem__
for i in range(1,N+1):
    print(''.join(map(C, A[i,1:M+1])))