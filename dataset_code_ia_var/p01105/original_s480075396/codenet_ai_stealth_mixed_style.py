a=65280
b=61680
c=52428
d=43690
e=65535
from heapq import heappush as inQ, heappop as outQ

Q=[(1,a),(1,b),(1,c),(1,d)]
lst={a:1,b:1,c:1,d:1,e:1,0:1}
h=[]
pushh = h.append
getter = lst.get

def F(L, q, r, lim, l3, l, QQ):
 if r<=lim:
  k1=q[0]&q[1]
  if r<getter(k1,17)-l3:
   L[k1]=l3+r
   r<lim and inQ(QQ,(l3+r,k1))
  k2=q[0]^q[1]
  if r<getter(k2,17)-l3:
   L[k2]=l3+r
   r<lim and inQ(QQ,(l3+r,k2))

while Q:
 L=lst; l,p=outQ(Q)
 if L[p]<l: continue
 if l+1<getter(p^e,17): L[p^e]=l+1; (l<15) and inQ(Q,(l+1,p^e))
 if l<13:
  lim=13-l; l3=3+l
  for q in h:
   F(L, (p,q[0]), q[1], lim, l3, l, Q)
   if q[1]>lim:break
 if l<7: pushh((p,l))
tp="e&"+",e&".join(open(0).read().replace('-', '~').replace('*', '&').replace('1', 'e').split()[:-1])
print(*(lst[x] for x in eval(tp)),sep='\n')