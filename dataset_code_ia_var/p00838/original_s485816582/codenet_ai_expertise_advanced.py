from functools import reduce
from itertools import product
from sys import stdin

def solve():
    # All 24 distinct face orderings for a cube (rotation group)
    ROTATIONS = [
        (0, 1, 2, 3, 4, 5), (0, 2, 4, 1, 3, 5), (0, 4, 3, 2, 1, 5), (0, 3, 1, 4, 2, 5),
        (1, 0, 3, 2, 5, 4), (1, 3, 5, 0, 2, 4), (1, 5, 2, 3, 0, 4), (1, 2, 0, 5, 3, 4),
        (2, 0, 1, 4, 5, 3), (2, 1, 5, 0, 4, 3), (2, 5, 4, 1, 0, 3), (2, 4, 0, 5, 1, 3),
        (3, 0, 4, 1, 5, 2), (3, 4, 5, 0, 1, 2), (3, 5, 1, 4, 0, 2), (3, 1, 0, 5, 4, 2),
        (4, 0, 2, 3, 5, 1), (4, 2, 5, 0, 3, 1), (4, 5, 3, 2, 0, 1), (4, 3, 0, 5, 2, 1),
        (5, 1, 3, 2, 4, 0), (5, 3, 4, 1, 2, 0), (5, 4, 2, 3, 1, 0), (5, 2, 1, 4, 3, 0)
    ]

    # Cache for small n to avoid redundant computation
    cache = {}

    def min_repaints(cubes):
        n = len(cubes)
        key = tuple(map(tuple, cubes))
        if key in cache:
            return cache[key]
        cube1, rest = cubes[0], cubes[1:]
        min_cost = 6 * (n - 1)
        # Iterate all possible orientation assignments for n-1 cubes
        for orientations in product(ROTATIONS, repeat=n-1):
            cost = sum(
                n - max(
                    reduce(
                        lambda counter, face_colors: (
                            counter.setdefault(face_colors[0], 0) or counter.update({face_colors[0]: counter.get(face_colors[0],0)+1}) or counter,
                            *face_colors[1:]
                        )[0],
                        zip([cube1[i]] + [cube[r[i]] for cube, r in zip(rest, orientations)] for i in range(6)),
                        {cube1[i]:1 for i in range(6)}
                    ).values()
                )
            )
            if cost < min_cost:
                min_cost = cost
            if min_cost == 0:
                break
        cache[key] = min_cost
        return min_cost

    while True:
        try:
            n = int(stdin.readline())
            if not n: break
            cubes = [stdin.readline().split() for _ in range(n)]
            if n == 1:
                print(0)
                continue
            print(min_repaints(cubes))
        except Exception:
            break

solve()