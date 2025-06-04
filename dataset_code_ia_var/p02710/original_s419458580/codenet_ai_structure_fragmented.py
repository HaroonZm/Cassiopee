import sys

def set_recursion_limit():
    sys.setrecursionlimit(10**8)

def get_input_function():
    return sys.stdin.readline

def read_n(input_func):
    return int(input_func())

def read_c(input_func):
    return list(map(int, input_func().split()))

def read_ab(input_func, n):
    return [tuple(map(int, input_func().split())) for _ in range(n-1)]

def build_empty_graph(n):
    return [[] for _ in range(n)]

def build_graph_edges(es, AB):
    for a, b in AB:
        append_edge(es, a-1, b-1)

def append_edge(es, a, b):
    es[a].append(b)
    es[b].append(a)

def build_color_nodes(cs, C):
    for i, c in enumerate(C):
        assign_color_node(cs, c-1, i)

def assign_color_node(cs, color, i):
    cs[color].append(i)

def prepare_tin_tout(N):
    return ([-1]*N, [-1]*N)

def prepare_k():
    return [0]

def run_dfs(N, es, tin, tout, k_holder):
    dfs(0, -1, es, tin, tout, k_holder)

def dfs(v, p, es, tin, tout, k_holder):
    mark_tin(tin, v, k_holder)
    increase_k(k_holder)
    for to in es[v]:
        if is_parent(to, p): continue
        dfs(to, v, es, tin, tout, k_holder)
    mark_tout(tout, v, k_holder)

def mark_tin(tin, v, k_holder):
    tin[v] = k_holder[0]

def increase_k(k_holder):
    k_holder[0] += 1

def is_parent(to, p):
    return to == p

def mark_tout(tout, v, k_holder):
    tout[v] = k_holder[0]

class BinaryIndexedTree:
    def __init__(self, size):
        self.N = size
        self.bit = [0]*(size+1)

    def add(self, x, w):
        x += 1
        while x <= self.N:
            self.bit[x] += w
            x += (x & -x)

    def _sum(self, x):
        ret = 0
        while x > 0:
            ret += self.bit[x]
            x -= (x & -x)
        return ret

    def sum(self, l, r):
        return self._sum(r) - self._sum(l)

    def __str__(self):
        arr = [self.sum(i, i+1) for i in range(self.N)]
        return str(arr)

def init_bit(tree, N):
    for i in range(N):
        tree.add(i, 1)

def get_whole(N):
    return N*(N+1)//2

def sort_color_nodes(cs, i, tin):
    cs[i].sort(key=lambda x: -tin[x])

def calc_components(cs, i, es, tin, tout, bit, N):
    ans = get_whole(N)
    sort_color_nodes(cs, i, tin)
    history = []
    for v in cs[i]:
        cnt, hlist = process_vertex_components(v, es, tin, tout, bit)
        ans, history = subtract_components(ans, v, cnt, es, tin, tout, bit, history, hlist)
    pn, ans = handle_remaining_subtree(bit, N, ans)
    restore_bit_state(bit, history)
    return ans

def process_vertex_components(v, es, tin, tout, bit):
    cnt = 1
    hlist = []
    for to in es[v]:
        if tin[to] < tin[v]: continue
        num = bit.sum(tin[to], tout[to])
        hlist.append(num)
    return cnt, hlist

def subtract_components(ans, v, cnt, es, tin, tout, bit, history, hlist):
    cnt_local = cnt
    for ind, to in enumerate(es[v]):
        if tin[to] < tin[v]: continue
        num = hlist[ind]
        ans -= num*(num+1)//2
        cnt_local += num
    bit.add(tin[v], -cnt_local)
    history.append((tin[v], cnt_local))
    return ans, history

def handle_remaining_subtree(bit, N, ans):
    pn = bit.sum(0, N)
    ans -= pn*(pn+1)//2
    return pn, ans

def restore_bit_state(bit, history):
    for a, b in history:
        bit.add(a, b)

def solve_all(N, cs, es, tin, tout, bit):
    result = []
    for i in range(N):
        r = solve_for_color(cs, i, es, tin, tout, bit, N)
        result.append(r)
    return result

def solve_for_color(cs, i, es, tin, tout, bit, N):
    ans = get_whole(N)
    cs[i].sort(key=lambda x: -tin[x])
    history = []
    for v in cs[i]:
        cnt = 1
        for to in es[v]:
            if tin[to] < tin[v]:
                continue
            num = bit.sum(tin[to], tout[to])
            ans -= num*(num+1)//2
            cnt += num
        bit.add(tin[v], -cnt)
        history.append((tin[v], cnt))
    pn = bit.sum(0, N)
    ans -= pn*(pn+1)//2
    for a, b in history:
        bit.add(a, b)
    return ans

def print_result(anss):
    print(*anss, sep='\n')

def main():
    set_recursion_limit()
    input_func = get_input_function()
    N = read_n(input_func)
    C = read_c(input_func)
    AB = read_ab(input_func, N)
    es = build_empty_graph(N)
    build_graph_edges(es, AB)
    cs = build_empty_graph(N)
    build_color_nodes(cs, C)
    tin, tout = prepare_tin_tout(N)
    k_holder = prepare_k()
    run_dfs(N, es, tin, tout, k_holder)
    bit = BinaryIndexedTree(N)
    init_bit(bit, N)
    anss = solve_all(N, cs, es, tin, tout, bit)
    print_result(anss)

main()