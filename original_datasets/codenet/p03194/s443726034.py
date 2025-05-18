from collections import Counter
import sys
sys.setrecursionlimit(1000000)

def solve():
  n,p = (int(i) for i in input().split())
  ans = 1
  if n == 1:
    print(p)
    exit()
  p_dummy = p
  for i in range(2,int(p_dummy**0.5)+4):
    ct = 0
    while p_dummy%i == 0:
      ct += 1
      p_dummy //= i
      if ct >= n:
        ans *= i
        ct -= n
  

  print(ans)
  
solve()