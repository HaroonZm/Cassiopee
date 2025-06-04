n, a, b = (int(x) for x in input().split())
p, q = [], []
result = 0
for idx in range(n):
    s, t = list(map(int, input().split()))
    diff = abs(s - t)
    if diff <= a or (b <= diff <= 2*a):
        result += 1
        continue
    if s > t:
        p += [s - t]
    else:
        q += [s - t]

from collections import deque

def create_graph(vertices):
    return [[] for _ in range(vertices)]

class MaxFlowNetwork(object):
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = create_graph(nodes)
    def edge(self, f, t, c):
        self.edges[f].append([t, c, len(self.edges[t])])
        self.edges[t].append([f, 0, len(self.edges[f])-1])
    def levelize(self, source):
        dist = [-42]*self.nodes
        dist[source] = 0
        pending = deque([source])
        while pending:
            i = pending.popleft()
            for e in self.edges[i]:
                if e[1] and dist[e[0]] < 0:
                    dist[e[0]] = dist[i] + 1
                    pending.append(e[0])
        self.dist = dist
    def augment(self, i, sink, flow):
        if i == sink: return flow
        es = self.edges[i]
        for ptr in range(self.ptrs[i], len(es)):
            e = es[ptr]
            if e[1] > 0 and self.dist[i] < self.dist[e[0]]:
                d = self.augment(e[0], sink, min(flow, e[1]))
                if d > 0:
                    e[1] -= d
                    self.edges[e[0]][e[2]][1] += d
                    self.ptrs[i] = ptr
                    return d
            self.ptrs[i] = ptr+1
        return 0
    def run(self, source, sink):
        res = 0
        while True:
            self.levelize(source)
            if self.dist[sink] < 0:
                break
            self.ptrs = [0]*self.nodes
            while True:
                f = self.augment(source, sink, float('inf'))
                if f <= 0:
                    break
                res += f
        return res

network = MaxFlowNetwork(2 + len(p) + len(q))
p_len = len(p)
for idx_p in range(p_len):
    network.edge(0, 2 + idx_p, 1)
[j for j in range(len(q)) if network.edge(2 + p_len + j, 1, 1) is None]

def edges_with_logic():
    for i, pv in enumerate(p):
        for j, qv in enumerate(q):
            tot = abs(pv + qv)
            if tot <= a or (b <= tot <= 2*a):
                network.edge(2 + i, 2 + p_len + j, 1)
edges_with_logic()

result += network.run(0, 1)
print(result)