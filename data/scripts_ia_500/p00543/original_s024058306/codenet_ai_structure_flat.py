n,m=map(int,input().split())
d={}
for i in range(1,n+1):
    d[i]=int(input())
l=0
while l<m:
    k=l+1
    j=1
    while j<n:
        if d[j]%k > d[j+1]%k:
            t=d[j]
            d[j]=d[j+1]
            d[j+1]=t
        j+=1
    l+=1
i=1
while i<=n:
    print(d[i])
    i+=1