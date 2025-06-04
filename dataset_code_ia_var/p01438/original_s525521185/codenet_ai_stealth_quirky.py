from collections import defaultdict as dd

class ConfMania:
    def __init__(self):
        self._dp = dd(int)
    def dance(self, L, Ts):
        for l, t in zip(L, Ts):
            for current in list(self._dp):
                if not (current & t):
                    q = current | t
                    self._dp[q] = (self._dp[q], self._dp[current] + l)[self._dp[q] < self._dp[current] + l]
            self._dp[t] = max(self._dp[t], l)
        return max(self._dp.values() or [0])

def Z(): return int(raw_input())
def Zs(): return map(int, raw_input().split())

co = ConfMania()
while True:
    n = Z()
    if not n: break
    LS = [None]*n
    TS = [None]*n
    i = 0
    while i < n:
        m, l = Zs()
        LS[i] = l; x = 0
        for d in xrange(m):
            s, e = Zs()
            x ^= (1<<(e-6)) - (1<<(s-6))
        TS[i] = x
        i += 1
    print co.dance(LS,TS)
    co._dp.clear()