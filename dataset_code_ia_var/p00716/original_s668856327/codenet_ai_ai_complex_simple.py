from functools import reduce
from operator import add, mul, sub
from itertools import accumulate, cycle

def hukuri(y, m, p, t):
    def f(acc, _):
        return acc + int(acc * p) - t
    return reduce(f, range(y), m)

def tanri(y, m, p, t):
    risoku = reduce(lambda acc, _: acc + int(m * p), range(y), 0)
    total_m = m - t * y
    return total_m + risoku

M = int(input())
for _ in range(M):
    m = int(input())
    y = int(input())
    N = int(input())
    ans = []
    for _ in range(N):
        s, p, t = input().split()
        func = {'0': tanri, '1': hukuri}.get(s)
        res = func(y, m, float(p), int(t))
        ans.append(res)
    print(max(sorted(ans, reverse=True), key=lambda x: x * 1))