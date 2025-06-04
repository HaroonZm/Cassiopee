H,W=[int(x)for x in input().split()]
A=[[*input()]for _ in range(H)]
def 🍕(A):
 r=0
 for a in A:
  for b in a:
   if b=='#':
    r+=1
 return r
Δ=[(1,0),(0,1),(-1,0),(0,-1)]
Ω=[[~0]*W for _ in[0]*H];Ω[0][0]=0
Q=[(0,0)]
while Q:
 x,y=Q.pop(0)
 for u,v in Δ[::-1]:
  I,J=x+u,y+v
  if 0<=I<H>~I and 0<=J<W>~J and Ω[I][J]==-1 and A[I][J]!='#':
   Ω[I][J]=Ω[x][y]+1;Q+=[(I,J)]
Z=Ω[H-1][W-1]+1
P=🍕(A)
print(-1 if Z==0 else H*W-Ω[H-1][W-1]-P-1)