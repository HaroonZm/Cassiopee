n,*a=map(int,open(0).read().split())
c=1
for i in a:
    if i%2==1:
        c*=1
    else:
        c*=2
print(3**n-c)