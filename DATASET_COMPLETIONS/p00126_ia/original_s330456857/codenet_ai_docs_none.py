R=range(9)
def f1(M):
  global F
  for y in R:
    A=M[y]
    for x in R:
      if A.count(A[x])>=2: F[y][x]="*"
def f2(M):
  global F
  for x in R:
    A=[M[y][x] for y in R]
    for y in R:
      if A.count(A[y])>=2: F[y][x]="*"
def f3(M):
  global F
  for i in R:
    x=i%3*3
    y=i//3*3
    A=M[y][x:x+3]+M[y+1][x:x+3]+M[y+2][x:x+3]
    for j in R:
      if A.count(A[j])>=2: F[y+j//3][x+j%3]="*"
n=input()
while n:
  M=[]
  F=[[" " for _ in range(9)] for _ in range(9)]
  M=[map(int,raw_input().split()) for _ in range(9)]
  f1(M)
  f2(M)
  f3(M)
  for i in R:
    s=zip(F[i],map(str,M[i]))
    print "".join([a+b for a,b in s])
  if n>1: print
  n-=1