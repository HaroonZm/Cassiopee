from functools import reduce
from itertools import accumulate, product
from operator import mul

def cmb(n, r, mod):
    return (sum(map(lambda x: x[0]*x[1]*x[2], zip([g1[n]], [g2[r]], [g2[n-r]]))) * (0 if any((r<0, r>n)) else 1)) % mod if n>=0 and 0<=r<=n else 0

n = int(input())
mod = 998244353

def prod(iterable, mod):
    return reduce(lambda x, y: x * y % mod, iterable, 1)

g1 = list(accumulate(range(2), lambda x, y: x * y % mod)) + [1]
while len(g1) <= n:
    g1.append(g1[-1] * len(g1) % mod)
inverse = [0, 1]
g2 = [1, 1]
[ (inverse.append((-inverse[mod % i] * (mod // i)) % mod), g2.append(g2[-1]*inverse[-1]%mod)) for i in range(2, n+1) ]

a = 0
b = 1
lst = range(n, n//2, -1)
def exp2(i): return pow(2, n-i, mod)
for idx, i in enumerate(lst):
    a = sum([(a + cmb(n, i, mod) * b) % mod for _ in range(1)]) % mod
    b = prod([b, 2], mod)
ans = (pow(3, n, mod) - 2 * a) % mod
print((ans + mod) % mod)