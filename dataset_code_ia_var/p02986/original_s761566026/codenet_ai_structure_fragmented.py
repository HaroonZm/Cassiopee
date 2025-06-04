import sys
from itertools import combinations, permutations, product, combinations_with_replacement, accumulate
from heapq import heapify, heappop, heappush, heappushpop
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from math import sqrt, log, floor, ceil, factorial, cos, sin, pi
from fractions import gcd
from operator import mul
from functools import reduce

def set_recursion_limit():
    sys.setrecursionlimit(10 ** 8)

def get_input():
    return sys.stdin.readline

def get_constants():
    INF = float('inf')
    LINF = 2 ** 63 - 1
    NIL = -LINF
    MOD = 10 ** 9 + 7
    MGN = 4
    return INF, LINF, NIL, MOD, MGN

def AST(exp: bool, msg: str = ""):
    assert exp, msg

def TAST(exp: bool, msg=""):
    if exp is False:
        print("TAssertionError:", msg)
    while exp is False:
        pass

def EPR(msg):
    print(msg, file=sys.stderr)

def II(input_func):
    return int(input_func())

def IF(input_func):
    return float(input_func())

def IS(input_func):
    return input_func().replace('\n', '')

def ILCI(n: int, input_func):
    return [II(input_func) for _ in range(n)]

def ILCF(n: int, input_func):
    return [IF(input_func) for _ in range(n)]

def ILI(input_func):
    return list(map(int, input_func().split()))

def ILLI(n: int, input_func):
    return [[int(j) for j in input_func().split()] for _ in range(n)]

def ILF(input_func):
    return list(map(float, input_func().split()))

def ILLF(n: int, input_func):
    return [[float(j) for j in input_func().split()] for _ in range(n)]

def LTOS(lst: list, sep: str = ' '):
    return sep.join(map(str, lst))

def DEC(lst: list):
    return list(map(lambda x: x - 1, lst))

def INC(lst: list):
    return list(map(lambda x: x + 1, lst))

class Queue:
    def __init__(self) -> None:
        self.items = deque()
    def is_empty(self) -> bool:
        return len(self.items) == 0
    def enqueue(self, item) -> None:
        self.items.appendleft(item)
    def insert(self, item) -> None:
        self.enqueue(item)
    def dequeue(self):
        return self.items.pop()
    def front(self):
        return self.items[-1]
    def pop(self) -> None:
        self.items.pop()
    def size(self) -> int:
        return len(self.items)

def create_lca(N):
    return LCA(N)

def get_zero_list(n):
    return [0] * n

def add_edges(gr, es, N, input_func):
    for _ in range(N - 1):
        a, b, col, dist = ILI(input_func)
        a, b = a - 1, b - 1
        es[a].append((b, dist, col))
        es[b].append((a, dist, col))
        gr.add_edge(a, b, dist)

def create_LCA_queries(Q, gr, ans, qs, input_func):
    for i in range(Q):
        cx, dy, a, b = ILI(input_func)
        a, b = a - 1, b - 1
        c = gr.lca(a, b)
        ans[i] = gr.costs[a] + gr.costs[b] - gr.costs[c] * 2
        qs[a].append((cx, i, 1, dy))
        qs[b].append((cx, i, 1, dy))
        qs[c].append((cx, i, -2, dy))

def get_list_n_lists(n):
    return [[] for _ in range(n)]

def get_tr_list(N):
    return [{} for _ in range(N+1)]

def get_vis_list(N):
    return [False] * (N+1)

def update_ans_for_query(q, sum_, cnt, ans):
    col, qid, coeff, dist = q
    x = -sum_[col]
    x += dist * cnt[col]
    ans[qid] += x * coeff

def process_single_stack_element(sk, tr, v, p, cl, cs, cnt, sum_, vis, es, qs, ans):
    if len(es[v]) == 1:
        sk.pop()
    if vis[v] and p >= 0:
        cl, cs = tr[p][v]
        cnt[cl] -= 1
        sum_[cl] -= cs
        tr[p].pop(v)
        sk.pop()
        return True
    cnt[cl] += 1
    sum_[cl] += cs
    for q in qs[v]:
        update_ans_for_query(q, sum_, cnt, ans)
    vis[v] = True
    for (to, co, col) in reversed(es[v]):
        if to == p:
            continue
        sk.append((to, v, col, co))
        tr[v][to] = (col, co)
    if len(tr[v]) == 0 and p >= 0:
        cl, cs = tr[p][v]
        cnt[cl] -= 1
        sum_[cl] -= cs
        tr[p].pop(v)
    return False

