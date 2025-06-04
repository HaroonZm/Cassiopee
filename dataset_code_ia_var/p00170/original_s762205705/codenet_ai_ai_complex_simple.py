from functools import reduce
from operator import mul

while True:
    try:
        n = int(input())
    except:
        continue
    if n==0: break

    D=[input().split() for _ in range(n)]
    F,W,S=map(list,zip(*((f,int(w),int(s)) for f,w,s in D)))

    perm=lambda xs: (lambda f: f(f,xs,[]))(
    lambda f,unpicked,picked: 
        [picked] if not unpicked else
        sum([f(f,unpicked[:i]+unpicked[i+1:],picked+[x]) for i,x in enumerate(unpicked)],[])
    )

    def isvalid(order):
        return all(S[i] >= (lambda z: reduce(lambda a,b:a+b, (W[o] for o in order[:k]),0))(k)
                for k,i in enumerate(order))
    orders=[o for o in perm(list(range(n))) if isvalid(o)]

    def calcval(order):
        return sum((i+1)*W[order[n-1-i]] for i in range(n))
    
    winner = min(orders, key=calcval)
    for i in winner:print(F[i])