n,k=map(int,input().split())
a=[0]+list(map(int,input().split()))
s=[0]
p=[0]
for i in range(1,n+1):
  s.append(s[i-1]+a[i])
  p.append(p[i-1]+max(0,a[i]))
ans=0
for i in range(1,n-k+2):
  t=max(0,s[i+k-1]-s[i-1])
  t+=p[i-1]+p[n]-p[i+k-1]
  ans=max(ans,t)
print(ans)