from sys import stdin as S
Y=lambda:int(S.readline())
M=lambda:int(S.readline())
n=Y()
f=[[*map(int,S.readline().split())]for _ in range(n)]
p=[[*map(int,S.readline().split())]for _ in range(n)]
res=-999999999
for h in range(1,1<<10):
 t=0
 z=[0]*n
 for d,e in enumerate(f):
  for g,j in enumerate(e):
   z[d]+=((h>>g)&1)&j
 for aa,bb in enumerate(z):
  t+=p[aa][bb]
 if t>res:res=t
print(res)