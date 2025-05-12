n,l=map(int,input().split())
a=list(map(int,input().split()))
failflag=1
for i in range(n-1):
  if a[i]+a[i+1]>=l:
    failflag=0
    k=i
    break
if failflag==1:
  print('Impossible')
else:
  print('Possible')
  for i in range(1,k+1):
    print(i)
  for i in range(n-1-k):
    print(n-1-i)