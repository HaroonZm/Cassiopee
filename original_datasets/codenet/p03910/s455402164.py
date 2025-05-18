n=int(input())
s=0
for i in range(n):
  s+=i+1
  if s>=n:
    k=i+1
    break
if s==n:
  for i in range(k):
    print(i+1)
else:
  if n==2:
    print(2)
  else:
    for i in range(k):
      if s-i-1!=n:
        print(i+1)