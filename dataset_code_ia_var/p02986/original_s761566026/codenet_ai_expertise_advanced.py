import sys
import math
import operator as op
from itertools import (
    combinations, permutations, product,
    combinations_with_replacement, accumulate
)
from heapq import heapify, heappop, heappush, heappushpop
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import reduce, partial, lru_cache

sys.setrecursionlimit(1 << 20)
input = sys.stdin.readline

INF = float('inf')
LINF = (1 << 63) - 1
NIL = -LINF
MOD = 10 ** 9 + 7
MGN = 4

def AST(exp: bool, msg: str = ""):
    if not exp:
        raise AssertionError(msg)

def TAST(exp: bool, msg=""):
    if not exp:
        print(f"TAssertionError: {msg}", file=sys.stderr)
        while True: pass

def EPR(msg): print(msg, file=sys.stderr)

II = lambda: int(input())
IF = lambda: float(input())
IS = lambda: input().rstrip('\n')
ILCI = lambda n: [II() for _ in range(n)]
ILCF = lambda n: [IF() for _ in range(n)]
ILI = lambda: list(map(int, input().split()))
ILLI = lambda n: [list(map(int, input().split())) for _ in range(n)]
ILF = lambda: list(map(float, input().split()))
ILLF = lambda n: [list(map(float, input().split())) for _ in range(n)]
LTOS = lambda lst, sep=' ': sep.join(map(str, lst))
DEC = lambda lst: [x - 1 for x in lst]
INC = lambda lst: [x + 1 for x in lst]

class Queue(deque):
    def is_empty(self) -> bool: return not self
    def enqueue(self, item) -> None: self.appendleft(item)
    def insert(self, item) -> None: self.enqueue(item)
    def dequeue(self): return self.pop()
    def front(self): return self[-1]
    def pop(self) -> None: super().pop()
    def size(self) -> int: return len(self)

class LCA:
    def __init__(self, N: int):
        self.N = N
        self.graph = [list() for _ in range(N)]
        self.weights = [list() for _ in range(N)]
        self.depth = [0] * N
        self.costs = [0] * N
        self.l = (N-1).bit_length()
        self.parent = [[-1] * self.l for _ in range(N)]
    def add_edge(self, a: int, b: int, c=0):
        self.graph[a].append(b)
        self.weights[a].append(c)
        self.graph[b].append(a)
        self.weights[b].append(c)
    def _bfs(self, root: int):
        que = Queue([root])
        vis = [False] * self.N
        while que:
            v = que.dequeue()
            vis[v] = True
            for (nv, cost) in zip(self.graph[v], self.weights[v]):
                if not vis[nv]:
                    self.depth[nv] = self.depth[v] + 1
                    self.costs[nv] = self.costs[v] + cost
                    self.parent[nv][0] = v
                    que.enqueue(nv)
    def init(self, root: int=0):
        self.root = root
        self._bfs(root)
        for k in range(self.l-1):
            for v in range(self.N):
                if self.parent[v][k] != -1:
                    self.parent[v][k+1] = self.parent[self.parent[v][k]][k]
    def lca(self, u: int, v: int) -> int:
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        for k in reversed(range(self.l)):
            if self.parent[u][k] != -1 and self.depth[self.parent[u][k]] >= self.depth[v]:
                u = self.parent[u][k]
        if u == v:
            return u
        for k in reversed(range(self.l)):
            if self.parent[u][k] != -1 and self.parent[u][k] != self.parent[v][k]:
                u = self.parent[u][k]
                v = self.parent[v][k]
        return self.parent[u][0]
    def dist(self, a: int, b: int):
        c = self.lca(a, b)
        return self.costs[a] + self.costs[b] - 2 * self.costs[c]
    def length(self, a: int, b: int):
        c = self.lca(a, b)
        return self.depth[a] + self.depth[b] - 2 * self.depth[c]

def main():
    N, Q = ILI()
    lca = LCA(N)
    edges = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b, col, dist = ILI()
        a -= 1; b -= 1
        edges[a].append((b, dist, col))
        edges[b].append((a, dist, col))
        lca.add_edge(a, b, dist)
    lca.init()
    ans = [0] * Q
    queries = [[] for _ in range(N)]
    for qi in range(Q):
        cx, dy, a, b = ILI()
        a -= 1; b -= 1
        c = lca.lca(a, b)
        ans[qi] = lca.costs[a] + lca.costs[b] - 2 * lca.costs[c]
        queries[a].append((cx, qi, 1, dy))
        queries[b].append((cx, qi, 1, dy))
        queries[c].append((cx, qi, -2, dy))
    cnt = [0] * N
    sum_ = [0] * N

    # Iterative DFS using a manual stack for performance
    stack = [(0, -1, 0, 0)]  # (node, parent, last_color, last_cost)
    call_stack = []
    state = [0]*N
    ptr = [0]*N

    # To handle arbitrary colors, use dicts as sparse arrays for performance if colors are large
    cntc = defaultdict(int)
    sumc = defaultdict(int)
    query_at_node = queries
    while stack:
        v, p, pre_col, pre_cost = stack[-1]
        if state[v] == 0:
            for (col, qid, coeff, dist_) in query_at_node[v]:
                x = -sumc[col] + dist_ * cntc[col]
                ans[qid] += x * coeff
            state[v] = 1
        if ptr[v] < len(edges[v]):
            to, cost, col = edges[v][ptr[v]]
            ptr[v] += 1
            if to == p: continue
            cntc[col] += 1
            sumc[col] += cost
            stack.append((to, v, col, cost))
        else:
            if v != 0:
                cntc[pre_col] -= 1
                sumc[pre_col] -= pre_cost
            stack.pop()
    print(*ans, sep='\n')

if __name__ == '__main__':
    main()