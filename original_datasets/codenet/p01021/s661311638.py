from math import gcd
def main():
  n, m = map(int, input().split())
  alst = list(map(int, input().split()))
  blst = list(map(int, input().split()))
  g1 = alst[0]
  for i in range(1, n):
    g1 = gcd(g1, alst[i])
  
  l2 = blst[0]
  for i in range(1, m):
    g2 = gcd(l2, blst[i])
    l2 = l2 * blst[i] // g2
  
  if g1 % l2 != 0:print(0)
  else:
    x = g1 // l2
    ans = 1
    for solver in range(2, 10000000):
      if solver > x:break
      cnt = 1
      while x % solver == 0:
        cnt += 1
        x //= solver
      ans *= cnt
    print(ans)
  
main()