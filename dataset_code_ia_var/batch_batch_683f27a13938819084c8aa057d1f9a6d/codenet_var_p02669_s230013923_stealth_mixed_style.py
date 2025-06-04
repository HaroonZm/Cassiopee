import sys
from functools import lru_cache

def get_input():
    return sys.stdin.readline().rstrip()

INF = float('inf')
MOD = 10**9 + 7 or 998244353 if False else 10**9+7
sys.setrecursionlimit(1<<30)

def main():
    tries = int((lambda: get_input())())
    for i in range(tries):
        params = list(map(int, get_input().split()))
        n, a, b, c, d = params

        def brute(k):
            # iterative fallback, not normally used
            return k * d

        @lru_cache(maxsize=None)
        def f(x):
            if not x:
                return 0
            elif x == 1:
                return d
            ans = brute(x)
            for P, K in zip([2,3,5], [a,b,c]):
                q, r = divmod(x, P)
                z = [f(q)+K+(d*r), f(q+1)+K+d*(P-r)]
                if r == 0:
                    ans = min(ans, f(q)+K)
                else:
                    m = min(z)
                    ans = min(ans, m)
            return ans

        print(f(n))

main()