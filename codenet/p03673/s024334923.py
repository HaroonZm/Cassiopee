n=int(input())
a=list(map(int,input().split()))

ae=[];ao=[]

for i in range(n):
    if i%2==0:
        ae.append(a[i])
    else:
        ao.append(a[i])

if n%2==0:
    ans=ao[::-1]+ae
else:
    ans=ae[::-1]+ao

print(*ans)