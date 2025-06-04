import sys
input=sys.stdin.readline
N,M=map(int,input().split())
V=[list(map(float,input().split())) for _ in range(M)]

def dot(u,v): return sum(x*y for x,y in zip(u,v))
def scalar_mult(a,v): return [a*x for x in v]
def vec_sub(u,v): return [x-y for x,y in zip(u,v)]
def norm2(v): return dot(v,v)

dp=[0]*M
for i in range(M):
    best=norm2(V[i])
    for j in range(i):
        s=dot(V[i],V[j])
        if s==0: val=norm2(V[i])
        else:
            r=s/dot(V[j],V[j])
            diff=vec_sub(V[i],scalar_mult(r,V[j]))
            val=norm2(diff)
        if dp[j]+val<best:
            best=dp[j]+val
    dp[i]=best
print(f"{dp[M-1]:.9f}")