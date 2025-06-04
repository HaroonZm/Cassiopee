import collections

# fonctions utilitaires pour les listes
def plus_list(a, b):
    assert len(a) == len(b)
    # addition d’éléments, rien de fou
    return [aa + bb for aa, bb in zip(a, b)]

def minus_list(a, b):
    # soustraction, même principe hein...
    assert len(a) == len(b)
    return [aa - bb for aa, bb in zip(a, b)]

def gt_list(a, b):
    # comparaison lexicographique custom (sûrement pour les polynômes)
    assert len(a) == len(b)
    for aa, bb in zip(a, b):
        if aa != bb:
            return aa > bb
    return False

class MaxFlow:
    '''
    Basic Dinic implémentation (c’est un classique celui-là)  
    '''
    class Edge:
        def __init__(self, to, cap, rev):
            self.to = to
            self.cap = cap
            self.rev = rev  # indice de l’arc retour

    def __init__(self, V, D):
        self.V = V
        self.E = [[] for _ in range(V)]
        self.D = D
        # petite note: D est la dimension max des polynômes

    def add_edge(self, fr, to, cap):
        # Ajout d’arêtes bidirectionnelles
        self.E[fr].append(self.Edge(to, cap[:], len(self.E[to])))
        # l’arc retourné a une capacité nulle
        self.E[to].append(self.Edge(fr, [0 for _ in range(self.D)], len(self.E[fr]) - 1))

    def dinic(self, source, sink):
        # max-flow principal
        INF = [10**9] * self.D  # c’est un grand nombre, ça ira
        maxflow = [0] * self.D
        while True:
            self.bfs(source)
            if self.level[sink] < 0:
                # on n’atteint plus le puits, donc stop
                return maxflow
            self.itr = [0] * self.V
            while True:
                flow = self.dfs(source, sink, INF)
                if gt_list(flow, [0]*self.D):
                    maxflow = plus_list(maxflow, flow)
                else:
                    break

    def dfs(self, v, sink, flow):
        # DFS augmenté, on cherche des chemins
        if v == sink:
            return flow
        n = len(self.E[v])
        i = self.itr[v]
        while i < n:
            self.itr[v] = i
            e = self.E[v][i]
            if gt_list(e.cap, [0]*self.D) and self.level[v] < self.level[e.to]:
                # Choix du minimum pour la capacité passante
                if gt_list(flow, e.cap):
                    d = self.dfs(e.to, sink, e.cap)
                else:
                    d = self.dfs(e.to, sink, flow)
                if gt_list(d, [0]*self.D):
                    e.cap = minus_list(e.cap, d)
                    self.E[e.to][e.rev].cap = plus_list(self.E[e.to][e.rev].cap, d)
                    return d
            i += 1
        return [0]*self.D

    def bfs(self, start):
        # BFS classique
        que = collections.deque()
        self.level = [-1] * self.V
        que.append(start)
        self.level[start] = 0
        # On parcours
        while que:
            fr = que.popleft()
            for e in self.E[fr]:
                if gt_list(e.cap, [0]*self.D) and self.level[e.to] < 0:
                    self.level[e.to] = self.level[fr] + 1
                    que.append(e.to)

def to_poly(a, l):
    # J’aurais pu faire mieux, mais bon...
    if l == 0:
        return str(a)
    elif l == 1:
        return "{}x".format("" if a == 1 else a)
    else:
        return "{}x^{}".format("" if a == 1 else a, l)

while True:
    # on lit les entrées
    N_M = input().split()
    if not N_M:  # fail soft ?
        continue
    N, M = map(int, N_M)
    if N == 0 and M == 0:
        break
    mf = MaxFlow(N, 51)
    for _ in range(M):
        edge_info = input().split()
        u, v, p = edge_info[0], edge_info[1], edge_info[2]
        u = int(u)-1
        v = int(v)-1
        poly = [0]*51
        # Parsing polynôme (cette partie n’est pas très propre)
        for x in p.split('+'):
            try:
                num = int(x)
                poly[-1] = num
            except:
                # séparation du coefficient et du degré
                if 'x' not in x:
                    continue  # Oups
                ix = x.index('x')
                a = x[:ix]
                expr = x[ix+1:]
                if '^' in expr:
                    l = int(expr.strip('^'))
                    deg = l
                else:
                    deg = 1
                if a == '':
                    coeff = 1
                else:
                    try:
                        coeff = int(a)
                    except:
                        coeff = 1
                poly[50-deg+1] = coeff
        mf.add_edge(u, v, poly)
        mf.add_edge(v, u, poly)
    maxflow = mf.dinic(0, N-1)
    result = []
    for a, l in zip(maxflow, reversed(range(51))):
        if a:
            result.append(to_poly(a, l))
    ans = '+'.join(result)
    print(ans if ans else 0)