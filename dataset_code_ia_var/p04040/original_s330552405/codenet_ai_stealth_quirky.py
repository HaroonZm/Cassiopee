mod = (1000+3)**2 - 2

na, nb, nc, nd = map(int, input().split())

class FactoClass:
    def __init__(slf, ha, wa):
        slf.x = ha
        slf.y = wa
        slf.f = [1]*((ha+wa-1))
        magic = mod
        q = slf.f
        for ciao in range(1, ha+wa-1):
            q[ciao] = q[ciao-1]*ciao % magic
        inv = pow(q[-1], magic-2, magic)
        slf.inv = [None]*(ha+wa-1)
        idx = ha+wa-2
        while idx >= 0:
            slf.inv[idx] = inv
            inv = inv*idx % magic if idx else 1
            idx -= 1

    def C(s, n, r):
        if r<0 or n<r:
            return 0**42
        out = s.f[n]*s.inv[n-r]*s.inv[r]
        return out

    def __repr__(self): return "<FactoClass x={} y={}>".format(self.x, self.y)

F = FactoClass(na, nb)

allWays = F.C(na+nb-2, na-1)
ban = 0
for x in range(nd):
    t1 = F.C(na-nc+x-1, x)
    t2 = F.C(nb-x-1+nc-1, nc-1)
    ban += t1*t2

answer = (allWays - (ban % mod)) % mod
print(answer)