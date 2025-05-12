n=int(input())
a=list(map(int,input().split()))
p=[]
for j in range(30):
  p.append(pow(2,j))
t=0
for i in range(n):
  t=t^a[i]
for i in range(n):
  ans=0
  for j in range(30):
    ans=ans+p[j]*(((a[i]^t)//p[j])%2)
  print(ans,end=" ")