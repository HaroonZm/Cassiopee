import math

a, b = map(int, input().split())
fa = math.factorial(a)
fb = math.factorial(b)
mod = 10**9 + 7
fa %= mod
fb %= mod
k = fa*fb

if abs(a-b) >= 2:
  print(0)
elif abs(a-b) == 1:
  print(k%mod)
elif abs(a-b) == 0:
  print((2*k) % mod)