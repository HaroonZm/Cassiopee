import itertools
import sys

N = 999999
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41] 
primeb = [0 for i in range(N+1)]
 
for i in primes:
  primeb[i] = 1
 
def isprime(n):
  for p in primes:
    if (n % p == 0):
      return True
    if (n < p*p):
      return False 
S = primes[-1]
for i in range(S, N):
  if isprime(i):
    pass 
  else: 
    primes.append(i)
    primeb[i] = 1

for line in sys.stdin:
  n = int(line)
  print sum(primeb[:n+1])