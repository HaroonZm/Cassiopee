m,n=map(int,input().split())
a=list(map(int,input().split()))
if m==2:
  x=y=0
  for i in range(n):
    b=i%2+1
    c=(i+1)%2+1
    if a[i]!=b:x+=1
    if a[i]!=c:y+=1
  print(min(x,y))
  exit()
x=0
for i in range(1,n):
  if a[i-1]==a[i]:a[i]=-1;x+=1
print(x)