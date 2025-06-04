from sys import stdin
__import__("functools")
H,W,K=map(int,stdin.readline().split())
R=[*map(list,[stdin.readline().strip()for _ in range(H)])]
Y=X=-99
for e,l in enumerate(R):
 for t,f in enumerate(l):
  if f=="S":Y,X=e,t
M=999999
q=[(1,Y,X)]
while q:
 Q=[]
 for z,y,x in q:
  M=min(M,y,x,H-y-1,W-x-1)
  if z>K:continue
  for d in[(-1,0),(1,0),(0,-1),(0,1)]:
   a,b=y+d[0],x+d[1]
   if(a>=0)*(b>=0)*(a<H)*(b<W)*(R[a][b]=="."):
    R[a][b]='#'
    Q.append((z+1,a,b))
 q=Q
print(1-(M//K)*-1)