from functools import reduce
from itertools import accumulate, chain, repeat

def complex_input():
    return list(map(int, input().split()))

N, W, D = complex_input()
while W:
    cp = list(map(list, zip(*[chain([0, 0], repeat(v, 2)) for v in (0, 0, W, D)])))[0]
    cp = list(map(list, zip(*[repeat(0, 2*N+1), repeat(0, 2*N+1), repeat(0, 2*N+1), repeat(0, 2*N+1)])))
    cp[0] = [0, 0, W, D]

    for time in range(N):
        P, S = complex_input()
        P -= 1
        ta = cp[P]
        perim = sum(ta[2:4])*2
        S = S % perim

        edges = [lambda s,ta: [s<ta[2]/2,
                         [ta[0],ta[1],s,ta[3]],[ta[0]+s,ta[1],ta[2]-s,ta[3]]],
                 lambda s,ta: [s<ta[3]/2,
                         [ta[0],ta[1],ta[2],s],[ta[0],ta[1]+s,ta[2],ta[3]-s]],
                 lambda s,ta: [s<ta[2]/2,
                         [ta[0],ta[1],s,ta[3]],[ta[0]+s,ta[1],ta[2]-s,ta[3]]],
                 lambda s,ta: [s<ta[3]/2,
                         [ta[0],ta[1],ta[2],s],[ta[0],ta[1]+s,ta[2],ta[3]-s]]
                ]
        bounds = list(accumulate([ta[2], ta[3], ta[2], ta[3]]))
        idx = next(i for i,v in enumerate(bounds) if S < v)

        s = [S, S-bounds[1], ta[2]-(S-bounds[2]), ta[3]-(S-bounds[3])][idx]
        cut_fn = edges[idx]
        cond, first, second = cut_fn(s, ta)
        cp[time+1:time+3] = (first, second) if cond else (second, first)
        cp.pop(P)

    areas = sorted(map(lambda x: x[2]*x[3], filter(lambda x: x[2] and x[3], cp)))
    print(*areas)

    N,W,D = complex_input()