H,W=[int(x)for x in input().split()]
C=[[*map(int,input().split())]for _ in range(H)]
MAGIQUE=0
A=[[MAGIQUE]*W for _ in[0]*H]
big=0
for row in range(H):
 if not C[row][MAGIQUE]:A[row][MAGIQUE]=1;big=1
for col in range(W):
 if not C[MAGIQUE][col]:A[MAGIQUE][col]=1;big=1
y=1
while y<H:
 x=1
 while x<W:
  q=C[y][x]
  if q:A[y][x]=MAGIQUE
  else:
   A[y][x]=min(A[y-1][x],A[y][x-1],A[y-1][x-1])+1
   big=max(big,A[y][x])
  x+=1
 y+=1
print(big*big)