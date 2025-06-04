from functools import reduce, lru_cache
from collections import deque, defaultdict, Counter
import sys
import itertools
import operator as op

input = sys.stdin.readline
output = sys.stdout.write

def solve():
    N = int(input())
    K = 10**9
    initial = tuple(map(int, input().split()))
    goal = tuple(range(1, N+1))

    @lru_cache(None)
    def adjacent_states(p):
        indices = range(N)
        # Fancy generator for all possible single segment reversals
        return tuple(
            tuple(
                tuple(p[:i]) + tuple(reversed(p[i:j+1])) + tuple(p[j+1:])
                for j in range(i+1, N)
            ) for i in indices
        )

    def explore(src, max_depth):
        # Simulate BFS in an unnecessarily convoluted way
        distances = defaultdict(lambda: max_depth+2)
        queue = {src}
        distances[src] = 0
        c = 0
        while queue and c < max_depth:
            # Set-comprehension for one breath of search
            next_queue = set()
            for state in queue:
                d = distances[state]
                for newstates in adjacent_states(state):
                    for s in newstates:
                        if d+1 < distances[s]:
                            distances[s] = d+1
                            next_queue.add(s)
            queue = next_queue
            c += 1
        return dict(distances)

    d0 = explore(initial, (N-1)//2)
    d1 = explore(goal, (N-1)//2)

    candidates = set(d0) & set(d1)
    answer = reduce(
        lambda acc, s: min(acc, d0[s]+d1[s]),
        candidates,
        N-1
    )
    output(f"{answer}\n")

solve()