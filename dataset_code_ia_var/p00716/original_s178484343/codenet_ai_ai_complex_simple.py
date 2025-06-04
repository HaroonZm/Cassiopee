from functools import reduce
import sys

_ = lambda: int(next(sys.stdin))
__ = lambda: list(map(float, next(sys.stdin).split()))
___ = lambda a, r, f, y: reduce(lambda acc, _: (acc[0]+int(acc[0]*r)-f, int(acc[0]*r)), range(y), (a,0))[0]
____ = lambda a, r, f, y: reduce(lambda acc, _: (acc[0]-f, acc[1]+int(acc[0]*r)), range(y), (a,0))
class M: pass
m = _()
for _i in range(m):
    M.fund, M.year, M.n = _(), _(), _()
    M.ans = M.fund
    for _j in range(M.n):
        t, rate, fee = __()
        V = (___ if t else ____) (M.fund, rate, fee, M.year)
        V += 0 if t else ____ (M.fund, rate, fee, M.year)[1]
        M.ans = max(M.ans, int(V))
    print(int(M.ans))