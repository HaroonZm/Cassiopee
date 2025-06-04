import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class Edge:
    def __init__(self, to, rev, capacity):
        self.to = to
        self.rev = rev
        self.capacity = capacity

class MaxFlow:
    def __init__(self, n):
        self.size = n
        self.graph = [[] for _ in range(n)]

    def add_edge(self, fr, to, cap):
        forward = Edge(to, len(self.graph[to]), cap)
        backward = Edge(fr, len(self.graph[fr]), 0)
        self.graph[fr].append(forward)
        self.graph[to].append(backward)

    def bfs(self, s, t, level):
        from collections import deque
        q = deque()
        level[s] = 0
        q.append(s)
        while q:
            v = q.popleft()
            for e in self.graph[v]:
                if e.capacity > 0 and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    q.append(e.to)
        return level[t] >= 0

    def dfs(self, v, t, upTo, iter_, level):
        if v == t:
            return upTo
        while iter_[v] < len(self.graph[v]):
            e = self.graph[v][iter_[v]]
            if e.capacity > 0 and level[v] < level[e.to]:
                d = self.dfs(e.to, t, min(upTo, e.capacity), iter_, level)
                if d > 0:
                    e.capacity -= d
                    self.graph[e.to][e.rev].capacity += d
                    return d
            iter_[v] += 1
        return 0

    def max_flow(self, s, t):
        flow = 0
        level = [-1]*self.size
        INF = 10**9
        while True:
            level = [-1]*self.size
            if not self.bfs(s, t, level):
                break
            iter_ = [0]*self.size
            while True:
                f = self.dfs(s, t, INF, iter_, level)
                if f == 0:
                    break
                flow += f
        return flow



class PersistentFlowSolver:
    def __init__(self, N, edges):
        self.N = N
        self.edges = edges
        # We build a unique index scheme: since edges are undirected, each edge is represented as two directed edges with capacity 1.
        # But we do not want to rebuild max flow from scratch for each query.

        # Unfortunately, we must answer Q=10^5 queries which each ask for min cut edge count separating two nodes a,b.
        # Min-cut between node u and v in undirected graph equals the global min s-t cut.

        # Given large constraints, naive maxflow per query is impossible.
        # Solution: Build Gomory-Hu Tree, which represents all min s-t cuts for every pair.

        # Let's build a Gomory-Hu Tree to answer queries efficiently.

        self.gomory_hu_tree = [[] for _ in range(N)]
        self.parent = [0]*N
        self.mincut = [0]*N
        self.build_gomory_hu_tree()

    def build_gomory_hu_tree(self):
        # Build adjacency for maxflow
        N = self.N
        # Convert undirected edges with capacity 1 for both directions
        graph = [[] for _ in range(N)]
        for u,v in self.edges:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)

        parent = [0]*N
        mincut = [0]*N
        for i in range(1, N):
            # Build flow network for each step
            mf = MaxFlow(N)
            for u in range(N):
                for w in graph[u]:
                    mf.add_edge(u, w, 1)
            flow = mf.max_flow(i, parent[i])
            mincut[i] = flow

            # BFS to find partition for next parent set
            from collections import deque
            visited = [False]*N
            queue = deque()
            queue.append(i)
            visited[i] = True
            while queue:
                u = queue.popleft()
                for e in mf.graph[u]:
                    if e.capacity > 0 and not visited[e.to]:
                        visited[e.to] = True
                        queue.append(e.to)

            for j in range(i+1, N):
                if parent[j] == parent[i] and visited[j]:
                    parent[j] = i

        self.parent = parent
        self.mincut = mincut
        # Build tree edges
        for i in range(1, N):
            p = parent[i]
            w = mincut[i]
            self.gomory_hu_tree[p].append((i, w))
            self.gomory_hu_tree[i].append((p, w))

    def prepare_lca(self):
        from math import log2
        N = self.N
        LOG = max(1,(N-1).bit_length())
        self.LOG = LOG
        self.depth = [0]*N
        self.par = [[-1]*N for _ in range(LOG)]
        self.mincost = [[10**9]*N for _ in range(LOG)]

        def dfs(v, p, d):
            self.depth[v] = d
            for to, w in self.gomory_hu_tree[v]:
                if to == p:
                    continue
                self.par[0][to] = v
                self.mincost[0][to] = w
                dfs(to, v, d+1)
        dfs(0, -1, 0)

        for k in range(LOG-1):
            for v in range(N):
                if self.par[k][v] < 0:
                    self.par[k+1][v] = -1
                    self.mincost[k+1][v] = self.mincost[k][v]
                else:
                    self.par[k+1][v] = self.par[k][self.par[k][v]]
                    self.mincost[k+1][v] = min(self.mincost[k][v], self.mincost[k][self.par[k][v]])

    def lca_min_edge_cut(self, u, v):
        # u,v 0-based
        if u == v:
            return 0
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        res = 10**9
        # Lift u up to depth v
        for k in reversed(range(self.LOG)):
            if self.par[k][u]>=0 and self.depth[self.par[k][u]] >= self.depth[v]:
                res = min(res, self.mincost[k][u])
                u = self.par[k][u]
        if u == v:
            return res
        for k in reversed(range(self.LOG)):
            if self.par[k][u] != self.par[k][v]:
                res = min(res, self.mincost[k][u])
                res = min(res, self.mincost[k][v])
                u = self.par[k][u]
                v = self.par[k][v]
        # now one step up
        res = min(res, self.mincost[0][u])
        res = min(res, self.mincost[0][v])
        return res


class NamoCutSolver:
    class SolverInterface:
        def solve(self):
            raise NotImplementedError

    class InputProcessor(SolverInterface):
        def __init__(self, solver):
            self.solver = solver
            self.N = 0
            self.edges = []
            self.Q = 0
            self.queries = []

        def read(self):
            self.N = int(input())
            self.edges = [tuple(map(int, input().split())) for _ in range(self.N)]
            self.Q = int(input())
            self.queries = [tuple(map(int, input().split())) for _ in range(self.Q)]
            self.solver.N = self.N
            self.solver.edges = self.edges
            self.solver.Q = self.Q
            self.solver.queries = self.queries

        def solve(self):
            self.read()
            self.solver.prepare()

    class SolverCore(SolverInterface):
        def __init__(self):
            self.N = 0
            self.edges = []
            self.Q = 0
            self.queries = []
            self.ght_solver = None
        def prepare(self):
            self.ght_solver = PersistentFlowSolver(self.N, self.edges)
            self.ght_solver.prepare_lca()
        def solve(self):
            out = []
            for a,b in self.queries:
                res = self.ght_solver.lca_min_edge_cut(a-1,b-1)
                out.append(str(res))
            print("\n".join(out))



def main():
    core_solver = NamoCutSolver.SolverCore()
    input_processor = NamoCutSolver.InputProcessor(core_solver)
    input_processor.solve()
    core_solver.solve()

if __name__ == "__main__":
    main()