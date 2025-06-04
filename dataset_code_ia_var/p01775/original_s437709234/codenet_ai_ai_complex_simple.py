from heapq import heappush, heappop
from functools import reduce, lru_cache
from itertools import product, chain, repeat, starmap, combinations, accumulate
from operator import or_, itemgetter

n, m, k, p = map(int, input().split())
p -= 1
edges = [[] for _ in range(n)]
list(map(lambda _: (lambda x, y, w: (edges[x := x - 1].append((y := y - 1, w)), edges[y].append((x, w))))(*map(int, input().split())), range(m)))

points = list(chain.from_iterable(starmap(lambda s, t: (s - 1, t - 1), (map(int, input().split()) for _ in range(k)))))
INF = pow(10, 20)

def dist(src):
    mem = [INF] * n
    mem[src] = 0
    q = [(0, src)]
    push = heappush
    pop = heappop
    while q:
        total, node = pop(q)
        [mem.__setitem__(to, new_total) or push(q, (new_total, to))
         for to, cost in edges[node]
         if (new_total := total + cost) < mem[to]]
    return mem

precomputed = [[dist(points[i])[point] for point in points] for i in range(2 * k)]
start_dists = dist(p)
start_cost = list(map(start_dists.__getitem__, points))

end_state = (1 << (2 * k)) - 1
memo = {}

def parity_mask(stat, i):
    return (stat >> i) & 1

def dependency_check(stat, i):
    return i % 2 == 1 and not parity_mask(stat, i - 1)

def visitable(stat, i):
    return not parity_mask(stat, i) and not dependency_check(stat, i)

def next_moves(stat):
    return (i for i in range(2 * k) if visitable(stat, i))

def setter(dic, key, value):
    dic[key] = value
    return value

def min_cost(stat, pos):
    if (stat, pos) in memo: return memo[(stat, pos)]
    if stat == end_state: return setter(memo, (stat, pos), 0)
    possibilities = (precomputed[pos][i] + min_cost(stat | (1 << i), i) for i in next_moves(stat))
    return setter(memo, (stat, pos), min(possibilities, default=INF))

result = reduce(lambda acc, i: min(acc, start_cost[i] + min_cost(1 << i, i)), range(0, 2 * k, 2), INF)
print("Cannot deliver" if result == INF else result)