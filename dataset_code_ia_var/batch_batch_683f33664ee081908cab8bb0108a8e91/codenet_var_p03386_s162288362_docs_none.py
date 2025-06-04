A,B,K=(int(i) for i in input().split())
a=B-A+1
if K>=a:
  for i in range(A,B+1):
    print(i)
else:
  L1=list(range(A,A+K))
  L2=list(range(B-K+1,B+1))
  S=list(set(L1+L2))
  S.sort()
  for i in S:
    print(i)