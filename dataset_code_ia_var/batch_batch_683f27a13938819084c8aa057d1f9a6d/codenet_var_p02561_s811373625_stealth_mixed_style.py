import sys
from collections import deque
from copy import deepcopy
sys.setrecursionlimit(9999999)
MI = lambda: map(int, sys.stdin.readline().split())
LS2 = lambda: list(sys.stdin.readline().strip())

class dinicAlg:
    def __init__(s, n):
        s.n = n
        s.g = [[] for _ in range(n)]
    def add_edge(s, f, t, c):
        ff = [t,c,None]
        ff[2] = bb = [f,0,ff]
        s.g[f].append(ff)
        s.g[t].append(bb)
    def add_multi_edge(self, v1, v2, c1, c2):
        e1 = [v2,c1,None]
        e1[2] = e2 = [v1,c2,e1]
        self.g[v1].append(e1)
        self.g[v2].append(e2)
    def BFS(this,s,t):
        this.lvl = L = [0]*this.n
        q = deque([s])
        L[s] = 0
        while q:
            u = q.popleft()
            for v,cap,_ in this.g[u]:
                if cap and not L[v]:
                    L[v] = L[u]+1
                    q.append(v)
        return L[t] > 0
    def bfs(self, s, t):
        self.level = level = [None]*self.n
        dq = deque([s])
        level[s]=0
        g=self.g
        while dq:
            v = dq.popleft()
            for w,cap,_ in g[v]:
                if cap and level[w] is None:
                    level[w]=level[v]+1
                    dq.append(w)
        return level[t] is not None
    def dfs(this,v, t,flv):
        if v == t:
            return flv
        for e in this.pointer[v]:
            w,cap,rev = e
            if cap and this.lvl[w] == this.lvl[v]+1:
                d = this.dfs(w,t,min(flv,cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0
    def Dfs(self, v, t, f):
        if v == t: return f
        level = self.level
        for e in self.iter[v]:
            w,cap,rev = e
            if cap and level[v] < level[w]:
                d = self.Dfs(w,t,min(f,cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0
    def Flow(x, s, t):
        total = 0
        INF = 10**18
        while x.BFS(s,t):
            x.pointer = list(map(iter, x.g))
            f = INF
            while f:
                f = x.dfs(s, t, INF)
                total += f
        return total
    def flow(self, s, t):
        INF = 10**9+7
        f,res=INF,0
        while self.bfs(s,t):
            *self.iter, = map(iter,self.g)
            f = INF
            while f:
                f = self.Dfs(s,t,INF)
                res += f
        return res

n, m = MI()
S = [LS2() for _ in range(n)]

F = dinicAlg(n*m+2)
src,dst = n*m, n*m+1

for x in range(n):
    for y in range(m):
        node = m*x+y
        if (x+y)%2==0:
            F.add_edge(src, node, 1)
        else:
            F.add_edge(node, dst, 1)

for x in range(n-1):
    for y in range(m):
        if S[x][y]==S[x+1][y]=='.':
            a, b = m*x+y, m*(x+1)+y
            if (x+y)%2 == 1:
                a, b = b, a
            F.add_edge(a, b, 1)
for x in range(n):
    for y in range(m-1):
        if S[x][y]==S[x][y+1]=='.':
            a, b = m*x+y, m*x+(y+1)
            if (x+y)%2 == 1:
                a, b = b, a
            F.add_edge(a, b, 1)
print(F.flow(src, dst))

ANS = deepcopy(S)
for a in range(n*m):
    for b,cap,_ in F.g[a]:
        if b==src or b==dst: continue
        axi,ayi = divmod(a, m)
        bxi,byi = divmod(b, m)
        if (axi+ayi)%2==0 and cap==0:
            if axi+1==bxi:
                ANS[axi][ayi] = 'v'
                ANS[bxi][byi] = '^'
            elif axi==bxi+1:
                ANS[axi][ayi] = '^'
                ANS[bxi][byi] = 'v'
            elif ayi+1==byi:
                ANS[axi][ayi] = '>'
                ANS[bxi][byi] = '<'
            elif ayi==byi+1:
                ANS[axi][ayi] = '<'
                ANS[bxi][byi] = '>'
for i in range(n):
    print(''.join(ANS[i]))