for e in iter(input,'0 0'):
 w,h=map(int,e.split())
 M=[[[1,0]*2 for _ in[0]*h]for _ in[0]*w]
 for i in range(1,w):
  for j in range(1,h):
   a,b=M[i-1][j][:2]
   c,d=M[i][j-1][2:]
   M[i][j]=[d,a+b,b,c+d]
 print((sum(M[w-2][h-1][:2])+sum(M[w-1][h-2][2:]))%10**5)