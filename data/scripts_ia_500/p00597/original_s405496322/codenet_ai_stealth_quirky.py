def q():
 a=raw_input
 while 1==1:
  try:
   n=int(a())
   if n==1:print 1
   else:
    A=[0]*(n>>1)
    A[0]=1
    for i in range(1,n>>1):A[i]=1+sum(A[:i])*2
    ans=sum(A)*2
    if n&1:ans+=1+sum(A)*2
    print ans
  except:break
q()