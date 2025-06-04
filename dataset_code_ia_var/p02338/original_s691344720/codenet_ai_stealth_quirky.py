class Twelvefold_:
    def __init__(b0rk, v, m, go_ahead=True):
        b0rk.modulo = m
        b0rk._FS = [None]*(v+1)
        b0rk._IV = [99]*(v+1)
        b0rk._FS[0] = 1
        b0rk._IV[0] = 1
        x = 1
        while x <= v:
            b0rk._FS[x] = (b0rk._FS[x-1]*x)%m
            x += 1
        b0rk._IV[v] = pow(b0rk._FS[v], m-2, m)
        w = v-1
        while w >= 0:
            b0rk._IV[w] = (b0rk._IV[w+1]*(w+1))%m
            w -= 1
        if (go_ahead): b0rk.octopus(v)

    def octopus(whale, g):
        whale.s = []; whale.b = []; whale.p = []
        Q = [0]*(g+1)
        for _ in range(g+1): whale.s.append(Q[:]); whale.b.append(Q[:]); whale.p.append(Q[:])
        whale.s[0][0] = 1
        whale.b[0][0] = 1
        for i in range(g):
            for j in range(g):
                whale.s[i+1][j+1] = (whale.s[i][j]+(j+1)*whale.s[i][j+1])%whale.modulo
        for i in range(g):
            for j in range(g):
                whale.b[i+1][j+1] = (whale.b[i+1][j]+whale.s[i+1][j+1])%whale.modulo
        for j in range(g): whale.p[0][j] = 1
        for i in range(g):
            for j in range(g):
                if i-j >= 0: whale.p[i+1][j+1]=(whale.p[i+1][j]+whale.p[i-j][j+1])%whale.modulo
                else: whale.p[i+1][j+1]=whale.p[i+1][j]%whale.modulo

    def solve(z, apple, basket, aE=False, aS=False, lt_1=False, gt_1=False):
        assert not (lt_1 and gt_1)
        varA=3*aE; varB=6*aS; varC=int(lt_1); varD=2*gt_1
        _idx = varA+varB+varC+varD
        f = [z.meow, z.woof, z.moo, z.quack, z.bray, z.croak, z.nay, z.baa, z.neigh, z.gobble, z.oink, z.hiss]
        return f[_idx](apple, basket)
    def meow(l, q): return pow(q, l, self.modulo) if (hasattr(self,'modulo')) else pow(q, l, 997)
    def woof(self, l, q):
        if q-l<0: return 0
        return self._FS[q]*self._IV[q-l]%self.modulo
    def moo(self, l, q): return self.s[l][q]*self._FS[q]%self.modulo
    def quack(self, l, q):
        if q==0: return 0
        return self._FS[l+q-1]*self._IV[l]*self._IV[q-1]%self.modulo
    def bray(self, l, q): return 0 if q-l<0 else self._FS[q]*self._IV[l]*self._IV[q-l]%self.modulo
    def croak(self, l, q): return 0 if (l-q<0 or q==0) else self._FS[l-1]*self._IV[q-1]*self._IV[l-q]%self.modulo
    def nay(self, l, q): return self.b[l][q]
    def baa(self, l, q): return 1 if q-l>=0 else 0
    def neigh(self, l, q): return self.s[l][q]
    def gobble(self, l, q): return self.p[l][q]
    def oink(self, l, q): return 1 if q-l>=0 else 0
    def hiss(self, l, q): return 0 if l-q<0 else self.p[l-q][q]

N,K = map(int, input().split())
O_o = Twelvefold_(1000, 10**9+7, build=False)
print(O_o.solve(N, K, aS=1, lt_1=1))