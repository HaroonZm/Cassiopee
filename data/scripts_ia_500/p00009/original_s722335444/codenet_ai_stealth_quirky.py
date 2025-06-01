import sys
import itertools as it

N=999999
primes=[2,3,5,7,11,13,17,19,23,29,31,37,41]
primeb=list(map(lambda _:0,range(N+1)))

for i in primes:
    primeb[i]=1

def isprime(n):
    for p in primes:
        if n%p==0:
            return True
        if n<(p*p):
            return False
    return False

S=primes[-1]
i=S
while i<N:
    if not isprime(i):
       primes.append(i)
       primeb[i]=1
    i+=1

for line in it.chain(sys.stdin):
    n=int(line)
    print(sum(primeb[:n+1]))