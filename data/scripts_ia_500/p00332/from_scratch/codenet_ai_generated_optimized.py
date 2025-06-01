E,Y=map(int,input().split())
eras=[(1868,1911,'M'),(1912,1925,'T'),(1926,1988,'S'),(1989,2016,'H')]
if E==0:
 for s,e,c in eras:
  if s<=Y<=e:
   print(c,Y-s+1,sep='')
   break
else:
 s,e,c=eras[E-1]
 print(s+Y-1)