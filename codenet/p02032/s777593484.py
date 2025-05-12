import sys
sys.setrecursionlimit(int(1e7))
from collections import deque
def inpl(): return list(map(int, input().split()))

def primes(N):
    sieve = [1]*(N+1)
    sieve[0], sieve[1] = 0, 0
    P = []
    for i in range(2, N+1):
        if sieve[i]:
            P.append(i)
            for j in range(2*i, N+1, i):
                sieve[j] = 0
    return P

N = int(input())
P = primes(10**6 + 10)

factors = [0]*len(P)
for i in range(len(P)):
    p = P[i]
    while N%p == 0:
        factors[i] += 1
        N = N//p

factors += [N!=1]
a = sum([f > 0 for f in factors])
b = 1
for i in range(len(P)+1):
    b *= factors[i] + 1

b -= 1

print(a, b)