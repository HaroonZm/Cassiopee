A,B,N=map(int,input().split())
ans=10**15
for x in range(1,N+1):
 for y in range(1,N+1):
  num=A*y-B*x
  den=y
  c1=num//den
  candidates=[c1,c1+1]
  for c in candidates:
   if c>=1:
    diff=abs(A - c*x)
    if diff<ans:
     ans=diff
print(ans)