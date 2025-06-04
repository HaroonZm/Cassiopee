import sys
import bisect

MAX_N = 200000

def sieve(n):
    is_prime = [True]*(n+1)
    is_prime[0]=False
    is_prime[1]=False
    for i in range(2,int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i,n+1,i):
                is_prime[j]=False
    return [i for i,v in enumerate(is_prime) if v]

primes = sieve(MAX_N+10000)

def solve(N,P):
    # find first prime > N
    idx = bisect.bisect_right(primes, N)
    primesN = primes[idx:]
    sums = []
    for i in range(len(primesN)):
        for j in range(i,len(primesN)):
            sums.append(primesN[i]+primesN[j])
    sums.sort()
    return sums[P-1]

for line in sys.stdin:
    if line.strip() == '':
        continue
    N,P = map(int,line.split())
    if N==-1 and P==-1:
        break
    print(solve(N,P))