import numpy as np
def eratosthenes(n):
    is_prime = np.ones((n+1,), dtype=bool)
    is_prime[:2] = False
    for i in range(2,n+1):
        if is_prime[i]:
            is_prime[i*2::i]=False
    return np.arange(n+1)[is_prime]
Ps = eratosthenes(1000)
def divisor(n):
    for p in Ps:
        if p*p>n:return -1
        if n%p==0:return p
def prime_division(n):
    d={}
    while n>1:
        p=divisor(n)
        if p==-1:d[n]=d.get(n,0)+1;break
        else:d[p]=d.get(p,0)+1;n//=p
    return d

N=int(input())
d={}
for i in range(1,N):
  p=prime_division(i+1)
  for k,v in p.items():
    d[k]=d.get(k,0)+v
r=1
for v in d.values():
  r=r*(v+1)%1000000007
print(r)