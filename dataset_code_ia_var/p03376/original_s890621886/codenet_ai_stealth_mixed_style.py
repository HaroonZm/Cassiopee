n,x,d=[int(z)for z in input().split()]
a=[0]*n
a[0]=int(input())
b=[0]*n
for v in range(n-1):
 u,vv=map(int,input().split())
 a[v+1],b[v+1]=u,vv
c=n*[1]
for i in range(n-1,0,-1):
 p=b[i]-1
 c[p]+=c[i]
 a[p]+=a[i]
l=[d for _ in range(n)]
l[0]=x
import collections

def Go(n,W,wg,vg,mg):
 V0=max(vg)
 mx=sum(z*min(V0,m)for z,m in zip(vg,mg))
 f=[W+1]*(mx+1)
 f[0]=0
 i=0
 while i<n:
  v=vg[i];w=wg[i];m=mg[i]
  take=min(V0,m)
  mg[i]-=take
  k=0
  while k<v:
   q=collections.deque()
   qappend=q.append
   qpopf=q.popleft
   qpopb=q.pop
   idx=0
   lim=(mx-k)//v+1
   while idx<lim:
    z=f[k+idx*v]-idx*w
    while q and z<=q[-1][1]:qpopb()
    qappend((idx,z))
    xx,yy=q[0]
    f[k+idx*v]=yy+idx*w
    if q and xx<=idx-take: qpopf()
    idx+=1
   k+=1
  i+=1
 ords=list(range(n))
 ords.sort(key=lambda h: wg[h]/vg[h])
 ls=[(vg[_],wg[_],mg[_]) for _ in ords]
 def hld():
  yield 0
  for z in range(mx+1):
   if f[z]>W:continue
   rst=W-f[z]
   total=z
   for vv,ww,mm in ls:
    zz=min(mm,rst//ww) if ww!=0 else mm
    total+=zz*vv
    rst-=zz*ww
   yield total
  return
 return max(hld())

print(Go(n,x,a,c,l))