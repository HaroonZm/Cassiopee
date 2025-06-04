a,b,c=map(int,input().split())
count=0
i=a
while i<=b:
  if c%i==0:
    count+=1
  i+=1
print(count)