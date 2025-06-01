def s():
 import sys,functools,operator as o,itertools as it
 R=map(str.strip,sys.stdin)
 f=lambda x,y: (int(x[0])+int(y[0]),int(x[1])+int(y[1]))
 while 1:
  e=next(R)
  if e=='0 0':break
  w,h=map(int,e.split())
  M=functools.reduce(lambda M,_:M+[[[1,0]*2 for __ in range(h)]],[None]*w,[])
  for i,j in it.product(range(1,w),range(1,h)):
   a,b,c,d=M[i-1][j][0],M[i-1][j][1],M[i][j-1][2],M[i][j-1][3]
   M[i][j]=[d,a+b,b,c+d]
  r=sum(M[w-2][h-1][:2])+sum(M[w-1][h-2][2:])
  print(r%10**5)
if __name__=='__main__':s()