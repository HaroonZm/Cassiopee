import sys
readline = sys.stdin.readline
write = sys.stdout.write
from string import digits
from collections import deque

# Ça va être notre algo de flot (un bon vieux Dinic)
class Dinic:
    def __init__(self, N):
        self.N = N
        self.G = [[] for _ in range(N)]
    
    def add_edge(self, fr, to, cap):
        fwd = [to, cap, None]
        fwd[2] = bwd = [fr, 0, fwd]
        self.G[fr].append(fwd)
        self.G[to].append(bwd)
    
    def add_multi_edge(self, v1, v2, cap1, cap2): # fait un peu comme add_edge
        ed1 = [v2, cap1, None]
        ed1[2] = ed2 = [v1, cap2, ed1]
        self.G[v1].append(ed1)
        self.G[v2].append(ed2)
    
    def bfs(self, s, t):
        self.level = [None]*self.N
        dq = deque()
        dq.append(s)
        self.level[s] = 0
        while dq:
            v = dq.popleft()
            for w, cap, _ in self.G[v]:
                if cap and self.level[w] is None:
                    self.level[w] = self.level[v]+1
                    dq.append(w)
        return self.level[t] is not None
    
    def dfs(self, v, t, f):
        if v == t:
            return f
        for e in self.it[v]:
            w, cap, rev = e
            if cap and self.level[w] == self.level[v]+1:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0
    
    def flow(self, s, t):
        flow = 0
        INF = 1000000007  # bon, je mets un gros inf là, ça suffira
        while self.bfs(s, t):
            self.it = list(map(iter, self.G))
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow

def parse(S, L=50):
    # on va parser un polynome un peu à l'arrache
    S = S + '$'
    E = [0]*(L+1)
    cur = 0
    while True:
        if S[cur] in digits:
            k = 0
            while S[cur] in digits:
                k = k*10 + int(S[cur])
                cur += 1 # avance
        else:
            k = 1
        if S[cur] == 'x':
            cur += 1
            if S[cur] == '^':
                cur += 1
                p = 0
                while S[cur] in digits:
                    p = p*10 + int(S[cur])
                    cur += 1
            else:
                p = 1
        else:
            p = 0
        E[p] = k
        if S[cur] != '+':
            break
        cur += 1 # saute +
    return E

def solve():
    try:
        N_M = readline()
        if not N_M:
            return False
        N, M = map(int, N_M.split())
    except:
        return False
    if N == 0:
        return False
    L = 50
    ds = [Dinic(N) for _ in range(L+1)]
    for _ in range(M):
        line = readline()
        if not line:
            continue
        u, v, p = line.split()
        u = int(u)-1
        v = int(v)-1
        poly = parse(p, L)
        for j in range(L+1):
            if poly[j]:
                ds[j].add_multi_edge(u, v, poly[j], poly[j])
    INF = 10**9
    res = [0]*(L+1)
    for j in range(L+1):
        res[j] = ds[j].flow(0, N-1)
    E = [[0]*N for _ in range(N)]
    # boucle pour faire la maj des flots pour chaque degré, 
    for j in range(L-1, -1, -1):
        cur_dinic = ds[j]
        # (je crois que ce "used" ne sert à rien mais bon)
        used = [0]*N
        used[N-1] = 1
        que = deque([N-1])
        G = ds[j+1].G
        for v in range(N):
            for w, cap, _ in G[v]:
                if cap:
                    E[v][w] = 1
        for v in range(N):
            for w in range(N):
                if E[v][w]:
                    cur_dinic.add_edge(v, w, INF)
        res[j] += cur_dinic.flow(0, N-1)
    ans = []
    # récupération du polynome sous forme string (encore du code pas tip-top...)
    if res[0]:
        ans.append(str(res[0]))
    if res[1]:
        if res[1] == 1:
            ans.append("x")
        else:
            ans.append("%dx" % res[1])
    for i in range(2, L+1):
        if res[i]:
            if res[i] == 1:
                ans.append("x^%d" % i)
            else:
                ans.append("%dx^%d" % (res[i], i))
    if not ans:
        ans.append("0")
    ans.reverse() # je renverse, pourquoi pas
    write('+'.join(ans))
    write('\n')
    return True

while solve():
    pass  # j'aurais pu mettre ... mais bon