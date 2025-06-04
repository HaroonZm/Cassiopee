from functools import reduce
from itertools import chain, islice, tee, starmap
from collections import deque
import sys
import operator

# Lambdas et helpers excessifs
splitter = lambda x: list(map(int, x.split()))
to_pairs = lambda it: zip(*[islice(iter(it), i, None, 2) for i in range(2)])
compose = lambda *fs: lambda x: reduce(lambda v, f: f(v), fs[::-1], x)
bitfull = lambda n: (1 << n) - 1

# Entrée complexe
lines = sys.stdin.buffer.read().decode().split('\n')
N = int(lines[0])
datastream = list(chain.from_iterable(map(splitter, lines[1:])))
A, B = tee(datastream)
AB = zip(islice(A, 0, None, 2), islice(B, 1, None, 2))

# Graph construction avec compréhension "créative"
graph = reduce(lambda acc, ab: (acc[ab[0]].append(ab[1]), acc[ab[1]].append(ab[0]), acc)[-1],
               AB,
               [[] for _ in range(N+1)])

# DFS itératif biscornu
root, parent, order = 1, [0] * (N+1), []
stack = deque([root])
while stack:
    node = stack.pop()
    order.append(node)
    unused = list(filter(lambda y: parent[node] != y,
                        graph[node]))
    parent_iter = starmap(lambda y, p=node: (operator.setitem(parent, y, p), y)[-1],
                          ((y,) for y in unused))
    stack.extend(parent_iter)

full = bitfull(60)
uninity, dp, twice = [0]*(N+1), [0]*(N+1), [0]*(N+1)

for x in reversed(order):
    p = parent[x]
    n = twice[x].bit_length() - 1
    add_mask = bitfull(n+1) if n >= 0 else 0
    dp[x] |= add_mask
    can_use = full & ~dp[x]
    lsb = can_use & -can_use if can_use else 0
    uninity[x] = lsb
    dp[x] |= lsb
    dp[x] &= full & -(lsb)
    twice[p] |= dp[x] & dp[p]
    dp[p] |= dp[x]

from operator import itemgetter
x = max(uninity, key=itemgetter(0))
print((x.bit_length()-1) if x > 0 else 0)