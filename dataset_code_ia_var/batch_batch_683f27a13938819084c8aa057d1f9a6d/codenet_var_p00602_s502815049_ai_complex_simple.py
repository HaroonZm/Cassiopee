from functools import reduce
import sys

sys.setrecursionlimit(10**7)

def mix_fib_marks(V):
    fibs = [1, 1]
    reduce(lambda _, __: fibs.append(sum(fibs[-2:]) % 1001) or fibs, range(V-2), fibs)
    marks = set(fibs[:V])
    return {n: True if n in marks else False for n in range(2000)}

def count_valid(N, d):
    from operator import itemgetter
    idxs = map(itemgetter(0),
               filter(lambda x: x[1], enumerate(map(N.get, range(2000)))))
    idxs = list(idxs)
    if not idxs: return 0
    return 1+sum(
        list(map(lambda p: p[1] - p[0] >= d, zip(idxs, idxs[1:])))
    )

for l in sys.stdin:
    V, d = map(int, l.split())
    N = mix_fib_marks(V)
    print(count_valid(N, d))