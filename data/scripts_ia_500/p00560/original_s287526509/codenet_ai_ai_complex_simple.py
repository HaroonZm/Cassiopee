from heapq import heapify, heappop, heappush
from functools import reduce
N,M,K=map(int,input().split())
A,B,C=map(int,input().split())
T=int(input())
S=list(map(lambda x:int(x)-1, [input() for _ in range(M)]))

def f(rt,rn):
    return (lambda p,q:(p*p==p**2 and q*q==q**2) and (p if p<q else q))((rt//A),(rn-1))

ans=reduce(lambda acc,i: acc+(lambda s0,s1: (lambda val: val[2]+val[3])(*((lambda rt,rn,k,k0: (
    k+1,
    rt-(k+1)*C,rn-(k+1),
    [k0:=f(rt-(k+1)*C,rn-(k+1))][0],
    k0 if k0>=0 else 0
    ))(T-B*s0,s1-s0,f(T-B*s0,s1-s0)))) if B*S[i]<=T else (0,0,0,0), S[i],S[i+1])),0,range(M-1))
if B*S[-1]<=T:
    ans+=1

que=list(filter(None, map(lambda i: (lambda rt,rn,k: ((-k,rt,rn) if k>=0 else None))(
    T-B*S[i], S[i+1]-S[i], f(T-B*S[i],S[i+1]-S[i])) if B*S[i]<=T else None, range(M-1))))
heapify(que)

def step(ans, que):
    if not que: return ans, que
    k,rt,rn=heappop(que)
    k= -k
    rt-= (k+1)*C; rn-=k+1
    ans+=k+1
    k0=f(rt,rn)
    if k0>=0:
        heappush(que, (-k0, rt, rn))
    return ans, que

for _ in range(K-M):
    ans, que=step(ans, que)
print(ans-1)