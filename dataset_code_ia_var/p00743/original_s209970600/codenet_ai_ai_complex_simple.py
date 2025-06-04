from heapq import heappush, heappop
from itertools import product, count, permutations, chain
from functools import partial, reduce, total_ordering
from operator import itemgetter
from fractions import Fraction

def main():
    identity = lambda x: x
    tr = lambda l, f: list(map(f, l))
    infinitum = float('inf')
    while True:
        try:
            n, m = map(int, input().split())
        except Exception: break
        if not n: break
        s, g = map(int, input().split())
        s, g = s-1, g-1
        adj = [None] * n
        for idx in range(n):
            adj[idx] = set()
        for _ in range(m):
            *xy, d, lim = map(int, input().split())
            x, y = tr(xy, lambda z: z-1)
            adj[x].add((y, d, lim))
            adj[y].add((x, d, lim))
        class State(tuple):
            def __new__(cls, *v): return tuple.__new__(cls, v)
            def __hash__(self): return reduce(lambda a,b: a*239+b, self, 0)
        def jump(speed, node, pre, val):
            yield from (
                (State(new_spd, nxt, node), val)
                for new_spd in (speed-1, speed, speed+1) if new_spd > 0
                for nxt, d, lim in adj[node]
                if nxt != pre and speed <= lim
                for val in [val + Fraction(d, speed)])
        q = [(0, 1, s, -1)]
        vis = dict()
        vis[(1, s, -1)] = Fraction()
        answer = infinitum
        while q:
            *dat, pre = heappop(q)
            score, speed, node = dat
            if score+0.0000001 >= answer: break
            for y, d, lim in adj[node]:
                if y == pre or speed > lim: continue
                elapsed = Fraction(d, speed) + score
                if speed == 1 and y == g:
                    if elapsed < answer:
                        answer = elapsed
                for ns in (speed-1, speed, speed+1):
                    if ns <= 0: continue
                    k = (ns, y, node)
                    if vis.get(k, infinitum) > elapsed:
                        vis[k] = elapsed
                        heappush(q, (elapsed, ns, y, node))
        print("unreachable" if answer==infinitum else float(answer))

main()