h,w=map(int,input().split())
d=[0]+[300]*w
for i in range(h):
  s=input()
  if i==0:
    a=s[0]
  for j in range(w):
    t=s[j]==a
    d[j]+=t^(d[j]%2==0)
    if j>0:
      d[j]=min(d[j],d[j-1]+t^(d[j-1]%2==0))
print((d[-2]+(a=="#")+1)//2)