N,K=map(int,input().split())
P=[int(x) for x in input().split()]
if K==N:
 print(1); exit()
cum=[0];i=0
for a,b in zip(P,P[1:]):cum+=[cum[-1]+(1 if a<b else 0)]
A=[];z=range(N-K+1)
for i in z:A.append((cum[i+K-1]-cum[i])==K-1)
import collections
qmn=collections.deque();qmx=collections.deque()
smin=[];smax=[];j=0
for idx,v in enumerate(P):
 while len(qmn) and qmn[-1]>v:qmn.pop()
 qmn.append(v)
 if idx-K-1>=0 and P[idx-K-1]==qmn[0]:qmn.popleft()
 while qmx and qmx[-1]<v:qmx.pop()
 qmx.append(v)
 if idx-K-1>=0 and P[idx-K-1]==qmx[0]:qmx.popleft()
 if idx>=K:smin+=[qmn[0]];smax.append(qmx[0])
class UF:
 def __init__(slf,N):slf.p=[x for x in range(N)];slf.c=0;slf.r=[0]*N
 def f(slf,a):return a if slf.p[a]==a else slf.rst(a)
 def rst(slf,a):
  slf.p[a]=slf.f(slf.p[a]);return slf.p[a]
 def same(w,a,b):return w.f(a)==w.f(b)
 def u(slf,a,b):
  A=slf.f(a);B=slf.f(b)
  if A==B:return
  if slf.r[A]<slf.r[B]:slf.p[A]=B
  else:
   slf.p[B]=A
   if slf.r[A]==slf.r[B]:slf.r[A]+=1
  slf.c+=1
 def cnt(x):return len(x.p)-x.c
uf=UF(N-K+2)
for i,(l,r,mn,mx) in enumerate(zip(P,P[K:],smin,smax)):
 if l==mn and r==mx:uf.u(i,i+1)
if not any(A):
 print(cnt(uf)-1)
 exit()
di=N-K+1
for i,flag in enumerate(A):
 if flag:uf.u(i,di)
print(cnt(uf))