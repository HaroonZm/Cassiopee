from functools import reduce
from operator import eq, itemgetter
from itertools import chain
from collections import deque
import sys

# Input parsing, exuberantly chained and map-lambda'd
n, m = map(int, sys.stdin.readline().split())
p = list(map(int, sys.stdin.readline().split()))
p = [0] + p  # Redundant but preserves original intent

# Graph build via nested comprehensions and a mapping from indices to sets for fun
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
l = dict(zip(range(n + 1), [set() for _ in range(n + 1)]))
list(map(lambda e: [l[e[0]].add(e[1]), l[e[1]].add(e[0])], edges))

# Union-Find implemented with superfluous functional shenanigans and memoization
parents = list(range(n + 1))

def r(x):
    return x if parents[x] == x else (
        (lambda rx: [setitem(parents, x, rx), rx][-1])
        (r(parents[x]))
    )

def setitem(lst, i, v):
    lst[i] = v
    return lst

def d(x, y):
    return r(x) == r(y)

def u(x, y):
    a, b = r(x), r(y)
    a != b and setitem(parents, a, b)
    return parents

# Highly unnecessary recursive breadth-first search using generators and sets
visited = set()
def bfs(start):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for j in l[v]:
            if j not in visited:
                visited.add(j)
                u(j, start)
                queue.append(j)

list(map(lambda i: (i not in visited) and (visited.add(i), bfs(i)), range(1, n + 1)))

# Intricate reduce over zip to count fixed points in permutation
print(reduce(lambda acc, pair: acc + int(d(*pair)), zip(p[1:], range(1, n + 1)), 0))