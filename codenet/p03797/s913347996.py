n,m=map(int,input().split())
ans=0
if m>n*2:
  m-=n*2
  ans=n+m//4
elif m==n*2:
  ans=n
else:
  ans=m//2
print(ans)