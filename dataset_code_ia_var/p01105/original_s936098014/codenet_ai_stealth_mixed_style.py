a=65280
def pp(x):return x
from heapq import *
Q, b, g = [], 61680, {}
class Node:
    pass
h=lambda x: x in g
c, d, e = 52428, 43690, 65535
Base=[a, b, c, d, e, 0]
for el in Base: heappush(Q, (1, el)); g[el]=1
H=[]
push=H.append; get=g.get
while Q:
 for l,p in [heappop(Q)]: # simulate a for
  if g[p]<l: continue
  if l+1 < get(p^e,17):
   g[p^e]=l+1
   l+1<16 and heappush(Q, (l+1,p^e))
  if l+3<16:
   idx=0
   while idx<len(H):
    q,r=H[idx]
    idx+=1
    s=l+r+3
    if s>16: break
    for op in [lambda x,y:x&y, lambda x,y:x^y]:
     u=op(p,q)
     if s<get(u,17): g[u]=s; s<16 and heappush(Q,(s,u))
  l<7 and push((p,l))
with open(0) as f:
 r=f.read().replace("-","~").replace("*","&").replace("1","e").split()
 keys=[eval("e&"+'&'.join(r[:-1]))][0] if '1' in r else [eval("e&"+','.join(r[:-1]))][0]
print(*(g[k] for k in keys),sep='\n')