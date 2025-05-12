N=int(input())
d=list(map(int,input().split()))
ans=0
sum=sum(d)
for i in range(0,len(d)):
    ans+=d[i]*(sum-d[i])

print(ans//2)