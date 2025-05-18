n,*a=map(int,open(0).read().split())
c=1
for i in a:
  c*=(1 if i%2==1 else 2)
print(3**n-c)