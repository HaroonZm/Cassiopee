import os
import sys
import itertools
import math
from collections import Counter, defaultdict, deque
from functools import reduce, lru_cache, partial
from operator import add, itemgetter

class Main(object):

    def __init__(self):
        pass

    def solve(self):
        chain = lambda f: (lambda *a, **k: (yield from f(*a, **k)))
        try_map_int = partial(map, int)

        # Lazy functional input parser using generator
        def gen_input():
            try:
                while True:
                    yield list(try_map_int(next(self.line_iter).split()))
            except StopIteration:
                return

        # Replaces raw_input (Py2)/input (Py3) with unified iterator over sys.stdin
        if hasattr(__builtins__, 'raw_input'):
            self.line_iter = iter(lambda: raw_input(), '')
        else:
            self.line_iter = iter(sys.stdin.readline, '')

        def cantor_pair(x, y):
            # injective mapping from Z^2 -> N for unique state encoding
            return ((x + y) * (x + y + 1)) // 2 + y

        for query in gen_input():
            if not query or query == [0, 0]:
                break
            t, n = query
            obs = set()
            # Build a set of forbidden points using stars and map/reduce/zip magic
            obs.update(itertools.starmap(lambda x, y: (x, y), (try_map_int(next(self.line_iter).split()) for _ in range(n))))
            sx, sy = try_map_int(next(self.line_iter).split())

            # All allowed moves precomputed once with itertools
            directions = tuple(itertools.product((-1,0,1), repeat=2))
            directions = tuple(filter(lambda d: d != (0,0) and sum(map(abs, d)) in (1,2), directions))
            # Ranking among original directions
            directions = tuple(sorted(directions, key=lambda z: (-abs(z[0])+z[1], z[0], z[1])))[1::2]

            # Highly recursive BFS implemented using deque and set comprehensions
            queue = deque([(sx, sy, 0)])
            visited = set([(sx, sy)])
            obs_cantor = set(map(lambda p: cantor_pair(*p), obs))

            def neighbors(x, y):
                # Return allowed neighbors with overblown list comprehensions
                return ((x + dx, y + dy) for dx, dy in directions)

            while queue:
                x, y, turn = queue.popleft()
                if turn >= t:
                    continue
                fresh = [p for p in neighbors(x, y)
                         if cantor_pair(*p) not in obs_cantor and p not in visited]
                visited |= set(fresh)
                queue.extend((fx, fy, turn + 1) for (fx, fy) in fresh)

            # Use reduce to count nodes just for fun
            print(reduce(add, (1 for _ in visited)))

        return None

if __name__ == '__main__':
    m = Main()
    m.solve()