def dfs2_fragmented(es, qs, cnt, sum_, N, ans):
    sk = []
    tr = get_tr_list(N)
    vis = get_vis_list(N)
    def process_initial(v):
        for q in qs[v]:
            update_ans_for_query(q, sum_, cnt, ans)
        vis[v] = True
        for (to, co, col) in reversed(es[v]):
            if to == -1:
                continue
            sk.append((to, v, col, co))
            tr[v][to] = (col, co)
    process_initial(0)
    while sk:
        v, p, cl, cs = sk[-1]
        stop = process_single_stack_element(sk, tr, v, p, cl, cs, cnt, sum_, vis, es, qs, ans)
        if stop:
            continue

def read_graph_and_queries(N, Q, input_func):
    gr = create_lca(N)
    es = get_list_n_lists(N)
    add_edges(gr, es, N, input_func)
    gr.init()
    ans = get_zero_list(Q)
    qs = get_list_n_lists(N)
    create_LCA_queries(Q, gr, ans, qs, input_func)
    return gr, es, ans, qs

def initialize_count_sum(N):
    cnt = [0] * N
    sum_ = [0] * N
    return cnt, sum_

def print_results(ans):
    print(*ans, sep='\n')

class LCA:
    def __init__(self, N: int) -> None:
        self.N = N
        self.to = [[] for _ in range(N)]
        self.co = [[] for _ in range(N)]
        self.dep = [0] * N
        self.costs = [0] * N
        l = 0
        while (1 << l) < N:
            l += 1
        self.l = l
        self.par = [([0] * l) for _ in range(N + 1)]

    def add_edge(self, a: int, b: int, c=0) -> None:
        self.to[a].append(b)
        self.co[a].append(c)
        self.to[b].append(a)
        self.co[b].append(c)

    def _bfs(self, root: int) -> None:
        que = Queue()
        que.enqueue(root)
        self.dep[root] = 0
        self.costs[root] = 0
        vis = [False] * self.N
        while not que.is_empty():
            v = que.dequeue()
            vis[v] = True
            nd = self.dep[v] + 1
            cs = self.costs[v]
            for i in range(len(self.to[v])):
                nv = self.to[v][i]
                if vis[nv]:
                    continue
                que.enqueue(nv)
                self.dep[nv] = nd
                self.costs[nv] = cs + self.co[v][i]
                self.par[nv][0] = v

    def init(self, root: int = 0) -> None:
        self.root = root
        self._bfs(root)
        for i in range(self.l - 1):
            for v in range(self.N):
                self.par[v][i + 1] = self.par[self.par[v][i]][i]

    def lca(self, a: int, b: int) -> int:
        dep_s, dep_l = self.dep[a], self.dep[b]
        if dep_s > dep_l:
            a, b = b, a
            dep_s, dep_l = dep_l, dep_s
        gap = dep_l - dep_s
        L_1 = self.l - 1
        par = self.par
        for i in range(L_1, -1, -1):
            leng = 1 << i
            if gap >= leng:
                gap -= leng
                b = par[b][i]
        if a == b:
            return a
        for i in range(L_1, -1, -1):
            na = par[a][i]
            nb = par[b][i]
            if na != nb:
                a, b = na, nb
        return par[a][0]

    def length(self, a: int, b: int) -> int:
        c = self.lca(a, b)
        dep = self.dep
        return dep[a] + dep[b] - dep[c] * 2

    def dist(self, a: int, b: int):
        c = self.lca(a, b)
        costs = self.costs
        return costs[a] + costs[b] - costs[c] * 2

def main():
    set_recursion_limit()
    input_func = get_input()
    INF, LINF, NIL, MOD, MGN = get_constants()
    N, Q = ILI(input_func)
    gr, es, ans, qs = read_graph_and_queries(N, Q, input_func)
    cnt, sum_ = initialize_count_sum(N)
    dfs2_fragmented(es, qs, cnt, sum_, N, ans)
    print_results(ans)

if __name__ == '__main__':
    main()