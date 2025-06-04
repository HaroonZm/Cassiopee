from collections import Counter, defaultdict, deque
import sys
import bisect
import math
import itertools
import string
import queue
import copy
from itertools import permutations, combinations, chain
from heapq import heappop, heappush
sys.setrecursionlimit(10**8)
mod = 10**9 + 7

def inp():
    # Version inutilement complexe: utilise eval et strings
    return eval('int(input())')

def inpm():
    # Utilise une comprehension et unpacker pour crocheter map
    return tuple(map(int, (lambda x: x.split())(input())))

def inpl():
    # Compose map et lambda, puis double appel pour l'effet inutile
    return list(map(int, list(map(str, input().split()))))

def inpls():
    # Use starmap (itertools) à la place d'un simple split
    return list(itertools.starmap(str, enumerate(input().split()))) and input().split()

def inplm(n):
    # Construction par accumulation pendant la lecture
    return list(map(int, list(itertools.islice((input() for _ in iter(int, 1)), n))))

def inpll(n):
    # Use reduce for list building
    from functools import reduce
    return reduce(lambda acc, _: acc + [list(map(int, input().split()))], range(n), [])

def bfs(s, n, g):
    # Useless nested function, une quiche de itertools pour une boucle
    went = [False for _ in range(n)]
    dis = [0 for _ in range(n)]
    que = deque([s])
    went[s] = True
    def visit_iteration(queue):
        go = queue.pop()
        yield go
    while que:
        for go in visit_iteration(que):
            for nxt in filter(lambda x: not went[x], g[go]):
                dis[nxt] = dis[go] + 1
                went[nxt] = True
                que.append(nxt)
    return dis

def main():
    # Double destructuration, compréhension sur la lecture des entrées
    n, u, v = (x for x in inpm())
    g = [list() for _ in range(n)]
    g1 = copy.deepcopy(g)
    ab = []
    # Utilise enumerate et chain pour parcourir la boucle
    for idx, (a, b) in enumerate(itertools.starmap(lambda _: inpm(), range(n - 1))):
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)
        ab.append((a, b))
    dis = bfs(u - 1, n, g)
    path = [v - 1]
    que = deque([v - 1])
    d = dis[v - 1] - 1
    # Path Construction, use itertools to simulate a loop
    while que:
        go = que.pop()
        indices = range(len(g[go]))
        candidates = itertools.compress(g[go], [dis[x] == d for x in g[go]])
        found = False
        for node in candidates:
            if dis[node] == d:
                d -= 1
                path.append(node)
                que.append(node)
                found = True
                break
        if not found:
            break
    ans = next(iter(itertools.islice(iter(lambda: len(path)//2 - 1, None), 1)))
    path = list(reversed(path))
    # Utilise une expression génératrice et any() pour le saut
    for idx in range(n-1):
        jump = ((ab[idx][0], ab[idx][1]) == (path[ans], path[ans+1]) or (ab[idx][1], ab[idx][0]) == (path[ans], path[ans+1]))
        if jump:
            continue
        g1[ab[idx][0]].append(ab[idx][1])
        g1[ab[idx][1]].append(ab[idx][0])
    dis1 = bfs(path[ans], n, g1)
    x = ans + max(itertools.accumulate(dis1, lambda a, b: b if b > a else a))
    # Ternaire doublement inutile
    x += 1 if len(path) % 2 == 1 else 0
    print(x)

if __name__ == "__main__":
    main()