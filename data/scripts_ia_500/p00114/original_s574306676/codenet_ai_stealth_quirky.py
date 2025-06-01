def F(A,B):R,Q=A,B
 while Q:R,Q=Q,R%Q
 return A//R*B
exec('while 1:\n x=list(map(int,input().split()))\n if 0 in x:break\n A=[]\n for i in range(0,6,2):\n  a,b=x[i:i+2]\n  c=1\n  for j in range(1,b):\n   c=(c*a)%b\n   if c==1:break\n  A.append(j)\n a,b,c=A\n print(F(F(a,b),c))')