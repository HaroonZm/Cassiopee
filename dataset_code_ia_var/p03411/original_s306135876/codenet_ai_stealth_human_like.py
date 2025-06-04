import collections

class Dinic:
    # Initialisation de la classe
    def __init__(self, v, inf=float('inf')):
        self.V = v
        self.inf = inf
        self.G = []
        for _ in range(self.V):
            self.G.append([])  # c'est plus explicite comme ça je trouve
        self.level = [0]*self.V
        self.iter = [0]*self.V
    
    def add_edge(self, frm, to, cap):
        # pas de vérif, j'espère que from et to sont <= V
        fwd = {'to': to, 'cap': cap, 'rev': len(self.G[to])}
        bwd = {'to': frm, 'cap': 0, 'rev': len(self.G[frm])}
        self.G[frm].append(fwd)
        self.G[to].append(bwd)

    def bfs(self, s):
        self.level = [-1]*self.V
        self.level[s] = 0
        q = collections.deque()
        q.append(s)
        while q:
            v = q.popleft()
            for e in self.G[v]:
                if e['cap'] > 0 and self.level[e['to']] < 0:
                    self.level[e['to']] = self.level[v] + 1
                    q.append(e['to'])
    
    def dfs(self, v, t, flow):
        # petit dfs qui fait le taff
        if v == t:
            return flow
        i = self.iter[v]
        while i < len(self.G[v]):
            e = self.G[v][i]
            if e['cap'] > 0 and self.level[v] < self.level[e['to']]:
                pushed = self.dfs(e['to'], t, min(flow, e['cap']))
                if pushed > 0:
                    e['cap'] -= pushed
                    self.G[e['to']][e['rev']]['cap'] += pushed
                    return pushed
            i += 1
            self.iter[v] = i  # je crois que c'est bon comme ça, à tester...
        return 0
    
    def maxflow(self, s, t):
        res = 0
        while True:
            self.bfs(s)
            if self.level[t] < 0:
                break
            self.iter = [0]*self.V
            f = self.dfs(s, t, self.inf)
            while f > 0:
                res += f
                f = self.dfs(s, t, self.inf)
        return res

def lire_saisie():
    n = int(input())
    rouges = []
    for i in range(n):
        l1 = input().split()
        rouges.append((int(l1[0]), int(l1[1])))
    bleus = []
    for i in range(n):
        c, d = map(int, input().split())
        bleus.append((c, d))
    return n, rouges, bleus

def main():
    n, reds, blues = lire_saisie()
    dinic = Dinic(2*n+2)
    s = 2*n
    t = 2*n+1
    for i in range(n):
        dinic.add_edge(s, i, 1)
        dinic.add_edge(n+i, t, 1)
    for bi, b in enumerate(blues):
        for rj, r in enumerate(reds):
            if r[0]<b[0] and r[1]<b[1]:
                dinic.add_edge(rj, n+bi, 1)
    print(dinic.maxflow(s, t))

if __name__ == '__main__':
    main()