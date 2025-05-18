import sys
from collections import deque
from copy import deepcopy
sys.setrecursionlimit(10**7)
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

class Dinic:
    def __init__(self, N):
        self.N = N
        self.G = [[] for _ in range(N)]

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    def bfs(self, s, t):
        self.level = level = [None]*self.N
        deq = deque([s])
        level[s] = 0
        G = self.G
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in G[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        return level[t] is not None

    def dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        INF = 10**9 + 7
        G = self.G
        while self.bfs(s, t):
            *self.it, = map(iter, self.G)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow

N,M = MI()
S = [LS2() for _ in range(N)]

D = Dinic(N*M+2)
s,t = N*M,N*M+1
for i in range(N):
    for j in range(M):
        if (i+j) % 2 == 0:
            D.add_edge(s,M*i+j,1)
        else:
            D.add_edge(M*i+j,t,1)

for i in range(N-1):
    for j in range(M):
        if S[i][j] == S[i+1][j] == '.':
            a,b = M*i+j,M*(i+1)+j
            if (i+j) % 2 == 1:
                a,b = b,a
            D.add_edge(a,b,1)

for i in range(N):
    for j in range(M-1):
        if S[i][j] == S[i][j+1] == '.':
            a,b = M*i+j,M*i+(j+1)
            if (i+j) % 2 == 1:
                a,b = b,a
            D.add_edge(a,b,1)

print(D.flow(s,t))

ANS = deepcopy(S)
for a in range(N*M):
    for b,cap,_ in D.G[a]:
        if b == s or b == t:
            continue
        ai,aj = divmod(a,M)
        bi,bj = divmod(b,M)
        if (ai+aj) % 2 == 0 and cap == 0:
            if ai+1 == bi:
                ANS[ai][aj] = 'v'
                ANS[bi][bj] = '^'
            elif ai == bi+1:
                ANS[ai][aj] = '^'
                ANS[bi][bj] = 'v'
            elif aj+1 == bj:
                ANS[ai][aj] = '>'
                ANS[bi][bj] = '<'
            elif aj == bj+1:
                ANS[ai][aj] = '<'
                ANS[bi][bj] = '>'

for i in range(N):
    print(''.join(ANS[i]))