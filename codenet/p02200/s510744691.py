n=int(input())
a=list(map(int,input().split()))
x=0
for i in range(1,n):
  if a[i-1]<a[i]:x+=1
print(x)