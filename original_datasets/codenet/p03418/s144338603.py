n,k = map(int,input().split())
ans = 0
for i in range(1,n+1):
  ans += max(i-k,0)*(n//i)+max(n%i-k+1,0)
print(ans if k!=0 else ans-n)