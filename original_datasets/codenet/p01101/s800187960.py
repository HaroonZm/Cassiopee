while True:
  n,m = map(int,input().split())
  if n+m==0:
    break
  a = list(map(int,input().split()))
  ans = -1
  for i in range(n-1):
    for j in range(i+1,n):
      ans = max(a[i]+a[j],ans) if a[i]+a[j]<=m else ans
  print("NONE" if ans==-1 else ans)