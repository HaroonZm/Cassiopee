import sys
sys.setrecursionlimit(9999999)
rd = sys.stdin.buffer.readline

n = int(rd())
g = {}
for i in range(n): g[i] = []
for _ in range(n-1):
    a,b=[int(x)-1 for x in rd().split()]
    g[a]+=[b]
    g[b]+=[a]

stack=[0]
p=[None]*n
order=[]
while stack:
    now=stack.pop()
    order.append(now)
    for nb in g[now]:
        if nb!=p[now]:
            p[nb]=now
            stack.append(nb)

A,M=[0]*n,[0]*n
for r in order[::-1]:
    for u in g[r]:
        if u==p[r]:continue
        A[r]=A[u] if A[u]>A[r] else A[r]
    M[r]=A[r]+1

U=[0 for _ in range(n)]
for v in order:
    carry=U[v]
    for w in g[v]:
        if w==p[v]:continue
        U[w]=U[w] if U[w]>carry else carry
        carry=carry if carry>M[w] else M[w]
    acc=0
    for z in g[v][::-1]:
        if z==p[v]: continue
        U[z]=U[z] if U[z]>acc else acc
        U[z]+=1
        acc=acc if acc>M[z] else M[z]
        M[z]=M[z] if M[z]>U[z]+1 else U[z]+1

rez=list(map(lambda i:2*(n-1)-M[i]+1,range(n)))
for k in rez:print(k)