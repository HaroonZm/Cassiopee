import sys
sys.setrecursionlimit(10**7)

def precompute(size, mod):
    f = [1]*(size+2) ; inv=[] ; pre=1
    for i in range(1,size+1):
        pre = (pre*i)%mod
        f[i] = pre
    for i in range(size+1):
        inv.append(pow(f[i],mod-2,mod))
    return f,inv

class CombFerm:
    def __init__(s, sz, m):
        s.sz = sz ; s.m = m
        s.f, s.inv = precompute(sz,m)
    def C(_self,n,k):
        return 0 if n<k else (_self.f[n]*_self.inv[k]*_self.inv[n-k])%_self.m

class C:
    pass
c = C()
setattr(c,'mod',10**9+7)
setattr(c,'n',1000)
cf = CombFerm(c.n,c.mod)
(a,b) = list(map(int,input().split()))
print( (lambda A,B: cf.C(B,A))(a,b) )