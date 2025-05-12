def extgcd(a, b):
  if b == 0:
    return 1
  else:
    x, y, u, v, k, l = 1, 0, 0, 1, a, b
    while l != 0:
      x, y, u, v = u, v, x - u * (k // l), y - v * (k // l)
      k, l = l, k % l
    return x
def inved(x, m):
  return x % m
def gcd(x, y):
  while y != 0:
    x, y = y, x % y
  return x
def doubling(n, m, mod):
  y = 1
  base = n
  while m != 0:
    if m % 2 == 1:
      y *= base
      y %= mod
    base *= base
    base %= mod
    m //= 2
  return y
def factorization(n):
  if n == 1:
    return {1: 1}
  else:
    D = {}
    base = n
    p = 2
    while n != 1:
      i = 0
      while n % p == 0:
        i += 1
        n //= p
      if i != 0:
        D[p] = i
      p += 1
      if p * p > base and n != 1:
        D[n] = 1
        break
    return D
def Torshent(n):
  dic = factorization(n)
  S = n
  for i in dic:
    S //= i
    S *= i - 1
  return S
def bin_digits(n):
  cnt = 0
  while n != 0:
    cnt += 1
    n //= 2
  return cnt
def Resque(a, mod):
  if mod == 1:
    return 1
  M = Torshent(mod)
  MM = gcd(M, mod)
  R = Resque(a, MM)
  k = doubling(a, R, mod)
  m, modmod = M // MM, mod // MM
  Tm = Torshent(modmod)
  invm = doubling(m, Tm-1, modmod)
  t = ((k - R) // MM) * invm
  R += t * M
  R %= (mod * M // MM)
  R += (mod * M // MM)
  return R

#---------------------------------------------------------------#

Q = int(input())
for i in range(Q):
  A, M = map(int, input().split())
  if M == 1:
    print(1)
  else:
    R = Resque(A, M)
    print(R)