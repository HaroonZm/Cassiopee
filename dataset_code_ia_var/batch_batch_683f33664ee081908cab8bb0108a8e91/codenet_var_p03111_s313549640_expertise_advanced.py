import sys
import math
import bisect
from collections import defaultdict, deque
from functools import lru_cache
from itertools import combinations, product

# Constants
MOD = 10 ** 9 + 7
INF = float('inf')

# Fast I/O
input = sys.stdin.readline

# Input
I = lambda: int(input())
S = lambda: input().strip()
IL = lambda: list(map(int, input().split()))
SL = lambda: input().split()
ILs = lambda n: [int(input()) for _ in range(n)]
SLs = lambda n: [input().strip() for _ in range(n)]
ILL = lambda n: [list(map(int, input().split())) for _ in range(n)]
SLL = lambda n: [input().split() for _ in range(n)]

# Output
def P(arg): print(arg)
def Y(): print('Yes')
def N(): print('No')
def E(): exit()
def PE(arg): print(arg); exit()
def YE(): print("Yes"); exit()
def NE(): print("No"); exit()

# Shorten
DD = lambda arg: defaultdict(arg)

# Inverse
inv = lambda n: pow(n, MOD-2, MOD)

# Combinations (with memoization)
from operator import mul
from functools import reduce

_kaijo = [1]
def kaijo(n):
    if len(_kaijo) <= n:
        _kaijo.extend(reduce(lambda x, y: x+[x[-1]*(y)%MOD], range(len(_kaijo), n+1), [_kaijo[-1]])[1:])
    return _kaijo[n]
    
_gyaku_kaijo = [1]
def gyaku_kaijo(n): 
    while len(_gyaku_kaijo) <= n:
        _gyaku_kaijo.append(_gyaku_kaijo[-1] * pow(len(_gyaku_kaijo), MOD-2, MOD) % MOD)
    return _gyaku_kaijo[n]

def nCr(n, r):
    if n < r or r < 0: return 0
    if n == r: return 1
    return kaijo(n) * gyaku_kaijo(r) % MOD * gyaku_kaijo(n - r) % MOD

# Factorization
def factorization(n):
    res, t = [], n
    for i in range(2, int(n**0.5)+1):
        if t % i == 0:
            cnt = 0
            while t % i == 0: cnt += 1; t //= i
            res.append([i, cnt])
    if t != 1: res.append([t, 1])
    if not res: res.append([n, 1])
    return res

# Divisors
def make_divisors(n):
    small, large = [], []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            small.append(i)
            if i != n // i:
                large.append(n // i)
    return small + large[::-1]

# Primes
def make_primes(N):
    sieve = [True] * (N + 1)
    for i in range(2, int(N ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i:N + 1:i] = [False] * len(range(i * i, N + 1, i))
    return [i for i in range(2, N + 1) if sieve[i]]

# GCD & LCM
gcd = math.gcd
lcm = lambda a, b: a * b // gcd(a, b)

# Bit count
count_bit = lambda n: bin(n).count('1')

# Base conversion
def base_10_to_n(X, n):
    res = []
    while X:
        res.append(X % n)
        X //= n
    return res[::-1] or [0]
base_n_to_10 = lambda X, n: sum(int(d) * n ** i for i, d in enumerate(str(X)[::-1]))

# Integer log
def int_log(n, a):
    cnt = 0
    while n >= a:
        n //= a
        cnt += 1
    return cnt

# Main
N, A, B, C = IL()
L = ILs(N)

from itertools import product

def mp_cost(sub, target):
    if not sub: return INF
    return abs(sum(sub) - target) + (len(sub)-1)*10

MIN = INF

idx = [i for i in range(N)]
for assign in product((0,1,2,3), repeat=N):
    t = [[],[],[],[]]  # 0=unused, 1=A, 2=B, 3=C
    for i, x in enumerate(assign):
        t[x].append(L[i])
    if 0 in (len(t[1]), len(t[2]), len(t[3])): continue
    total = mp_cost(t[1],A) + mp_cost(t[2],B) + mp_cost(t[3],C)
    MIN = min(MIN, total)

print(MIN)