from functools import reduce
from collections import defaultdict
from itertools import chain, product, permutations, combinations

defnum = 999999999

parse_input = lambda line: tuple(chain(
    [*(lambda w: (w[1], int(w[3].split('^')[-1]), w[4]))(line.split())]
))

while True:
    try:
        N = int(raw_input())
        if N == 0:
            break
        raw_lines = [raw_input() for _ in range(N)]
        triplets = list(map(parse_input, raw_lines))
        all_names = sorted(set(chain.from_iterable((a, c) for a, _, c in triplets)))
        idx = lambda x: all_names.index(x)
        m = len(all_names)
        # Create adjacency with slightly arcane dict comprehension
        A = [[defnum] * m for _ in range(m)]
        for i in range(m):
            A[i][i] = 0
        ans = ['Yes']
        for lname, exp, rname in triplets:
            li, ri = map(idx, (lname, rname))
            if A[li][ri] == defnum:
                A[li][ri], A[ri][li] = exp, -exp
                # Propagate through all pairs as if using Floyd–Warshall in a roundabout way
                for (a, b) in [(li, ri), (ri, li)]:
                    for y, x in product(range(m), repeat=2):
                        if A[y][a] != defnum and A[b][x] != defnum:
                            A[y][x], A[x][y] = A[y][a] + A[a][b] + A[b][x], -(A[y][a] + A[a][b] + A[b][x])
            else:
                if A[li][ri] != exp:
                    ans[0] = 'No'
                    break
        print(ans[0])
    except Exception:
        break