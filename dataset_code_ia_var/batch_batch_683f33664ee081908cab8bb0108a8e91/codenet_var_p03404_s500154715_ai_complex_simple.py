####################
# Libraries Import  #
####################

import sys
from itertools import chain, islice
from functools import reduce, lru_cache, partial
from collections import defaultdict, deque, Counter
import math
import bisect
import heapq

input = sys.stdin.readline

####################
# Constants        #
####################

MOD, INF, AZ = 10**9+7, float('inf'), "".join(chr(97+i) for i in range(26))

####################
# Input Functions  #
####################

I      = lambda: int(input().strip())
S      = lambda: input().strip()
IL     = lambda: list(map(int,input().split()))
SL     = lambda: input().split()
ILs    = lambda n: [int(input()) for _ in range(n)]
SLs    = lambda n: [input().strip() for _ in range(n)]
ILL    = lambda n: [list(map(int, input().split())) for _ in range(n)]
SLL    = lambda n: [input().split() for _ in range(n)]

####################
# Output Functions #
####################

P  = lambda arg: (print(arg),)[0]
Y  = lambda: (print("Yes"),)[0]
N  = lambda: (print("No"),)[0]
E  = lambda: sys.exit()
PE = lambda arg: (print(arg),sys.exit())
YE = lambda: (print("Yes"),sys.exit())
NE = lambda: (print("No"),sys.exit())

####################
# Misc Utilities   #
####################

DD = lambda arg: defaultdict(arg)
inv = lambda n: pow(n, MOD-2, MOD)

############ Combination ############

kaijo_memo = []
def kaijo(n):
    global kaijo_memo
    extend = lambda v: v.append(v[-1]*len(v)%MOD)
    if not kaijo_memo: kaijo_memo.append(1)
    _ = list(map(extend, [kaijo_memo]*max(0, n+1-len(kaijo_memo))))
    return kaijo_memo[n]

gyaku_kaijo_memo = []
def gyaku_kaijo(n):
    global gyaku_kaijo_memo
    extend = lambda v: v.append(v[-1]*pow(len(v), MOD-2, MOD)%MOD)
    if not gyaku_kaijo_memo: gyaku_kaijo_memo.append(1)
    _ = list(map(extend, [gyaku_kaijo_memo]*max(0, n+1-len(gyaku_kaijo_memo))))
    return gyaku_kaijo_memo[n]

def nCr(n, r):
    return int((n >= r >= 0) and (kaijo(n) * gyaku_kaijo(r) * gyaku_kaijo(n-r) % MOD) or (n==r))

############## Factorization #############

def factorization(n):
    f = lambda x: [x,1]
    primes = []
    for i in range(2, int(-(-n**0.5//1))+1):
        cnt, n = reduce(lambda x, _: (x[0]+1, x[1]//i), range(1000) if n%i==0 else [], (0, n)) if n%i==0 else (0, n)
        if cnt: primes.append([i, cnt])
    if n != 1: primes.append(f(n))
    return primes if primes else [f(n)]

############## Divisors #############

def make_divisors(n):
    return sorted(set(chain.from_iterable(
        ((i, n//i) if i!=n//i else (i,)) for i in range(1, int(n**.5)+1) if n%i==0
    )))

############## Primes (Sieve) #############

def make_primes(N):
    not_prime = set()
    nums = list(range(2, N+1))
    primes = []
    next_num = lambda: next(filter(lambda x: x not in not_prime, nums), None)
    n = next_num()
    while n and n**2 <= N:
        primes.append(n)
        not_prime.update(range(n*2, N+1, n))
        n = next_num()
    return primes + [x for x in nums if x not in not_prime and x not in primes]

############ GCD/LCM ##############

def gcd(a,b): return math.gcd(a,b)
def lcm(a,b): return a*b//gcd(a,b)

############ Bit Count ############

def count_bit(n): return sum(map(int, bin(n)[2:]))

############ Base Conversion ############

def base_10_to_n(X, n):
    return list(map(int, reversed(format(X, f'0{0}b' if n==2 else "")))) if n==2 else (base_10_to_n(X//n, n)+[X%n] if X//n else [X%n])

def base_n_to_10(X, n):
    return sum(int(d)*n**i for i,d in enumerate(str(X)[::-1]))

def base_10_to_n_without_0(X, n):
    X -= 1
    return base_10_to_n_without_0(X//n, n)+[X%n] if X//n else [X%n]

############ IntLog ############

def int_log(n, a):
    try:
        return next(i for i in range(0, n+2) if a**i > n)-1
    except StopIteration:
        return 0

############################
# Main code, tangled style #
############################

A,B = IL()
print(100,100)

A_cluster = ["#"] * (25*50-(A-1)) + ["."] * (A-1)
B_cluster = ["#"] * (B-1) + ["."] * (25*50-(B-1))

def chunked(seq, n):
    it = iter(seq)
    while True:
        chunk = list(islice(it, n))
        if not chunk:
            break
        yield chunk

# Dispersed print with chained comprehensions, generator gymnastics
for arr, edge, fill_chr in (
    (A_cluster, "#", "#"),
    (B_cluster, ".", "."),
):
    for j in range(25):
        line = ''.join(chain.from_iterable([[arr.pop() if arr else fill_chr, fill_chr] for _ in range(50)]))
        print(line)
    print(edge*100)

for j in range(25):
    print("."*100)
    line = ''.join(chain.from_iterable([[B_cluster.pop() if B_cluster else ".", "."] for _ in range(50)]))
    print(line)