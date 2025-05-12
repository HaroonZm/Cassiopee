def fib(n, p):
  F = [1] * (n + 1)
  for i in range(2, n + 1):
    F[i] = F[i - 1] * i % p
  return F
def finv(F, p):
  N = len(F) - 1
  Finv = list(F)
  Finv[-1] = pow(F[-1], p - 2, p)
  for i in range(N - 1, -1, -1):
    Finv[i] = Finv[i + 1] * (i + 1) % p
  return Finv
def comb(F, Finv, n, a, p):
  return F[n] * Finv[a] * Finv[n - a] % p
N, A, B, K = map(int, input().split())
p = 998244353
F = fib(N, p)
Finv = finv(F, p)
cnt = 0
for a in range(min(N + 1, K // A + 1)):
  _A = A * a
  if _A > K:
    continue
  if (K - _A) % B > 0:
    continue
  b = (K - _A) // B
  if b > N:
    continue
  cnt += comb(F, Finv, N, a, p) * comb(F, Finv, N, b, p)
  cnt %= p
print(cnt)