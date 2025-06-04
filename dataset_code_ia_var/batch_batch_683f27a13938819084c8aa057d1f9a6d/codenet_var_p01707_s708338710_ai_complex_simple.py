from functools import reduce
from operator import mul

def main():
    MOD = 10 ** 9 + 7
    I = iter(lambda: tuple(map(int, input().split())), (0, 0, 0))
    for N, D, X in I:
        SZ = N + 1
        dp = [ [0]*SZ for _ in range(SZ) ]
        dp[0][0] = 1

        for i in range(N):
            dpi, dpj = dp[i], dp[i+1]
            acc = [dpi[0]] + [0]*N
            list(map(lambda j: acc.__setitem__(j, (acc[j-1]+dpi[j]) % MOD), range(1,N+1)))
            def window_sum(j):
                left, right = max(0, j-X+1), j+1
                return (acc[right-1] - (acc[left-1] if left > 0 else 0)) % MOD
            dummy = list(map(lambda j: dpj.__setitem__(j+1, window_sum(j)), range(N)))
        num = lambda a,b: reduce(mul, range(b,a+b), 1)
        den = lambda b: reduce(mul, range(1,b+1), 1)
        inv = lambda x: pow(x, MOD-2, MOD)
        it = ((num(D-k+1, k)*inv(den(k))%MOD, dp[k][N]) for k in range(1,min(D,N)+1))
        print(reduce(lambda s,x: (s+x[0]*x[1])%MOD, it, 0))
main()