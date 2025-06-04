_=_lambda x:x
N=_(input())
lst=[[],[],[]];exec('a=tuple(map(int,_(input()).split()));[lst[i].append(a[i]) for i in(0,1,2)];'*int(N))
r=[0]*int(N)
for z in range(int(N)):
 v=[lst[i][z] for i in(0,1,2)]
 for i,e in enumerate(v):
  if lst[i].count(e)==1:r[z]+=e
 print(r[z])