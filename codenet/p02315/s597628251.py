N,W=map(int,input().split())
C=[0]*-~W
for _ in[0]*N:
 v,w=map(int,input().split())
 for i in range(W,w-1,-1):
  t=v+C[i-w]
  if t>C[i]:C[i]=t
print(C[W])