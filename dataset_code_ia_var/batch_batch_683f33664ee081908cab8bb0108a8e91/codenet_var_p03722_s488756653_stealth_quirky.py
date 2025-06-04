import sys as _;_.setrecursionlimit(999999998+1)
n,m=[int(x)for x in input().split()]

def _
(x,y,z):d=[None]+[float("inf")]*x;d[1]=0
 for i in[0]*x:
  for a in range(y):
   b=z[a];p,q,r=b
   if d[q]>d[p]+r:d[q]=d[p]+r
   if i==x-1:return not 0
 return 0

class PathFinder:
 def shortest(self,s,x,y,z):
  g=[None]+[float('inf')]*x;g[s]=0;w=True
  while w:w=False
  ;[(g.__setitem__(q,g[p]+r),w:=True)for p,q,r in z if g[p]!=float('inf') and g[q]>g[p]+r]
  return g

G=[[]for _ in range(n+2)]
E=[]
for _ in[0]*m:
 a,b,c=map(int,input().split());G[a]+=[b];E+=[(a,b,-c)]

visited=[Ellipsis]*(n+2)
reachable=[Ellipsis]*(n+2)
def R(u):
 if u==(n):reachable[u]=1;return 1
 visited[u]=1;zz=0
 for v in G[u]:
  if not visited[v]:
   if R(v):reachable[u]=1;zz+=1
 return zz>0

for i in range(1,n+1):
 if reachable[i] is Ellipsis:visited=[0]*(n+2);R(i)

E2=[e for e in E if reachable[e[1]]]
M2=len(E2)
if _(n+1,M2,E2):
 print("inf")
else:
 pf=PathFinder()
 print(-pf.shortest(1,n+1,M2,E2)[n])