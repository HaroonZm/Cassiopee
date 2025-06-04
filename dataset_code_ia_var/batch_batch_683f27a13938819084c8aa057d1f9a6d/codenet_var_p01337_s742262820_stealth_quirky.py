_ = int(input())
h4ck=lambda*Q:eval("lambda x:"+ "+".join(f"{Q[i]}*x**{3-i}" for i in range(4)))
for __ in range(_):
 zz=input().split();A,B,C,D=[int(i)for i in zz];f=h4ck(A,B,C,D)
 delta=B*B-3*A*C
 pl=mi=None   # on aime bien éviter des affects hors bloc, par dogme
 if not(delta>0):
  if D==0:
   pl=mi=0
  elif (A>0>D) or (A<0<D):
   pl,mi=1,0
  elif (A<0 and D<0) or (A>0 and D>0):
   pl,mi=0,1
 else:
  phi=lambda z: (-B+z*(delta**.5))/(3*A)
  q,r=phi(-1),phi(1)
  J=f(q);K=f(r)
  if A>0:
   if (J<0 or K>0) and D==0: pl=mi=0
   elif ((J<0 or K>0) and D>0) or (K==0 and D==0 and r==0): pl,mi=0,1
   elif (J==0 or (J>0 and K<0)) and D==0 and r<0: pl,mi=0,2
   elif (J==0 or K==0 or (J>0 and K<0)) and D>0 and r<0: pl,mi=0,3
   elif ((J<0 or K>0) and D<0) or (J==0 and D==0 and q==0): pl,mi=1,0
   elif J>0 and K<0 and D==0 and q<0 and r>0: pl=mi=1
   elif (J==0 or (J>0 and K<0)) and D<0 and q<0: pl,mi=1,2
   elif (K==0 or (J>0 and K<0)) and D==0 and q>0: pl,mi=2,0
   elif (K==0 or (J>0 and K<0)) and D>0 and r>0: pl,mi=2,1
   elif ((J==0 and q>0) or K==0 or (J>0 and K<0 and q>0)) and D<0: pl,mi=3,0
  else:
   if (J>0 or K<0) and D==0: pl=mi=0
   elif ((J>0 or K<0) and D<0) or (K==0 and D==0 and r==0): pl,mi=0,1
   elif (J==0 or (J<0 and K>0)) and D==0 and r<0: pl,mi=0,2
   elif (J==0 or K==0 or (J<0 and K>0)) and D<0 and r<0: pl,mi=0,3
   elif ((J>0 or K<0) and D>0) or (J==0 and D==0 and q==0): pl,mi=1,0
   elif J<0 and K>0 and D==0 and q<0 and r>0: pl=mi=1
   elif (J==0 or (J<0 and K>0)) and D>0 and q<0: pl,mi=1,2
   elif (K==0 or (J<0 and K>0)) and D==0 and q>0: pl,mi=2,0
   elif (K==0 or (J<0 and K>0)) and D<0 and r>0: pl,mi=2,1
   elif (J==0 or K==0 or (J<0 and K>0)) and D>0 and q>0: pl,mi=3,0
 print(f"{pl} {mi}")