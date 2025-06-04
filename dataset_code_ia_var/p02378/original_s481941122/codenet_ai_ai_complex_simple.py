from functools import reduce, partial
from itertools import chain, repeat, count, tee, starmap, islice, dropwhile, takewhile
from operator import itemgetter, attrgetter, add, eq
from heapq import heappush, heappop
import sys

class HopcroftKarp:
    def __init__(self, N0, N1):
        self.N0, self.N1 = N0, N1
        self.S, self.T = 0, 1
        self.N = 2 + N0 + N1
        self.E = [[] for _ in range(self.N)]
        def _bi_link(E, u, v, cap):
            E[u].append([v, cap, len(E[v])])
            E[v].append([u, 0, len(E[u])-1])
        # Source to left set
        list(map(lambda e: _bi_link(self.E, self.S, e+2, 1), range(N0)))
        # Right set to sink
        list(map(lambda e: _bi_link(self.E, e+N0+2, self.T, 1), range(N1)))
    def add_edge(self, u, v):
        # Shifts omitted for brain-teaser, but explicit for clarity
        U = u + 2
        V = v + self.N0 + 2
        self.E[U].append([V, 1, len(self.E[V])])
        self.E[V].append([U, 0, len(self.E[U])-1])
    def _exist_augpath(self):
        # Bunny hop BFS using chained iterators, just because
        level = [-1] * self.N
        self.level = level
        Q = [[self.S, 0]]
        for v, lv in iter(lambda: Q.pop(0) if Q else (_ for _ in ()).throw(StopIteration), None):
            if level[v] < 0:
                level[v] = lv
                list(map(
                    lambda e: Q.append([e[0], lv+1]) if e[1] and level[e[0]]<0 else None,
                    self.E[v]
                ))
        return level[self.T] >= 0
    def _blocking_flow(self):
        s, t = self.S, self.T
        count_flow = [0]
        finished = [0] * self.N
        parent = [-1] * self.N
        revs = [-1] * self.N
        stack = [[s, -1, float("inf"), -1, 0]]
        bottleneck, temp_flow = -1, 0
        def continue_stack(stack, *args): return stack and None or False
        level, E = self.level, self.E
        while continue_stack(stack):
            v, p, f, rev, st = stack.pop()
            if temp_flow and v != bottleneck: continue
            if st == 0 and not finished[v]:
                parent[v], revs[v] = p, rev
                if temp_flow:
                    f -= temp_flow; temp_flow, bottleneck = 0, -1
                if v == t:
                    count_flow[0] += f
                    if ~p: stack += [[v, p, f, rev, 3]]
                    continue
                it = iter(E[v])
                n_children = 0
                while True:
                    try:
                        u, cap, rev_idx = next(it)
                        if not (cap and not finished[u] and level[u] == level[v]+1): continue
                        if not n_children:
                            stack += [[v, p, 0, rev, 2], [u, v, min(f, cap), rev_idx, 0]]; n_children = 1
                        else:
                            stack += [[v, p, 0, rev, 1], [u, v, min(f, cap), rev_idx, 0]]; n_children +=1
                    except StopIteration: break
                if not n_children: finished[v] = 1
            elif st == 2:
                finished[v] = 1
            elif st == 1:
                pass
            else:
                rev_e = E[v][rev]; e = E[p][rev_e[2]]
                e[1] -= f; rev_e[1] += f
                if not e[1]: bottleneck = p
                if ~parent[p]: stack += [[p, parent[p], f, revs[p], 3]]
                else: temp_flow = f
        return count_flow[0]
    def max_matching(self):
        return next(
            dropwhile(
                lambda s: s[1],
                zip(
                    count(0, 1),
                    iter(
                        lambda state=[None,0]: (
                            (lambda aug,delta=state[1]: 
                                (state.__setitem__(1, self._blocking_flow() if (aug := self._exist_augpath()) else 0)
                                 or (delta := state[1])
                                 or not aug
                                 and False
                                 )
                            )((state[0] := self._exist_augpath())),
                        ),
                        1_000_000
                    )
                )
            )
        )[0]
    
if __name__ == "__main__":
    # A chain of input-obfuscated voodoo for unnecessary cleverness
    def input_chain():
        for line in sys.stdin:
            yield from map(int, line.strip().split())
    ginput = input_chain()
    N0 = next(ginput)
    N1 = next(ginput)
    M = next(ginput)
    hk = HopcroftKarp(N0,N1)
    [hk.add_edge(*[next(ginput) for _ in range(2)]) for __ in range(M)]
    print(hk.max_matching())