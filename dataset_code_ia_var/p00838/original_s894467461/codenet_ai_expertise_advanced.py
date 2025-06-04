from itertools import product
from sys import stdin
from functools import partial

def solve():
    # All 24 rotation permutations for a cube (enumerated as index sequences)
    indices = (
        (0, 1, 2, 3, 4, 5), (0, 2, 4, 1, 3, 5), (0, 4, 3, 2, 1, 5), (0, 3, 1, 4, 2, 5),
        (1, 0, 3, 2, 5, 4), (1, 3, 5, 0, 2, 4), (1, 5, 2, 3, 0, 4), (1, 2, 0, 5, 3, 4),
        (2, 0, 1, 4, 5, 3), (2, 1, 5, 0, 4, 3), (2, 5, 4, 1, 0, 3), (2, 4, 0, 5, 1, 3),
        (3, 0, 4, 1, 5, 2), (3, 4, 5, 0, 1, 2), (3, 5, 1, 4, 0, 2), (3, 1, 0, 5, 4, 2),
        (4, 0, 2, 3, 5, 1), (4, 2, 5, 0, 3, 1), (4, 5, 3, 2, 0, 1), (4, 3, 0, 5, 2, 1),
        (5, 1, 3, 2, 4, 0), (5, 3, 4, 1, 2, 0), (5, 4, 2, 3, 1, 0), (5, 2, 1, 4, 3, 0)
    )

    # Fast input
    next_line = partial(next, stdin)
    while True:
        n = int(next_line())
        if n == 0:
            break
        cubes = [tuple(next_line().split()) for _ in range(n)]
        if n == 1:
            print(0)
            continue

        cube1, *other_cubes = cubes
        min_changes = 6 * (n - 1)

        # Pre-cache all rotations of other cubes to reduce repeated accesses
        rotated_cubes = [
            [tuple(cube[i] for i in idx) for idx in indices]
            for cube in other_cubes
        ]

        # For each rotation combination, compute the minimal changes needed
        # Use generator expressions and early break for performance
        for rot_combo in product(range(24), repeat=n - 1):
            changes = 0
            for face in range(6):
                color_count = {}
                color = cube1[face]
                color_count[color] = 1
                for cidx, ridx in enumerate(rot_combo):
                    c = rotated_cubes[cidx][ridx][face]
                    color_count[c] = color_count.get(c, 0) + 1
                max_count = max(color_count.values())
                changes += n - max_count
                if changes >= min_changes:
                    break  # Prune: no need to continue further
            else:
                min_changes = changes

        print(min_changes)

if __name__ == '__main__':
    solve()