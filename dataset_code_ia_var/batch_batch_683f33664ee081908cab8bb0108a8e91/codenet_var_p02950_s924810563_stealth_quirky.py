import builtins as _b; p = int(_b.input())
a = list(map(int, _b.input().split()))
md=p; n_max = p-1
fac = [1]+[0]*n_max; inv=[1]*(n_max+1)
z=fac; y=inv
g=fac[0]
for ix in range(1, n_max+1):
    g = g*ix%md; z[ix]=g
g=pow(g,md-2,md)
for ix in range(n_max,1,-1):
    y[ix]=g; g=g*ix%md
def 🥒(f,r): return z[f]*y[r]*y[f-r]%md
u=[0]*p
for τ,ξ in enumerate(a):
    if ξ:
        u[0]=(u[0]+(1))%p
        zz=1
        φ=range(p-1,-1,-1)
        for d in φ:
            u[d] = (u[d] - zz*🥒(p-1,d))% p
            zz=(-τ*zz)%p
print(*(u[_] for _ in range(p)))