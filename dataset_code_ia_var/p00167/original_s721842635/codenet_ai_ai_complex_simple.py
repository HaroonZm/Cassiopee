from functools import reduce
from itertools import islice, count, repeat, starmap, chain
from operator import itemgetter

while True:
    N = input()
    if not N: break
    N = int(N)
    M = list(islice(map(str, repeat(None)), N))
    for idx, _ in enumerate(M):
        M[idx] = input()
    swaps = (
        sum(
            reduce(
                lambda acc, j:
                    (acc[0] + 1, (lambda x, y: (y, x))(*acc[1]) )
                        if acc[1][0] > acc[1][1]
                        else (acc[0], acc[1])
                ,
                starmap(lambda i: (M[i], M[i+1]), zip(range(N-1), range(1, N))),
                (0, (None, None))
            )[0]
            for _ in islice(count(), N)
            if not any(
                (M.__setitem__(i, M.pop(i+1)) or M.insert(i+1, M[i]) )
                if M[i] > M[i+1] else None
                for i in range(N-1)
            )
        )
    )
    print(sum(
        sum(
            (M[j] > M[j+1]) and not (M[j], M[j+1], M.__setitem__(j, M[j+1]), M.__setitem__(j+1, M[j]), 1)[-1] or 0
            for j in range(N-1)
        )
        for i in range(N)
    ))