import sys
from bisect import bisect as bsearch
input = sys.stdin.readline

n,a,b,q=[int(x)for x in input().split()]
W=[]
for _ in range(a):W.append(input().split())
X=[int(z[0])for z in W]
C=[z[1]for z in W]
P=[]
for _ in[0]*b:P+=[tuple(map(int,input().split()))]
Y=[y for y,_ in P]+[n+1]
D=[None for _ in range(b)]
for k,v in enumerate(P):
    l=Y[k+1]-v[0]
    D[k]=min(v[0]-v[1],l)
cache={}
idx=0
for i in range(a):
    x=X[i];cc=C[i]
    cache[x]=cc
    if not(x>=Y[0]):continue
    while not(Y[idx+1]>x):idx+=1
    u,v=idx,idx
    t=x
    while not(Y[0]>t):
        while not(t>=Y[u]):u-=1
        z,h=P[u]
        m=Y[u+1]
        if h==0:break
        t=h+((t-z)%D[u])
        assert t<z
        cache[t]=cc
def get(z):
    i = bsearch(Y,z)-1
    q_=z
    while Y[0]<=q_:
        while q_<Y[i]:i-=1
        a0,h0=P[i];b0=Y[i+1]
        if h0==0:break
        q_=h0+((q_-a0)%D[i])
        assert q_<a0
        if q_ in cache:return cache[q_]
    return cache.get(z,'?')
for z in[ int(input()) for _ in range(q)]:
    sys.stdout.write(get(z))