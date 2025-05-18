class CSR:
    def __init__(self, n: int, edges: list):
        self.start = [0] * (n+1)
        self.elist = [0] * len(edges)
        for e in edges:
            self.start[e[0]+1] += 1
        
        for i in range(1, n+1):
            self.start[i] += self.start[i-1]
        
        counter = self.start[::] # copy
        for e in edges:
            self.elist[counter[e[0]]] = e[1]
            counter[e[0]] += 1

class SccGraph:
    def __init__(self, n: int = 0):
        self.__n = n
        self.__edges = []
    
    def __len__(self):
        return self.__n
    
    def add_edge(self, s: int, t: int):
        assert 0 <= s < self.__n and 0 <= t < self.__n
        self.__edges.append([s, t])
    
    def __scc_ids(self):
        g = CSR(self.__n, self.__edges)
        now_ord = group_num = 0
        visited = []
        low = [0] * self.__n
        order = [-1] * self.__n
        ids = [0] * self.__n
        parent = [-1] * self.__n
        for root in range(self.__n):
            if order[root] == -1:
                stack = [root, root]
                while stack:
                    v = stack.pop()
                    if order[v] == -1:
                        visited.append(v)
                        low[v] = order[v] = now_ord
                        now_ord += 1
                        for i in range(g.start[v], g.start[v+1]):
                            t = g.elist[i]
                            if order[t] == -1:
                                stack += [t, t]
                                parent[t] = v
                            else:
                                low[v] = min(low[v], order[t])
                    
                    else:
                        if low[v] == order[v]:
                            while True:
                                u = visited.pop()
                                order[u] = self.__n
                                ids[u] = group_num
                                if u == v:
                                    break
                                
                            group_num += 1
                        
                        if parent[v] != -1:
                            low[parent[v]] = min(low[parent[v]], low[v])
        
        for i, x in enumerate(ids):
            ids[i] = group_num - 1 - x
        
        return group_num, ids
    
    def scc(self):
        group_num, ids = self.__scc_ids()
        counts = [0] * group_num
        for x in ids:
            counts[x] += 1
        
        groups = [[] for _ in range(group_num)]
        for i, x in enumerate(ids):
            groups[x].append(i)
        
        return groups

N, M = map(int, input().split())
sg = SccGraph(N)

for _ in range(M):
    a, b = map(int, input().split())
    sg.add_edge(a, b)

scc = sg.scc()
print(len(scc))
for group in scc:
    print(*([len(group)] + group))