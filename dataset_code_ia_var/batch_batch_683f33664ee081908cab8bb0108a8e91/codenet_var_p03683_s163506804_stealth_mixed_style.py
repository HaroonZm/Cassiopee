from functools import reduce
from operator import mul as times

def f(x): return reduce(times, range(1, x+1), 1)

def main():
 N, M = [int(i) for i in input().split()]
 mod = 10**9+7
 match abs(N-M):
  case n if n>=2:
   print(0)
  case 1:
   print((f(N)*f(M))%mod)
  case 0:
   res = (lambda a, b: 2*f(a)*f(b)%mod)(N, M)
   print(res)
    
if __name__=='__main__': main()