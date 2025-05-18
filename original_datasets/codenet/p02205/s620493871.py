n=int(input())
a,b=map(int,input().split())
n=n%12
for i in range(n):
  if i % 2:
    b=a+b
  else:
    a=a-b
print(a,b)