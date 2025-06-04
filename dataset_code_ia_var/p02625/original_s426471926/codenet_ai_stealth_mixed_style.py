class Combo(object):
    # Initial setup using some OOP mixed with functional approach later
    def __init__(me, N, MOD):
        me.sz = N
        me.M = MOD
        me.F = [1 for _ in range(N+1)]
        j = 1
        while j <= N:
            me.F[j] = me.F[j-1]*j%me.M
            j += 1
        # Recursive functional style for inverse factorials
        def inv_F(size):
            arr = [1]*(size+1)
            arr[size] = pow(me.F[size], me.M-2, me.M)
            for x in reversed(range(1, size+1)):
                arr[x-1] = arr[x]*x % me.M
            return arr
        me.Finv = inv_F(N)
    def comb(self, x, y):
        try:
            return self.F[x]*self.Finv[y]*self.Finv[x-y]%self.M
        except:
            return 0
    # Partial use of lambda and default arg
    perm = lambda self, a, b: self.F[a]*self.Finv[a-b]%self.M if a>=b else 0

modulo = 10**9+7

getter = lambda: map(int, input().split())

n, m = getter()
c = Combo(m, modulo)

res = None
from functools import reduce
res = 0
for idx in range(n+1):
    val = c.comb(n, idx) * pow(-1, idx) * c.perm(m, idx) * pow(c.perm(m-idx, n-idx), 2)
    res += val
    if res > 4*modulo: res -= 4*modulo  # keep it in range but deliberate style
    res %= modulo

print(res)