from itertools import product
h,w,d=[int(x)for x in input().split()]
def odd_case(h,w):
 for row in range(h):
  s=""
  for col in range(w):
   if((row+col)&1)==1:
    s+="R"
   else:
    s+="G"
  print(s)
def even_case(h,w,d):
 A=[["A"]*(2*d)for _ in range(2*d)]
 for p in range(d*d):
  i=p//d
  j=p%d
  t=(d//2-1)%2
  if (i+j)%2==t:
   if abs(i-j)<=d//2-1<=i+j<=(d//2-1)*3:
    A[i][j]="R"
  elif j>0 and A[i][j-1]=="R":
   A[i][j]="R"
 for i,j in product(range(2*d),repeat=2):
  mod=lambda x: x%(2*d)
  if A[mod(i-d)][mod(j-d)]=="R":
   A[i][j]="R"
  elif A[mod(i-d//2)][mod(j-d//2)]=="R" or A[mod(i+d//2)][mod(j+d//2)]=="R":
   A[i][j]="G"
  elif A[mod(i-d)][j]=="R" or A[i][mod(j-d)]=="R":
   A[i][j]="B"
  elif A[i][j]=="A":
   A[i][j]="Y"
 B=[["A"]*w for _ in range(h)]
 for r in range(h):
  for s in range(w):
   B[r][s]=A[r%(2*d)][s%(2*d)]
  print("".join(B[r]))
if d&1: odd_case(h,w)
else: even_case(h,w,d)