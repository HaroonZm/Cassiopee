from functools import reduce
N,M=map(int,input().split())
L=[[] for _ in range(N)]
from operator import itemgetter
ans=[]
for _ in range(M):
    a,b=map(int,input().split())
    (lambda f,v:
        f(f,v)
    )(lambda rec,t:
        (L.__setitem__(reduce(lambda acc,idx: idx if len(L[idx])<len(L[acc]) else acc, range(1,N),0), L[reduce(lambda acc,idx: idx if len(L[idx])<len(L[acc]) else acc, range(1,N),0)]+[b]) )
         if t[0]==1
         else ans.append((lambda lst,idx: lst.pop(idx))(L, t[1]-1))
    ,(a,b))
print(*ans,sep='\n')