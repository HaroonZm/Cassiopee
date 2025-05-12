from functools import lru_cache
import sys
mod=1000000007

n,k=[int(i) for i in input().split(" ")]

facts=[1 for i in range(n+k+1)]

for i in range(1,n+k+1):
    facts[i]=i*facts[i-1]

@lru_cache()
def combination(i,j):
    return facts[i]//(facts[j]*facts[i-j])

if n<k:
    print(0)
    sys.exit()

print(combination(n-1,k-1)%mod)