def i1():
 return int(input())
def i2():
 return [int(i) for i in input().split()]
[k,q]=i2()
d=i2()
for i in range(q):
  [n,x,m]=i2()
  di=[]
  dz=[]
  for i in d:
    di.append(i%m)
    if i%m==0:
       dz.append(1)
    else:
       dz.append(0)
  x=((n-1)//k)*sum(di[:k])+x%m
  if (n-1)%k:
    x+=sum(di[:(n-1)%k])
  ans=n-1-x//m-((n-1)//k)*sum(dz[:k])
  if (n-1)%k:
   ans-=sum(dz[:(n-1)%k])
  print(ans)