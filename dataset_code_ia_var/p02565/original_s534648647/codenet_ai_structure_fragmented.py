import sys
def set_input_and_recursionlimit():
    import sys
    input_func = sys.stdin.readline
    sys.setrecursionlimit(1000000)
    return input_func
input = set_input_and_recursionlimit()

def create_graph(n):
    return [[] for _ in range(n)]

def create_bool_list(n):
    return [False]*n

def should_skip(fr, to):
    return fr == to

def append_edge(graph, graph_rev, fr, to):
    graph[fr].append(to)
    graph_rev[to].append(fr)

def set_false_list(lst, n):
    for i in range(n):
        lst[i] = False

def recursive_dfs(node, graph, already, order):
    already[node] = True
    for n in graph[node]:
        if already[n]:
            continue
        recursive_dfs(n, graph, already, order)
    order.append(node)

def first_dfs_main(already, n, graph, order):
    set_false_list(already, n)
    order.clear()
    for i in range(n):
        if already[i] == False:
            recursive_dfs(i, graph, already, order)

def reverse_order(order):
    return list(reversed(order))

def second_dfs_main(already, order, graph_rev, ans):
    set_false_list(already, len(order))
    res = []
    for n in reversed(order):
        if already[n]:
            continue
        already[n] = True
        group = []
        recursive_dfs(n, graph_rev, already, group)
        group.reverse()
        res.append(group)
    ans.clear()
    ans.extend(res)

class SCC:
    def __init__(self, n):
        self.n = n
        self.graph = create_graph(n)
        self.graph_rev = create_graph(n)
        self.already = create_bool_list(n)
        self.order = []
        self.ans = []

    def add_edge(self, fr, to):
        if should_skip(fr, to):
            return
        append_edge(self.graph, self.graph_rev, fr, to)

    def dfs(self, node, graph):
        recursive_dfs(node, graph, self.already, self.order)

    def first_dfs(self):
        first_dfs_main(self.already, self.n, self.graph, self.order)

    def second_dfs(self):
        self.already = create_bool_list(self.n)
        res = []
        for n in reversed(self.order):
            if self.already[n]:
                continue
            self.already[n] = True
            group = []
            recursive_dfs(n, self.graph_rev, self.already, group)
            group.reverse()
            res.append(group)
        self.ans = res

    def scc(self):
        self.first_dfs()
        self.second_dfs()
        return self.ans

def uf_init(n):
    return [-1] * (n+1)

def uf_find(x, par):
    if par[x] < 0:
        return x
    else:
        par[x] = uf_find(par[x], par)
        return par[x]

def uf_union(x, y, par):
    x = uf_find(x, par)
    y = uf_find(y, par)
    if x == y:
        return
    if par[x] > par[y]:
        x, y = y, x
    par[x] += par[y]
    par[y] = x

def uf_same(x, y, par):
    return uf_find(x, par) == uf_find(y, par)

def uf_size(x, par):
    return -par[uf_find(x, par)]

def uf_members(x, par, n):
    root = uf_find(x, par)
    return [i for i in range(n) if root == uf_find(i, par)]

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = uf_init(n)

    def find(self, x):
        return uf_find(x, self.par)

    def union(self, x, y):
        uf_union(x, y, self.par)

    def same(self, x, y):
        return uf_same(x, y, self.par)

    def size(self, x):
        return uf_size(x, self.par)

    def members(self, x):
        return uf_members(x, self.par, self.n)

def twosat_scc(ts):
    return ts.scc.scc()

def ts_union_prepare(ts):
    for v in ts.res:
        if len(v) == 1:
            continue
        for i in range(len(v)-1):
            ts.union.union(v[i], v[i+1])

def ts_judge_main(ts):
    for i in range(ts.n):
        if ts.union.same(i, i+ts.n):
            return False
    return True

class TwoSat:
    def __init__(self, n):
        self.n = n
        self.scc = SCC(n*2)
        self.union = UnionFind(n*2)
        self.res = []

    def add_sat(self, fr, to):
        self.scc.add_edge(fr, to)

    def scc_prepare(self):
        return twosat_scc(self)

    def union_prepare(self):
        ts_union_prepare(self)

    def ts_judge(self):
        return ts_judge_main(self)

    def judge(self):
        self.res = self.scc_prepare()
        self.union_prepare()
        return self.ts_judge()

def input_ints():
    return list(map(int, input().split()))

def flags_input(n):
    flag = [None]*n
    for i in range(n):
        x, y = map(int, input().split())
        flag[i] = (x, y)
    return flag

def add_manual_edges(ts, n):
    for i in range(n):
        ts.add_sat(n*3+i, i)
        ts.add_sat(n*2+i, n+i)

def distance_violates(x1, x2, d):
    return abs(x1-x2) < d

def ts_edges_logic(ts, flag, n, d):
    for i in range(n):
        for j in range(i+1, n):
            xi, yi = flag[i]
            xj, yj = flag[j]
            if distance_violates(xi, xj, d):
                ts.add_sat(i, n*2+j)
                ts.add_sat(j, n*2+i)
                ts.add_sat(i, n+j)
                ts.add_sat(j, n+i)
            if distance_violates(xi, yj, d):
                ts.add_sat(i, j)
                ts.add_sat(i, n*3+j)
                ts.add_sat(n+j, n+i)
                ts.add_sat(n+j, n*2+i)
            if distance_violates(yi, xj, d):
                ts.add_sat(j, i)
                ts.add_sat(j, n*3+i)
                ts.add_sat(n+i, n+j)
                ts.add_sat(n+i, n*2+j)
            if distance_violates(yi, yj, d):
                ts.add_sat(i+n, j)
                ts.add_sat(i+n, j+n*3)
                ts.add_sat(j+n, i)
                ts.add_sat(j+n, i+n*3)

def output_yes_no(val):
    print("Yes" if val else "No")

def assign_used(ts, n):
    used = [-1]*n
    count = 0
    for lis in reversed(ts.res):
        for v in lis:
            if v >= n*2:
                continue
            index = v if v < n else v - n
            if used[index] == -1:
                count += 1
                used[index] = v//n
            if count == n:
                break
    return used

def output_used(flag, used):
    for i in range(len(used)):
        print(flag[i][used[i]])

def main_read():
    n, d = input_ints()
    return n, d

def main_core(ts, flag, n, d):
    add_manual_edges(ts, n)
    ts_edges_logic(ts, flag, n, d)

def main_decision(ts):
    ans = ts.judge()
    output_yes_no(ans)
    return ans

def run_core(flag, ts, n, d):
    main_core(ts, flag, n, d)
    return main_decision(ts)

def main():
    n, d = main_read()
    ts = TwoSat(n*2)
    flag = flags_input(n)
    ans = run_core(flag, ts, n, d)
    if ans:
        used = assign_used(ts, n)
        output_used(flag, used)

if __name__ == "__main__":
    main()