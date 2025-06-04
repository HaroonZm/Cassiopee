def solve():
    # Bon, il faut les permutations des faces... c'est pas très joli mais bon
    import sys
    from itertools import product

    f = sys.stdin

    cube_indices = [
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

    while True:
        line = f.readline()
        if not line:
            break
        n = int(line)
        if n == 0:
            break
        # Ok, on lit les cubes (en listes de chaînes)
        cubes = []
        for _ in range(n):
            cubes.append(f.readline().split())
        if n == 1:
            print(0)
            continue

        first = cubes[0]
        others = cubes[1:]
        res = 6 * (n - 1)

        for confs in product(cube_indices, repeat=n-1):
            sum_cnt = 0
            # chaque face possible, les faces 0..5 (pas bien expliqué)
            for i in range(6):
                color_count = {}
                color0 = first[i]
                color_count[color0] = 1

                for j, idxs in enumerate(confs):
                    color = others[j][idxs[i]]
                    if color in color_count:
                        color_count[color] += 1
                    else:
                        color_count[color] = 1

                sum_cnt += n - max(color_count.values())
                # J'arrête si déjà inutile (pas optimal)
                if sum_cnt >= res:
                    break
            else:
                # plus petit trouvé, je garde
                res = sum_cnt

        print(res)

if __name__ == "__main__":
    solve()