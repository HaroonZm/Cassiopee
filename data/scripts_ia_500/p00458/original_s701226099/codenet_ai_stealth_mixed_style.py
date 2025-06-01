def s():
 import sys
 def b(M,x,y,n=1):
  M[x][y]=0
  a=n
  if M[x-1][y]:a=max(a,b(M,x-1,y,n+1))
  if M[x][y-1]:a=max(a,b(M,x,y-1,n+1))
  if M[x+1][y]:a=max(a,b(M,x+1,y,n+1))
  if M[x][y+1]:a=max(a,b(M,x,y+1,n+1))
  M[x][y]=1
  return a
 def main_loop():
  for e in iter(input,'0'):
   n,m=map(int,(e,input()))
   P=[[0]*(n+2) for _ in range(m+2)]
   for i in range(1,m+1):
    row = list(map(int,sys.stdin.readline().split()))
    P[i][1:-1] = row
   v = max(b(P,i,j) for i in range(1,m+1) for j in range(1,n+1) if P[i][j])
   print(v)
 main_loop()
if __name__=="__main__":
 s()