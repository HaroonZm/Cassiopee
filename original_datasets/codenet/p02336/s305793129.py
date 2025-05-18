MOD = 1000000007
lim = 10 ** 4+1
fac = [0] * lim
finv = [0] * lim
inv = [0] * lim

class ModInt:
    def __init__(self, x):
        self.x = x % MOD

    def __str__(self):
        return str(self.x)
    def __int__(self):
        return self.x

    __repr__ = __str__

    def __add__(self, other):
        return (
            ModInt(self.x + other.x) if isinstance(other, ModInt) else
            ModInt(self.x + other)
        )

    def __sub__(self, other):
        return (
            ModInt(self.x - other.x) if isinstance(other, ModInt) else
            ModInt(self.x - other)
        )

    def __mul__(self, other):
        return (
            ModInt(self.x * other.x) if isinstance(other, ModInt) else
            ModInt(self.x * other)
        )

    def __truediv__(self, other):
        return (
            ModInt(
                self.x * pow(other.x, MOD - 2, MOD)
            ) if isinstance(other, ModInt) else
            ModInt(self.x * pow(other, MOD - 2, MOD))
        )

    def __mod__(self, other):
        return (
            ModInt(
                other.x
            ) if isinstance(other, ModInt) else
            self.x
        )

    def __pow__(self, other):
        return (
            ModInt(pow(self.x, other.x, MOD)) if isinstance(other, ModInt) else
            ModInt(pow(self.x, other, MOD))
        )

    __radd__ = __add__

    def __rsub__(self, other):
        return (
            ModInt(other.x - self.x) if isinstance(other, ModInt) else
            ModInt(other - self.x)
        )

    __rmul__ = __mul__

    def __rtruediv__(self, other):
        return (
            ModInt(
                other.x * pow(self.x, MOD - 2, MOD)
            ) if isinstance(other, ModInt) else
            ModInt(other * pow(self.x, MOD - 2, MOD))
        )

    def __rpow__(self, other):
        return (
            ModInt(pow(other.x, self.x, MOD)) if isinstance(other, ModInt) else
            ModInt(pow(other, self.x, MOD))
        )
    
    def __iadd__(self,other):
        self.x += other.x if isinstance(other, ModInt) else other
        self.x %= MOD
        return self

    def __isub__(self,other):
        self.x += ModInt(MOD - other.x) if isinstance(other, ModInt) else ModInt(MOD - other)
        return self

    def __imul__(self, other):
        self.x *= other.x if isinstance(other, ModInt) else other
        self.x %= MOD
        return self
    
    def __ifloordiv__(self, other):
        self.x *= pow(int(other), MOD - 2, MOD)
        return self
    
    def factorical(self,n):
        tmp = ModInt(1)
        for i in range(n):
            tmp *= (i+1)
        return tmp
    
    #m:int MOD
    def modinv(self,a,m=MOD):
        b = m
        u = 1
        v = 0
        while(b):
            t = a//b
            a -= t * b
            a,b = b,a
            u -= t * v
            u,v = v,u
        return ModInt(u)

    def comb(self,n,r):
        n = int(n)
        r = int(r)
        if r > n or n < 0 or r < 0:
            return 0
        m = n+1
        nterms = min(r, n-r)
        numerator = ModInt(1)
        denominator = ModInt(1)
        for j in range(1, nterms + 1):
            numerator *= m - j
            denominator *= j
        return numerator * self.modinv(denominator.x)

def COMinit():
    fac[0] = ModInt(1)
    fac[1] = ModInt(1)
    finv[0] = ModInt(1)
    finv[1] = ModInt(1)
    inv[1] = ModInt(1)
    for i in range(2,lim):
        fac[i] = ModInt(fac[i - 1] * i)
        inv[i] = ModInt(MOD - inv[MOD%i] * (MOD // i))
        finv[i] = ModInt(finv[i - 1] * inv[i])

def cmb(n,k) -> ModInt:
    if int(n) < int(k):
        return ModInt(0)
    if int(n) < 0 or int(k) < 0:
        return ModInt(0)
    if fac[0] == 0:
        COMinit()
    tmp = ModInt(finv[int(k)] * finv[int(n - k)])
    tmp *= fac[int(n)]
    return tmp

        
if __name__ == "__main__":
    n,k = map(int,input().split())
    if n < k:
        print(0)
    else:
        n -= k
        k -= 1
        print(cmb(n+k,k))