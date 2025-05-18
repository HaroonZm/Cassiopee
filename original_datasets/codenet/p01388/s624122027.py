s=str(input())
a=0
k=s.count('K')
u=s.count('U')
p=s.count('P')
c=s.count('C')
while True:
    if k==0 or u==0 or p==0 or c==0:
        break
    else:
        a+=1; k-=1; u-=1; p-=1; c-=1
print(a)