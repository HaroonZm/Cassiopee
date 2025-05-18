class SegmentTree():
    def __init__(self, init, unit, f):
        self.unit = unit
        self.f = f
        if type(init) == int:
            self.n = init
            # self.n = 1 << (self.n - 1).bit_length()
            self.X = [unit] * (self.n * 2)
        else:
            self.n = len(init)
            # self.n = 1 << (self.n - 1).bit_length()
            self.X = [unit] * self.n + init + [unit] * (self.n - len(init))
            for i in range(self.n-1, 0, -1):
                self.X[i] = self.f(self.X[i*2], self.X[i*2|1])
    
    def getvalue(self, i):
        i += self.n
        return self.X[i]
        
    def update(self, i, x):
        i += self.n
        self.X[i] = x
        i >>= 1
        while i:
            self.X[i] = self.f(self.X[i*2], self.X[i*2|1])
            i >>= 1
    
    def add(self, i, x):
        i += self.n
        self.X[i] = (self.X[i] + x) % mod
        i >>= 1
        while i:
            self.X[i] = self.f(self.X[i*2], self.X[i*2|1])
            i >>= 1
    
    def getrange(self, l, r):
        l += self.n
        r += self.n
        al = self.unit
        ar = self.unit
        while l < r:
            if l & 1:
                al = self.f(al, self.X[l])
                l += 1
            if r & 1:
                r -= 1
                ar = self.f(self.X[r], ar)
            l >>= 1
            r >>= 1
        return self.f(al, ar)
    
    def debug(self):
        de = []
        a, b = self.n, self.n * 2
        while b:
            de.append(self.X[a:b])
            a, b = a//2, a
        print("--- debug ---")
        for d in de[::-1]:
            print(d)
        print("--- ---")

def r(a):
    for i in range(1, 10001):
        if i and a * i % mod <= 10000:
            return str(a*i%mod) + "/" + str(i)
        if i and -a * i % mod <= 10000:
            return str(-(-a*i%mod)) + "/" + str(i)
    return a

mod = 998244353
N, K = map(int, input().split())
P = [int(a) - 1 for a in input().split()]
f = lambda a, b: (a + b) % mod

p1 = (K - 1) * (K - 2) * pow(4, mod - 2, mod) % mod
p2 = K * (K - 1) * pow(4, mod - 2, mod) % mod
m = (K - 1) * pow(K, mod - 2, mod) % mod
invm = K * pow(K - 1, mod - 2, mod) % mod

st1 = SegmentTree(N, 0, f)
st2 = SegmentTree(N, 0, f)
ans = p2
for i, x in enumerate(P):
    if i >= K:
        ans = (ans + st1.getrange(x, N)) % mod
    st1.add(x, 1)

s = 1
invs = 1
st = SegmentTree(N, 0, f)
for i, x in enumerate(P[:K]):
    st.add(x, 1)
for i in range(K, N):
    s = s * m % mod
    invs = invs * invm % mod
    x = P[i]
    a = st.getrange(x, N) * s % mod
    ans = (ans + p2 - p1 - a) % mod
    st.add(x, invs % mod)

print(ans)