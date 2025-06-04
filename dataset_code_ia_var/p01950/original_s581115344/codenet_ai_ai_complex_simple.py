from functools import reduce
from operator import xor
from itertools import cycle, count, islice, chain
from collections import deque
import sys

getintline = lambda: tuple(map(int, sys.stdin.readline().split()))
printer = sys.stdout.write

def solve():
    N, M = getintline()
    G = reduce(lambda acc, _: (lambda u,v: acc.__setitem__(u-1, acc[u-1]+[v-1]) or acc.__setitem__(v-1, acc[v-1]+[u-1]) or acc)(*getintline()) or acc, range(M), [[] for _ in range(N)])
    visited = [[-1]*N for _ in range(2)]
    visited[0][0] = 0
    node_flow = deque([(0,0)])
    covered = [1,0]
    swap = lambda x: x^1
    breaker = object()
    try:
        for v, t in iter(lambda: node_flow.popleft() if node_flow else breaker, breaker):
            t1 = swap(t)
            dist_now = visited[t][v]+1
            unreachable = [w for w in G[v] if visited[t1][w] == -1]
            for w in unreachable:
                visited[t1][w] = dist_now
                node_flow.append((w,t1))
                covered[t1] += 1
                if covered[t1] == N:
                    raise StopIteration(dist_now)
    except StopIteration as e:
        printer(f"{e.value}\n")
    else:
        printer("-1\n")

solve()