class MaxFlowSolver:
    class Edge:
        __slots__ = ('to', 'rev', 'capacity', 'original_capacity')

        def __init__(self, to, rev, capacity):
            self.to = to
            self.rev = rev
            self.capacity = capacity
            self.original_capacity = capacity

    def __init__(self, n: int):
        self.n = n
        self.graph = [[] for _ in range(n)]

    def add_edge(self, frm: int, to: int, capacity: int):
        forward = self.Edge(to, len(self.graph[to]), capacity)
        backward = self.Edge(frm, len(self.graph[frm]), 0)
        self.graph[frm].append(forward)
        self.graph[to].append(backward)

    def bfs(self, s: int, t: int) -> list:
        level = [-1] * self.n
        level[s] = 0
        queue = [s]
        for v in queue:
            for i, e in enumerate(self.graph[v]):
                if e.capacity > 0 and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    queue.append(e.to)
        return level

    def dfs(self, v: int, t: int, f: int, level: list, iter_: list) -> int:
        if v == t:
            return f
        while iter_[v] < len(self.graph[v]):
            e = self.graph[v][iter_[v]]
            if e.capacity > 0 and level[v] < level[e.to]:
                d = self.dfs(e.to, t, min(f, e.capacity), level, iter_)
                if d > 0:
                    e.capacity -= d
                    self.graph[e.to][e.rev].capacity += d
                    return d
            iter_[v] += 1
        return 0

    def max_flow(self, s: int, t: int) -> int:
        flow = 0
        INF = 10**9
        while True:
            level = self.bfs(s, t)
            if level[t] < 0:
                return flow
            iter_ = [0] * self.n
            while True:
                f = self.dfs(s, t, INF, level, iter_)
                if f == 0:
                    break
                flow += f

    def reset(self):
        for edges in self.graph:
            for e in edges:
                e.capacity = e.original_capacity

class GraphTransformer:
    def __init__(self, N, roads):
        self.N = N
        self.roads = roads

    def to_maxflow_graph(self):
        solver = MaxFlowSolver(self.N)
        for a, b in self.roads:
            solver.add_edge(a-1, b-1, 1)
        return solver

class RoadReversalOptimizer:
    def __init__(self, N, M, S, T, roads):
        self.N = N
        self.M = M
        self.S = S - 1
        self.T = T - 1
        self.roads = roads
        self.base_solver = None
        self.base_max_flow = None

    def compute_base_max_flow(self):
        transformer = GraphTransformer(self.N, self.roads)
        solver = transformer.to_maxflow_graph()
        self.base_solver = solver
        self.base_max_flow = solver.max_flow(self.S, self.T)

    def reconstruct_flows(self):
        # flows used in the initial graph after max_flow calculation
        # reconstruct residual capacities accordingly, to allow increment after reversals
        # But Dinic has residual graph, capacities left, initial capacity 1, so we find used edges by capacity < 1
        # We'll not use this for this solution to avoid complexity in reconstruction; just recompute each time.
        pass

    def reversed_road_max_flow(self, rev_edge_idx):
        # create new graph with reversed edge at rev_edge_idx
        a, b = self.roads[rev_edge_idx]
        solver = MaxFlowSolver(self.N)
        for i, (u, v) in enumerate(self.roads):
            if i == rev_edge_idx:
                solver.add_edge(v-1, u-1, 1)  # reversed edge
            else:
                solver.add_edge(u-1, v-1, 1)
        return solver.max_flow(self.S, self.T)

    def analyze(self):
        self.compute_base_max_flow()
        improved_max_flow = self.base_max_flow
        candidates = []
        # If base max flow is zero, try all edges anyway
        for idx in range(self.M):
            new_flow = self.reversed_road_max_flow(idx)
            if new_flow > improved_max_flow:
                improved_max_flow = new_flow
                candidates = [idx]
            elif new_flow == improved_max_flow and new_flow > self.base_max_flow:
                candidates.append(idx)
        if improved_max_flow == self.base_max_flow:
            return self.base_max_flow, 0
        else:
            return improved_max_flow, len(candidates)

class InputProcessor:
    def __init__(self):
        self.datasets = []

    def parse(self):
        import sys
        for line in sys.stdin:
            if not line.strip():
                continue
            N, M, S, T = map(int, line.split())
            if N == 0 and M == 0 and S == 0 and T == 0:
                break
            roads = []
            for _ in range(M):
                a, b = map(int, sys.stdin.readline().split())
                roads.append((a,b))
            self.datasets.append( (N,M,S,T,roads) )

class OutputPresenter:
    @staticmethod
    def present(results):
        for maxflow, cnt in results:
            print(maxflow, cnt)

class ICPCTransportSolver:
    def __init__(self):
        self.processor = InputProcessor()

    def solve(self):
        self.processor.parse()
        results = []
        for (N,M,S,T,roads) in self.processor.datasets:
            optimizer = RoadReversalOptimizer(N,M,S,T,roads)
            result = optimizer.analyze()
            results.append(result)
        OutputPresenter.present(results)

if __name__ == "__main__":
    ICPCTransportSolver().solve()