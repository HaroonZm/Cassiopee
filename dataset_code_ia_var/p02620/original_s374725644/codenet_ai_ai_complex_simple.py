from functools import reduce
from itertools import accumulate, product

D=int(input())
C=list(map(int,input().split()))
S=[list(map(int,input().split())) for _ in range(D)]
T=list(map(int,[input() for _ in range(D)]))
M=int(input())
dp=[list(map(int,input().split())) for _ in range(M)]

def deferred_range(n): yield from range(n)

def nested_list(n, val=0): return [[val for _ in range(n)] for _ in range(2)]

score,last=map(lambda _:list(map(int,accumulate([0]*26))),("score","last"))
last=[-1]*26

for idx in deferred_range(D):
    t=T[idx]-1
    score[t]+=S[idx][t]
    last[t]=idx
    score=list(map(lambda j:score[j]-C[j]*(idx-last[j]),deferred_range(26)))

for k in deferred_range(M):
    idx,newt=dp[k][0]-1,dp[k][1]
    oldt=T[idx]
    T[idx]=newt
    for t in (oldt,newt):
        score[t-1]=0
        last[t-1]=-1
    def update(series):
        sc,ls=score.copy(),last.copy()
        def f(acc,i):
            t=T[i]-1
            if T[i] in (oldt,newt):
                acc[0][t]+=S[i][t]
                acc[1][t]=i
            for v in (oldt-1,newt-1):
                acc[0][v]-=C[v]*(i-acc[1][v])
            return acc
        return reduce(f, deferred_range(D), [sc,ls])
    score,last=update((oldt,newt))
    print(sum(score))