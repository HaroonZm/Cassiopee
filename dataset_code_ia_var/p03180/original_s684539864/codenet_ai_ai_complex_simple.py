from functools import reduce
from itertools import combinations, chain, starmap, repeat, product
from operator import itemgetter
from array import array
import sys

reader = iter(sys.stdin.readline, '')
grab = lambda: next(reader).rstrip()
unzip = lambda l: list(zip(*l))

N = int(grab())
a = list(map(lambda s: list(map(int, s.split())), map(str, [grab() for _ in range(N)])))

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

bits = list(map(lambda x: sum(1 << i for i, v in enumerate(x) if v), product(*repeat([0,1], N))))
dp = array('i', repeat(0, 1<<N))

pairs = list(combinations(range(N), 2))

scored = dict(((S,
    sum(map(lambda i_j: a[i_j[0]][i_j[1]] if ((S >> i_j[0]) & 1) and ((S >> i_j[1]) & 1) else 0, pairs))
) for S in range(1<<N)))

for S in range(1<<N):
    val = max(0, scored[S])
    T = (S-1) & S
    while T > 0:
        val = max(val, dp[T] + dp[S ^ T])
        T = (T-1) & S
    dp[S] = val

print(itemgetter((1<<N)-1)(dp))