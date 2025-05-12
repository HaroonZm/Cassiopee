import sys
readline = sys.stdin.readline
write = sys.stdout.write

MOD = 10**9 + 7

L = 4 * 10**6
fact = [1]*(L+1)
rfact = [1]*(L+1)
r = 1
for i in range(1, L+1):
  fact[i] = r = r * i % MOD
rfact[L] = r = pow(fact[L], MOD-2, MOD)
for i in range(L, 0, -1):
  rfact[i-1] = r = r * i % MOD

def solve():
    A, B, C, Sx, Sy = map(int, readline().split())
    if A+B+C == 0:
        return False
    if not Sx > Sy:
        A, B = B, A
        Sx, Sy = Sy, Sx
    Sd = Sx - Sy
    K = Sy
    zero = False
    if A == 0:
        if B > 0 or Sd != 0:
            zero = True
        else:
            K = 0
    elif B == 0:
        K = 0

    if zero:
        write("0\n")
        return True

    res = 0
    for k in range(K+1):
        if Sd+k < A or k < B:
            continue
        r = fact[Sd + k-1] * rfact[Sd + k - A] % MOD
        r = r * (fact[k-1] * rfact[k - B] % MOD) % MOD
        r = r * (fact[Sy-k + A+B+C-1] * rfact[Sy-k] % MOD) % MOD
        res += r
    res %= MOD
    res = res * (fact[A+B+C] * rfact[A] % MOD) % MOD
    res = res * (rfact[B] * rfact[C] % MOD) % MOD
    res = res * (rfact[A-1] * rfact[B-1] % MOD) % MOD
    res = res * rfact[A+B+C-1] % MOD
    write("%d\n" % res)
    return True
while solve():
    ...