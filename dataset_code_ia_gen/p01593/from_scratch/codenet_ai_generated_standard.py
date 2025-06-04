import math

def earn_big_probability(N, M):
    fact = math.factorial
    res = 0.0
    for k in range(M+1, N+1):
        sign = -1 if (k - M) % 2 else 1
        comb = math.comb(N, k)
        p = fact(N - k) / fact(N)
        res += sign * comb * p
    return 1 - res

N, M = map(int, input().split())
print(f"{earn_big_probability(N,M):.8f}")