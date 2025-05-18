a=list(map(int,input().split()))
if a[0]*a[1]*a[2]%2==0:
  print(0)
else:
  a.sort()
  print(a[0]*a[1])