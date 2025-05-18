import math
import collections

# 0以上整数x「未満」の素数をリストに格納して返す
def primes(x):
    if x < 2: return []

    primes = [i for i in range(x)]
    primes[1] = 0 # 1は素数ではない

    # エラトステネスのふるい
    for prime in primes:
        if prime > math.sqrt(x): break
        if prime == 0: continue
        for non_prime in range(2 * prime, x, prime): primes[non_prime] = 0

    return [prime for prime in primes if prime != 0]

p = primes(1000)
dic = collections.defaultdict(int)
N = int(input())
mod = 10**9 +7
for i in range(1, N+1):
    for j in p:
        while i % j == 0:
            dic[j] += 1
            i = i // j
    ans = 1
for c in dic.values():
    ans *= (c+1)
    ans %= mod
print(ans)