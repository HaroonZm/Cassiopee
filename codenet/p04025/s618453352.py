n=int(input())
a=list(map(int,input().split()))
amax, amin = max(a), min(a)
ans=5*10**6
for i in range(min(a), max(a)+1):
  tmp=0
  for j in range(n):
    tmp+=(a[j]-i)**2
  ans=min(tmp,ans)
print(ans)