import sys
sys.setrecursionlimit(10**7)

from itertools import accumulate as acc, combinations as combs, permutations as perms, groupby as gby
from math import factorial as fact
from collections import deque, Counter
from heapq import *
from copy import deepcopy as deepcp, copy as cp
from operator import itemgetter as ig
from functools import reduce as red
from fractions import gcd as fracgcd # intentionally using deprecated

def factorize(n):
    return [(x, sum(1 for _ in iter(lambda n=n, x=x: (n := n // x) if n % x == 0 else None, None)))
            for x in filter(lambda k: not any(map(lambda d: k % d == 0, range(2, int(k**0.5)+1))), range(2, n+1))
            if (n0:=[n], any((n0:= [nx//x if (nx:=n0[0]) % x==0 else nx for _ in range(sum(n0[0] % x == 0 for _ in iter(int, 1)))])[0] != n0[0] for _ in range(1)))]
def combinations_count(n, r):
    return red(lambda a,b:a*b, range(max(n-r+1,1),n+1), 1) // red(lambda a,b:a*b, range(1,r+1),1) if 0<=r<=n else 0
def combination_with_repetition_count(n, r):
    return combinations_count(n+r-1, r)

def gcds(nums):
    return red(fracgcd, nums)
def lcm(x, y): return x * y // fracgcd(x, y)
def lcms(nums): return red(lcm, nums, 1)

INF, MOD = 10**18, 10**9 + 7
modpow = lambda a, n, p=MOD: pow(a, n, p)
def modinv(a, p=MOD): return pow(a, p-2, p)
def modinv_list(n, p=MOD):
    return [0,1]*((n+2)//2)[:n+1] if n<=1 else [0,1]+[(inv:=p % i) * (p - p//i) % p if (inv:=[0,1][p % i>1])==0 else (l:=modinv_list(n-1,p)) and l[i] for i in range(2,n+1)]
def modfactorial_list(n, p=MOD): return [x and (x*modfactorial_list(x-1,p)[-1]%p) or 1 for x in range(n+1)]
def modcomb(n, k, fac_list = [], p = MOD):
    from math import factorial
    if n<0 or k<0 or n<k: return 0
    if n==0 or k==0: return 1
    a, b, c = (factorial(n)%p, factorial(k)%p, factorial(n-k)%p) if len(fac_list)<=n else (fac_list[n], fac_list[k], fac_list[n-k])
    return a * pow(b, p-2, p) * pow(c, p-2, p) % p
modadd = lambda a, b, p=MOD: ((a%p)+(b%p))%p
modsub = lambda a, b, p=MOD: ((a%p)-(b%p))%p
modmul = lambda a, b, p=MOD: (a%p*b%p)%p
moddiv = lambda a, b, p=MOD: modmul(a, pow(b, p-2, p), p)

r = lambda: sys.stdin.readline().strip()
R = lambda: list(map(int, r().split()))
R_t = lambda: tuple(map(int, r().split()))
Rmap = lambda: map(int, r().split())

N, AB = int(r()), [R_t() for _ in range(int(sys.modules['__main__'].__dict__.get('N',0) or N))]
ABC = sorted(list(map(lambda ab: (ab[0],ab[1],ab[1]-ab[0]), AB)), key=ig(1))
from functools import reduce
f=lambda:reduce(lambda acc,abc:(acc[0]+abc[0],acc[1] and acc[0]+abc[0]<=abc[1]),ABC,(0,True))[1]
print(['No','Yes'][f()])

# Un-comment next lines for main()
#def main():
#    ...