import collections

def plus_list(A, B):
    # Addition élément par élément
    result = []
    for i in range(len(A)):
        result.append(A[i] + B[i])
    return result

def minus_list(A, B):
    # Soustraction élément par élément
    result = []
    for i in range(len(A)):
        result.append(A[i] - B[i])
    return result

def gt_list(A, B):
    # Renvoie True si A > B dans l'ordre lexicographique
    for i in range(len(A)):
        if A[i] != B[i]:
            return A[i] > B[i]
    return False

class Edge:
    def __init__(self, to, cap, rev):
        self.to = to
        self.cap = cap
        self.rev = rev

class MaxFlow:
    def __init__(self, V, D):
        # V : nombre de sommets ; D : degré maximal du polynôme
        self.V = V
        self.E = []
        for _ in range(V):
            self.E.append([])
        self.D = D

    def add_edge(self, fr, to, cap):
        # Ajoute arête avec capacité cap (polynôme) de fr à to
        self.E[fr].append(Edge(to, cap, len(self.E[to])))
        # Ajoute arête retour de capacité 0
        self.E[to].append(Edge(fr, [0]*self.D, len(self.E[fr])-1))

    def bfs(self, start):
        self.level = [-1]*self.V
        que = collections.deque()
        que.append(start)
        self.level[start] = 0
        while que:
            u = que.popleft()
            for e in self.E[u]:
                if gt_list(e.cap, [0]*self.D) and self.level[e.to] == -1:
                    self.level[e.to] = self.level[u]+1
                    que.append(e.to)

    def dfs(self, v, t, upTo):
        # Cherche un chemin augmentant
        if v == t:
            return upTo
        while self.itr[v] < len(self.E[v]):
            i = self.itr[v]
            e = self.E[v][i]
            self.itr[v] += 1
            if gt_list(e.cap, [0]*self.D) and self.level[v] < self.level[e.to]:
                new_flow = []
                for x in range(self.D):
                    new_flow.append(min(upTo[x], e.cap[x]))
                if gt_list(upTo, e.cap):
                    d = self.dfs(e.to, t, e.cap)
                else:
                    d = self.dfs(e.to, t, upTo)
                if gt_list(d, [0]*self.D):
                    e.cap = minus_list(e.cap, d)
                    self.E[e.to][e.rev].cap = plus_list(self.E[e.to][e.rev].cap, d)
                    return d
        return [0]*self.D

    def dinic(self, s, t):
        INF = [10**9]*self.D
        maxflow = [0]*self.D
        while True:
            self.bfs(s)
            if self.level[t] == -1:
                break
            self.itr = [0]*self.V
            while True:
                flow = self.dfs(s, t, INF)
                if gt_list(flow, [0]*self.D):
                    maxflow = plus_list(maxflow, flow)
                else:
                    break
        return maxflow

def to_poly(a, l):
    # Convertit un coefficient et un exposant en chaîne pour polynôme
    if a == 0:
        return ""
    if l == 0:
        return str(a)
    elif l == 1:
        if a == 1:
            return "x"
        else:
            return str(a) + "x"
    else:
        if a == 1:
            return "x^" + str(l)
        else:
            return str(a) + "x^" + str(l)

while True:
    try:
        N, M = map(int, input().split())
    except:
        break
    if N == 0 and M == 0:
        break
    mf = MaxFlow(N, 51)
    for _ in range(M):
        u, v, p = input().split()
        u = int(u)-1
        v = int(v)-1
        poly = [0]*51
        terms = p.split('+')
        for x in terms:
            if 'x' not in x:
                # C'est la constante
                num = int(x)
                poly[-1] = num
            else:
                if '^' in x:
                    # forme ax^l
                    parts = x.split('x')
                    coef = parts[0]
                    if coef == '':
                        coef = '1'
                    expo = parts[1][1:] # enlever '^'
                    poly[-int(expo)-1] = int(coef)
                else:
                    # forme ax
                    parts = x.split('x')
                    coef = parts[0]
                    if coef == '':
                        coef = '1'
                    poly[-2] = int(coef)
        mf.add_edge(u, v, poly)
        mf.add_edge(v, u, poly)
    maxflow = mf.dinic(0, N-1)
    result = []
    for a, l in zip(maxflow, reversed(range(51))):
        s = to_poly(a, l)
        if s:
            result.append(s)
    if result:
        print('+'.join(result))
    else:
        print(0)