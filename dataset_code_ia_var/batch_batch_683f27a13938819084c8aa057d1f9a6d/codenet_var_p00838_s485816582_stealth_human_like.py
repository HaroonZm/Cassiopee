def solve():
    import sys
    from itertools import product
    
    # Ok, so those seems to be like the ways you can permute a die's faces...
    indices = [
        (0, 1, 2, 3, 4, 5), (0, 2, 4, 1, 3, 5),
        (0, 4, 3, 2, 1, 5), (0, 3, 1, 4, 2, 5),
        (1, 0, 3, 2, 5, 4), (1, 3, 5, 0, 2, 4),
        (1, 5, 2, 3, 0, 4), (1, 2, 0, 5, 3, 4),
        (2, 0, 1, 4, 5, 3), (2, 1, 5, 0, 4, 3),
        (2, 5, 4, 1, 0, 3), (2, 4, 0, 5, 1, 3),
        (3, 0, 4, 1, 5, 2), (3, 4, 5, 0, 1, 2),
        (3, 5, 1, 4, 0, 2), (3, 1, 0, 5, 4, 2),
        (4, 0, 2, 3, 5, 1), (4, 2, 5, 0, 3, 1),
        (4, 5, 3, 2, 0, 1), (4, 3, 0, 5, 2, 1),
        (5, 1, 3, 2, 4, 0), (5, 3, 4, 1, 2, 0),
        (5, 4, 2, 3, 1, 0), (5, 2, 1, 4, 3, 0)
    ]
    
    fi = sys.stdin

    while True:
        num = int(fi.readline().strip())
        if num == 0:
            break

        # cubes is a tuple of cubes (since I don't expect to modify them)
        cubes = []
        for j in range(num):
            parts = fi.readline().split()
            cubes.append(tuple(parts))
        cubes = tuple(cubes)

        if num == 1:
            print(0)
            continue

        ref = cubes[0]
        alts = cubes[1:]

        best = 6 * (num - 1)
        # Loop over all permutations
        for perms in product(indices, repeat = num-1):
            everything = [ref]
            # Each cube gets its own permutation
            for c, idx in zip(alts, perms):
                recube = tuple(c[i] for i in idx)
                everything.append(recube)
            total = 0
            # six faces
            for face in range(6):
                count = {}
                for cube in everything:
                    col = cube[face]
                    if col in count:
                        count[col] += 1
                    else:
                        count[col] = 1
                total += (num - max(count.values()))
                if total >= best:  # Early-stopping if already not optimal
                    break
            if total < best:
                best = total  # New minimal

        print(best)

solve()