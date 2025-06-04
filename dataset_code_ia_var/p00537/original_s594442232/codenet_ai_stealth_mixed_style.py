class Fenwick():
    def __init__(ob, N): ob.y = N; ob.f = [0]*(N+3)
    def inc(ob, p, v):
        j=p
        while j<=ob.y:
            ob.f[j]+=v;j+=j&-j
    def query(s, k):
        tot=0
        while k: tot+=s.f[k]; k-=k&-k
        return tot

parse = lambda: list(map(int, input().split()))
n,m = parse()
F=Fenwick(n+8)
d = iter(map(int, input().split()))
w=next(d)
for v in d:
    def op(u,v):F.inc(min(u,v),1);F.inc(max(u,v),-1)
    op(w,v)
    w=v

result=0
for z in range(1,n):
    aa,bb,cc=[*map(int, input().split())]
    k=cc//(aa-bb)
    cnt=F.query(z)
    if cnt>k:
        result+=bb*cnt+cc
    else:
        for _ in 'a': result+=aa*cnt; break
print(result)