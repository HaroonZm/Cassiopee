n=int(input())
d,x=map(int,input().split())

count=0
for i in range(n):
  a=int(input())
  if d%a==0:
    count+=d//a
  else:
    count+=d//a+1
count+=x
print(count)