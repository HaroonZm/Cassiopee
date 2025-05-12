N=int(input())
A=[int(x) for x in input().rstrip().split()]
ave=sum(A)//len(A)
ans=0

if N/2<(sum(A)%len(A)):
  ave+=1

for i in A:
  ans+=(i-ave)**2
print(ans)