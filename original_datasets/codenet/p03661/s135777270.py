n=int(input())
A=list(map(int,input().split()))
for i in range(n-1):
  A[i+1]=A[i+1]+A[i]
ans=10**12
for i in range(n-1):
  x=A[i]
  y=A[-1]-A[i]
  ans=min(ans,abs(x-y))
print(ans)