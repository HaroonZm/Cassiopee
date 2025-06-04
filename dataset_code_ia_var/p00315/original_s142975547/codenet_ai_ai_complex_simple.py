from functools import reduce
from operator import eq, xor

cyc = lambda N, i: (lambda x: (x+N)%N)(N - i - 1)
quad = lambda N, G, *idx: all(map(lambda rc: eq(*rc), zip(*(G[i][j] for i, j in idx))))
box = lambda N, G, i, j: reduce(lambda acc, _:(acc and quad(N, G,
        (i, j),
        (i, cyc(N, j)),
        (cyc(N, i), j),
        (cyc(N, i), cyc(N, j)))
    ), range(1), True)
def countfrags(N, G):  
    return sum(map(lambda x: not box(N, G, *x), ((i, j) for i in range(N//2) for j in range(N//2))))

C,N=map(int,input().split())
G=[[*map(int,list(input()))]for _ in range(N)]

q=sum([(countfrags(N,G)==0)])

for _ in range(C-1):
    k=int(input())
    S=set()
    for __ in range(k):
        r,c=map(int,input().split())
        r-=1;c-=1;S.add((r,c))
    mods=lambda t:(box(N,G,*t),t)
    pre={t:box(N,G,*t) for t in S}
    for (r,c) in S:
        G[r][c]^=1
    post={t:box(N,G,*t) for t in S}
    vchg=sum([(not pre[t]) and post[t] for t in S])-sum([pre[t] and (not post[t]) for t in S])
    frag=countfrags(N,G)
    q+=(frag==0)
print(q)