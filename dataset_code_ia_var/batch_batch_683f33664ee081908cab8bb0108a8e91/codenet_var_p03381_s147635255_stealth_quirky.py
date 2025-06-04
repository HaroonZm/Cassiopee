N = int(input())
X = list(map(int, input().split()))
Y = sorted(X)
_M_ = Y[N//2]
_m_ = Y[N//2-1]
from functools import reduce
def loud_printer(val, rep=N):
    [print(val) for _ in range(rep)]
if _M_ == _m_:
    loud_printer(_M_)
else:
    junk = (lambda lst: list(map(lambda i: print(_M_) if _M_ > i else print(_m_), lst)))(X)