from functools import reduce
from itertools import product, chain, starmap, count, takewhile
import math
from operator import mul

def divisors_pairs(n):
    sq = int(math.isqrt(n))
    # Find i in 1..100 if i divides n and i <= sqrt(n)
    valid_is = filter(lambda i: n % i == 0 and i <= sq, range(1, 101))
    # For each, get [i, n//i]
    return list(starmap(lambda i, ni: [i, ni], ((i, n//i) for i in valid_is)))

def min_ruin(anum, bnum):
    # For all pairs, get the concatenation, sort, find the ruin, and take min
    def ruin(z):
        u = sorted(z)
        return sum((u[j]-u[j-1])**2 for j in range(1,4))
    return min(starmap(ruin, product(anum, bnum)), default=float('inf'))

def unfold_input():
    # Generator reading stdin, ending with a==0
    try:
        while True:
            vals = raw_input()
            if not vals: continue
            a,b = map(int, vals.split())
            if a == 0: break
            yield a,b
    except EOFError:
        return

def main():
    list(map(lambda ab: print(
        min_ruin(divisors_pairs(ab[0]), divisors_pairs(ab[1]))
    ), unfold_input()))

main()