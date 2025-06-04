import sys
sys.setrecursionlimit(1000000)

def set_recursion_limit():
    sys.setrecursionlimit(1000000)

def create_graph(n):
    return {}


def add_edge_to_graph(g, frm, to):
    if frm in g:
        g[frm].append(to)
    else:
        g[frm] = [to]

def create_counts(group_num):
    return [0] * group_num

def create_groups(group_num):
    return [[] for _ in range(group_num)]

def listmap_int_split(n, input):
    return [list(map(int, input().split())) for _ in range(n)]

def read_N_D(input):
    return list(map(int, input().split()))

def abs_diff(a, b):
    return abs(a - b)

class SCCGraph:
    def __init__(self, n):
        self._n = n
        self.g = create_graph(n)

    def num_vertices(self):
        return self._n

    def add_edge(self, frm, to):
        add_edge_to_graph(self.g, frm, to)

    def _dfs(self, dfs, v, now_ord, group_num, visited, low, ord, ids):
        low[v] = ord[v] = now_ord
        now_ord += 1
        visited.append(v)
        if v in self.g:
            for to in self.g[v]:
                if ord[to] == -1:
                    now_ord, group_num = dfs(dfs, to, now_ord, group_num, visited, low, ord, ids)
                    low[v] = min(low[v], low[to])
                else:
                    low[v] = min(low[v], ord[to])
        if low[v] == ord[v]:
            while True:
                u = visited.pop()
                ord[u] = self._n
                ids[u] = group_num
                if u == v: break
            group_num += 1
        return now_ord, group_num

    def _init_low_ord_ids(self):
        low = [0] * self._n
        ord = [-1] * self._n
        ids = [0] * self._n
        return low, ord, ids

    def _finalize_ids(self, ids, group_num):
        for i in range(self._n):
            ids[i] = group_num - 1 - ids[i]
        return ids

    def scc_ids(self):
        now_ord = 0
        group_num = 0
        visited = []
        low, ord, ids = self._init_low_ord_ids()
        for i in range(self._n):
            if ord[i] == -1:
                now_ord, group_num = self._dfs(self._dfs, i, now_ord, group_num, visited, low, ord, ids)
        ids = self._finalize_ids(ids, group_num)
        return group_num, ids

    def scc(self):
        group_num, ids = self.scc_ids()
        counts = create_counts(group_num)
        for x in ids:
            counts[x] += 1
        groups = create_groups(group_num)
        for i in range(self._n):
            groups[ids[i]].append(i)
        return groups

    class edge:
        def __init__(self, frm, to):
            self.frm = frm
            self.to = to

def create_twosat_answer_list(n):
    return [False] * n

class TwoSat:
    def __init__(self, n):
        self._n = n
        self._answer = create_twosat_answer_list(n)
        self.scc = SCCGraph(2 * n)

    def _encode(self, i, f):
        return 2 * i + (not f)

    def _encode_neg(self, i, f):
        return 2 * i + (f)

    def add_clause(self, i, f, j, g):
        self.scc.add_edge(self._encode(i, f), self._encode_neg(j, g))
        self.scc.add_edge(self._encode(j, g), self._encode_neg(i, f))

    def _update_answer(self, id):
        for i in range(self._n):
            if id[2 * i] == id[2 * i + 1]:
                return False
            self._answer[i] = id[2 * i] < id[2 * i + 1]
        return True

    def satisfiable(self):
        _, id = self.scc.scc_ids()
        return self._update_answer(id)

    def answer(self):
        return self._answer

def at_least_one_different(ts, i, j, xi, yi, xj, yj, D):
    if abs_diff(xi, xj) < D:
        ts.add_clause(i, False, j, False)
    if abs_diff(xi, yj) < D:
        ts.add_clause(i, False, j, True)
    if abs_diff(yi, xj) < D:
        ts.add_clause(i, True, j, False)
    if abs_diff(yi, yj) < D:
        ts.add_clause(i, True, j, True)

def process_pairs(N, XY, D, ts):
    for i in range(N):
        for j in range(i + 1, N):
            xi, yi = XY[i]
            xj, yj = XY[j]
            at_least_one_different(ts, i, j, xi, yi, xj, yj, D)

def check_and_output(ts, XY, N):
    if not ts.satisfiable():
        print_result_no_and_exit()
    print_result_yes()
    answer = ts.answer()
    output_coordinates(answer, XY, N)

def print_result_no_and_exit():
    print("No")
    exit()

def print_result_yes():
    print("Yes")

def output_coordinates(answer, XY, N):
    for i in range(N):
        x, y = XY[i]
        if answer[i]:
            print(x)
        else:
            print(y)

def main():
    input = sys.stdin.readline
    N, D = read_N_D(input)
    XY = listmap_int_split(N, input)
    ts = TwoSat(N)
    process_pairs(N, XY, D, ts)
    check_and_output(ts, XY, N)

main()