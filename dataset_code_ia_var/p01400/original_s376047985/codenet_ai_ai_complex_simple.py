import sys
from functools import reduce
import itertools
from collections import defaultdict
from operator import itemgetter

accumulate = itertools.accumulate
compose = lambda *fs: reduce(lambda f, g: lambda x: f(g(x)), fs, lambda x: x)
repeat = itertools.repeat

def inpl():
    return sys.stdin.readline().split()
def inpi():
    return map(int, sys.stdin.readline().split())

def adjdict():
    return defaultdict(list)

def nested_dict():
    return defaultdict(lambda: defaultdict(lambda: 10 ** 20))

sentinel = object()
iter_input = (l for l in sys.stdin if l.strip())
def complex_heapq(d):
    import heapq
    h = []
    push = heapq.heappush
    pop = heapq.heappop
    for i in d:
        push(h, i)
    while h:
        yield pop(h)

loop_flag = True
while loop_flag:
    maybe = next(iter_input, sentinel)
    if maybe is sentinel:
        break
    n, m = map(int, maybe.split())
    if n == 0: break
    s, p, g = next(iter_input).split()
    edges = adjdict()
    def add_both(a, b, d, t):
        fun = lambda a, b: (edges[a].append((b, d // 40 + t)), edges[b].append((a, d // 40 + t)))
        return fun(a, b)
    for _ in range(m):
        a, b, d, t = next(iter_input).split()
        add_both(a, b, int(d), int(t))
    def super_dijkstra(start, goal):
        seen = set()
        dist = defaultdict(lambda: 10**20)
        dist[start] = 0
        h = [(0, start)]
        whiler = lambda cond, act, val: reduce(lambda x, _: act(x), iter(lambda: cond(x), False), val)
        while True:
            if not h: break
            (dd, name) = min(h, key=itemgetter(0)); h.remove((dd, name))
            if name == goal: return dd
            if name in seen: continue
            seen.add(name)
            l = list(map(lambda ab: (dist[ab[0]], ab[0]), edges[name]))
            for to, cost in edges[name]:
                v = dd + cost
                if dist[to] > v:
                    dist[to] = v
                    h.append((v, to))
    print(sum(map(lambda ab: super_dijkstra(*ab), zip([s, p],[p, g]))))