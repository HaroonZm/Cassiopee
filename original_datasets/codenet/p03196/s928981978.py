from fractions import gcd
from random import randint

def brent(N):
   # brent returns a divisor not guaranteed to be prime, returns n if n prime
   if N%2==0: return 2
   y,c,m = randint(1, N-1),randint(1, N-1),randint(1, N-1)
   g,r,q = 1,1,1
   while g==1:             
       x = y
       for i in range(r):
          y = ((y*y)%N+c)%N
       k = 0
       while (k<r and g==1):
          ys = y
          for i in range(min(m,r-k)):
             y = ((y*y)%N+c)%N
             q = q*(abs(x-y))%N
          g = gcd(q,N)
          k = k + m
       r = r*2
   if g==N:
       while True:
          ys = ((ys*ys)%N+c)%N
          g = gcd(abs(x-ys),N)
          if g>1:  break
   return g

def factorize(n1):
    if n1<=0: return []
    if n1==1: return [1]
    n=n1
    t = {}
    p=0
    mx=1000000
    if n%2 == 0: 
        t[2]=0
    if n%3 == 0:
        t[3]=0
    while n % 2 ==0 :
        t[2] += 1
        n//=2
    
    while n % 3 ==0 : 
        t[3] += 1;n//=3
        
    
    i=5
    inc=2
    # print(n)
    #use trial division for factors below 1M
    while i <=mx:
       while n % i ==0 : 
           if i not in t.keys():
               t[i] = 0
           t[i] += 1
           n//=i
       i+=inc
       inc=6-inc
    #use brent for factors >1M  
    # print(t)
    while n>mx:
      p1=n
      #iterate until n=brent(n) => n is prime
      while p1!=p:
          p=p1
          p1=brent(p)
      # print(p1)
      if p1 not in t.keys():
          t[p1] = 0
      t[p1] += 1;n//=p1 
    # print(n)
    if n!=1:
        t[n] = 1
    return t

from functools import reduce
from sys import argv
def main():
    n, p = tuple(map(int, input().strip().split()))
    if p==1:
        print(1)
        return
    q = factorize(p)
    # print(q)
    ans = 1
    for a in q.keys():
        q[a] //= n
        ans = ans * (a**q[a])
    print(ans)     
    

if __name__ == "__main__":
   main()