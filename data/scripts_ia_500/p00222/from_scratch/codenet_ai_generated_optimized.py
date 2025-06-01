import sys
import math

MAX_N = 10_000_000

def sieve(n):
    sieve = [True]*(n+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(n))+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return sieve

prime = sieve(MAX_N)
four_prime_max = [0]*(MAX_N+1)
last = 0
for a in range(5, MAX_N-7):
    if prime[a] and prime[a+2] and prime[a+6] and prime[a+8]:
        last = a+8
    four_prime_max[a+8] = last
for i in range(5, MAX_N+1):
    if four_prime_max[i] == 0:
        four_prime_max[i] = four_prime_max[i-1]

input = sys.stdin.readline
while True:
    n = int(input())
    if n == 0:
        break
    if n < 13:
        print(0)
    else:
        print(four_prime_max[n])