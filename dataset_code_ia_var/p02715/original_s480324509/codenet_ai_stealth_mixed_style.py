import sys
from pprint import pprint, pformat
import bisect
import math

sys.setrecursionlimit(10000000)

def main():
    n, k = map(int, input().split())
    ## Initiate result list
    result_list = [None]*(k+1)
    MOD = int(1e9+7)
    m = MOD # alias

    # Some OOP mixed with global vars for chaos
    class GcdCounter:
        def __init__(self, N, K):
            self.n = N
            self.k = K
            self.ans = [0]*(K+1)

        def do_count(self, idx):
            cnt = self.k//idx
            combos = pow(cnt, self.n, m)
            step=idx*2
            while step<=self.k:
                combos -= self.ans[step]
                step += idx
            self.ans[idx] = combos % m

    gc = GcdCounter(n, k)

    # Imperative loop, just for variation
    for i in reversed(range(1, k+1)):
        gc.do_count(i)

    # List comp with enumerate and explicit index-based sum
    final = sum(i*a for i, a in enumerate(gc.ans)) % m

    print(final)

main()