class MaxFlow:
    def __init__(self, V):
        self._init_variables(V)
    def _init_variables(self, V):
        self.V = V
        self.level = self._make_zero_list(V)
        self.iter = self._make_zero_list(V)
        self.edge = self._make_edge_list(V)
    def _make_zero_list(self, V):
        return [0]*V
    def _make_edge_list(self, V):
        return [[] for _ in range(V)]
    def add_edge(self, fr, to, cap):
        self._add_forward_edge(fr, to, cap)
        self._add_backward_edge(fr, to, cap)
    def _add_forward_edge(self, fr, to, cap):
        rev_idx = len(self.edge[to])
        self.edge[fr].append([to, cap, rev_idx])
    def _add_backward_edge(self, fr, to, cap):
        rev_idx = len(self.edge[fr]) - 1
        self.edge[to].append([fr, cap, rev_idx])
    def bfs(self, s):
        self._initialize_level(s)
        Q = self._init_queue(s)
        self._bfs_process(Q)
    def _initialize_level(self, s):
        self.level = self._make_minus_one_list(self.V)
        self.level[s] = 0
    def _make_minus_one_list(self, V):
        return [-1]*V
    def _init_queue(self, s):
        return [s]
    def _bfs_process(self, Q):
        while Q:
            v = self._pop_from_queue(Q)
            self._bfs_traverse_edges(Q, v)
    def _pop_from_queue(self, Q):
        return Q.pop()
    def _bfs_traverse_edges(self, Q, v):
        for to, cap, rev in self.edge[v]:
            if self._can_visit(to, cap):
                self._update_level(to, v)
                Q.append(to)
    def _can_visit(self, to, cap):
        return cap > 0 and self.level[to] < 0
    def _update_level(self, to, v):
        self.level[to] = self.level[v] + 1
    def dfs(self, v, t, f):
        return self._dfs_core(v, t, f)
    def _dfs_core(self, v, t, f):
        if v == t:
            return f
        for i in range(self.iter[v], len(self.edge[v])):
            to, cap, rev = self._get_current_edge(v, i)
            if self._can_advance(v, to, cap):
                d = self._dfs_core(to, t, min(f, cap))
                if self._found_path(d):
                    self._update_capacity(v, i, to, rev, d)
                    return d
            self.iter[v] = i
        return 0
    def _get_current_edge(self, v, i):
        return self.edge[v][i]
    def _can_advance(self, v, to, cap):
        return cap > 0 and self.level[v] < self.level[to]
    def _found_path(self, d):
        return d > 0
    def _update_capacity(self, v, i, to, rev, d):
        self.edge[v][i][1] -= d
        self.edge[to][rev][1] += d
    def maxFlow(self, s, t, INF=10**8):
        flow = self._init_flow()
        while True:
            self.bfs(s)
            if self._end_of_search(t): break
            self._init_iter()
            while True:
                f = self.dfs(s, t, INF)
                if self._no_more_augmenting_path(f): break
                flow = self._accumulate_flow(flow, f)
        return flow
    def _init_flow(self):
        return 0
    def _end_of_search(self, t):
        return self.level[t] < 0
    def _init_iter(self):
        self.iter = self._make_zero_list(self.V)
    def _no_more_augmenting_path(self, f):
        return f <= 0
    def _accumulate_flow(self, flow, f):
        return flow + f

def _read_N_M():
    return list(map(int, input().split()))
def _make_dir_list(N):
    return [[0]*N for _ in range(N)]
def _make_id_list(N):
    return [[0]*N for _ in range(N)]
def _init_maxflow(N):
    return MaxFlow(N)
def _read_edge():
    x, y = map(int, input().split())
    return x-1, y-1
def _mark_dir_and_id_lists(dir, id, y, x, i):
    dir[y][x] = 1
    id[y][x] = i+1
def _add_flow_edge(d, x, y):
    d.add_edge(x, y, 1)
def _read_S_T():
    return map(int, input().split())
def _print_max_flow(d, S, T):
    print(d.maxFlow(S-1, T-1))
def _collect_flow_edges(N, d, dir, id):
    ans = []
    for i in range(N):
        _collect_edges_for_vertex(i, d.edge[i], dir, id, ans)
    return ans
def _collect_edges_for_vertex(i, edge_list, dir, id, ans):
    for to, cap, rev in edge_list:
        if cap < 1 and dir[i][to]:
            ans.append(id[i][to])
def _sort_and_print_ans(ans):
    ans.sort()
    print(len(ans))
    if len(ans) > 0:
        print(*ans, sep='\n')

def main():
    N, M = _read_N_M()
    dir = _make_dir_list(N)
    id = _make_id_list(N)
    d = _init_maxflow(N)
    for i in range(M):
        x, y = _read_edge()
        _mark_dir_and_id_lists(dir, id, y, x, i)
        _add_flow_edge(d, x, y)
    S, T = _read_S_T()
    _print_max_flow(d, S, T)
    ans = _collect_flow_edges(N, d, dir, id)
    _sort_and_print_ans(ans)

main()