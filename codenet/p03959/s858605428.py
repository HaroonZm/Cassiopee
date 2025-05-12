mod=10**9+7
n=int(input())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
a=[-1]*n
b=[-1]*n
c=[-1]*n
s=arr1[0]
a[0]=s
for i in range(n):
  if arr1[i]==1:
    a[i]=1
  else:
    if s!=arr1[i]:
      a[i]=arr1[i]
      s=arr1[i]
s=arr2[-1]
b[-1]=s
for i in range(1,n+1):
  if arr2[-i]==1:
    b[-i]=1
  else:
    if s!=arr2[-i]:
      b[-i]=arr2[-i]
      s=arr2[-i]
flag=False
for i in range(n):
  if a[i]==-1 and b[i]==-1:
    c[i]=-1
  elif a[i]==-1:
    if arr1[i]>=b[i]:
      c[i]=b[i]
    else:
      flag=True
  elif b[i]==-1:
    if arr2[i]>=a[i]:
      c[i]=a[i]
    else:
      flag=True
  else:
    if a[i]==b[i]:
      c[i]=a[i]
    else:
      flag=True
if flag==True:
  print(0)
else:
  l=0
  r=0
  ans=1
  cnt=0
  for i in range(n):
    if c[i]==-1:
      if cnt==0:
        l=c[i-1]
      cnt+=1
    else:
      if cnt!=0:
        r=c[i]
        for _ in range(cnt):
          ans=(ans*min(l,r))%mod
        cnt=0
  print(ans)