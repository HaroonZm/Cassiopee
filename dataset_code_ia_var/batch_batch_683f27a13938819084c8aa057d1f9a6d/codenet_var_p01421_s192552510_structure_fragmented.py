import collections

class MaxFlow:
    class Edge:
        def __init__(self, to, cap, rev):
            self.to = to
            self.cap = cap
            self.rev = rev

    def __init__(self, V):
        self.V = V
        self.E = self._create_empty_adj_list(V)

    def _create_empty_adj_list(self, V):
        return [[] for _ in range(V)]

    def add_edge(self, fr, to, cap):
        self._internal_add_edge(fr, to, cap, add_reverse=True)

    def _internal_add_edge(self, fr, to, cap, add_reverse):
        self._add_directed_edge(fr, to, cap)
        if add_reverse:
            self._add_reverse_edge(fr, to)

    def _add_directed_edge(self, fr, to, cap):
        self.E[fr].append(self.Edge(to, cap, len(self.E[to])))

    def _add_reverse_edge(self, fr, to):
        self.E[to].append(self.Edge(fr, 0, len(self.E[fr])-1))

    def dinic(self, source, sink, INF=10**9):
        maxflow = self._init_maxflow()
        while True:
            self._construct_level_graph(source)
            if self._is_sink_unreachable(sink):
                return maxflow
            self._init_iterators()
            maxflow = self._augment_flows(source, sink, INF, maxflow)

    def _init_maxflow(self):
        return 0

    def _construct_level_graph(self, source):
        self._reset_levels()
        self._bfs_fill_levels(source)

    def _reset_levels(self):
        self.level = [-1] * self.V

    def _bfs_fill_levels(self, start):
        que = collections.deque()
        que.append(start)
        self.level[start] = 0
        while que:
            self._bfs_expand_vertex(que)

    def _bfs_expand_vertex(self, que):
        fr = que.popleft()
        for e in self.E[fr]:
            if self._can_visit_bfs(e):
                self._set_level_and_enqueue(e, fr, que)

    def _can_visit_bfs(self, e):
        return e.cap > 0 and self.level[e.to] < 0

    def _set_level_and_enqueue(self, e, fr, que):
        self.level[e.to] = self.level[fr] + 1
        que.append(e.to)

    def _is_sink_unreachable(self, sink):
        return self.level[sink] < 0

    def _init_iterators(self):
        self.itr = [0] * self.V

    def _augment_flows(self, source, sink, INF, maxflow):
        while True:
            flow = self._get_flow(source, sink, INF)
            if flow > 0:
                maxflow += flow
            else:
                break
        return maxflow

    def _get_flow(self, source, sink, INF):
        return self._dfs(source, sink, INF)

    def _dfs(self, vertex, sink, flow):
        if self._is_at_sink(vertex, sink):
            return flow
        res = self._dfs_iterate_edges(vertex, sink, flow)
        return res

    def _is_at_sink(self, vertex, sink):
        return vertex == sink

    def _dfs_iterate_edges(self, vertex, sink, flow):
        for i in range(self.itr[vertex], len(self.E[vertex])):
            self.itr[vertex] = i
            e = self.E[vertex][i]
            if self._can_advance_dfs(vertex, e):
                d = self._dfs(e.to, sink, min(flow, e.cap))
                if self._is_positive_flow(d):
                    self._apply_flow(e, d)
                    return d
        return 0

    def _can_advance_dfs(self, vertex, e):
        return e.cap > 0 and self.level[vertex] < self.level[e.to]

    def _is_positive_flow(self, d):
        return d > 0

    def _apply_flow(self, e, d):
        e.cap -= d
        self.E[e.to][e.rev].cap += d

def read_input_header():
    return map(int, input().split())

def create_max_flow_instance(N):
    return MaxFlow(N)

def read_edge():
    return [int(x) - 1 for x in input().split()]

def register_edges(M, mf):
    rev_edge = []
    for i in range(M):
        s, t = read_edge()
        _add_edge_pair(mf, s, t)
        rev_edge.append(_form_rev_edge_tuple(i, t, mf))
    return rev_edge

def _add_edge_pair(mf, s, t):
    mf.add_edge(s, t, 1)
    mf.add_edge(t, s, 1)

def _form_rev_edge_tuple(i, t, mf):
    return (i + 1, t, len(mf.E[t]) - 1)

def read_source_sink():
    return [int(x) - 1 for x in input().split()]

def print_result(flow, ans):
    print(flow)
    print(len(ans))
    if ans:
        print(*ans, sep='\n')

def collect_answer_edges(rev_edge, mf):
    ans = []
    for i, t, idx in rev_edge:
        if _edge_used(t, idx, mf):
            ans.append(i)
    return ans

def _edge_used(t, idx, mf):
    e = mf.E[t][idx]
    return mf.E[e.to][e.rev].cap == 1

def main():
    N, M = read_input_header()
    mf = create_max_flow_instance(N)
    rev_edge = register_edges(M, mf)
    source, sink = read_source_sink()
    flow = mf.dinic(source, sink)
    ans = collect_answer_edges(rev_edge, mf)
    print_result(flow, ans)

main()