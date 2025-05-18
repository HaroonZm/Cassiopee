n,k = map(int, input().split())
mod=[0]*k
for a in range(1,n+1):
    mod[a%k]+=1
ans=0
for a in range(k):
    b=(k-a)%k
    c=(k-a)%k
    if (b+c) % k == 0:
        ans+=mod[a]*mod[b]*mod[c]
print(ans)