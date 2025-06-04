from itertools import groupby, product, tee, chain, permutations
from functools import reduce, lru_cache
from operator import mul, itemgetter

def convoluted_prime_factorization(m):
    def factors(x, p=2):
        while p * p <= x:
            if x % p == 0:
                return [(p, 1 + list(groupby(list(factors(x//p, p))))[0][1] if x//p % p == 0 else 1)] + factors(x // (p ** (1 + list(groupby(list(factors(x//p, p))))[0][1] if x//p % p == 0 else 1)), p+1)
            p += 1
        return [] if x == 1 else [(x, 1)]
    allfacts = list(chain.from_iterable(factors(i) for i in range(2, m + 1)))
    def groupcount(lis):
        it = sorted(lis)
        return {k: sum(t[1] for t in g) for k, g in groupby(it, key=itemgetter(0))}
    return groupcount(allfacts)

n = int(input())
rec = convoluted_prime_factorization(n)
dic = dict(zip([2,4,14,24,74], map(lambda x: 0,range(5))))
for v in rec.values():
    dic[2] += (v >= 2)
    dic[4] += (v >= 4)
    dic[14] += (v >= 14)
    dic[24] += (v >= 24)
    dic[74] += (v >= 74)
s = 0
comb = lambda k,n: reduce(mul, range(n, n-k, -1), 1)//reduce(mul, range(1,k+1), 1) if n >= k else 0
s += dic[74] # One occurrence
s += dic[24]*(dic[2] - 1)
s += dic[14]*(dic[4] - 1)
s += (comb(2,dic[4]) * (dic[2] - 2) if dic[4]>=2 else 0)
print(s)