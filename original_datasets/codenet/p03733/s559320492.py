N,T=map(int,input().split())
l=list(map(int,input().split()))
ans=0
for i in range(N-1):
    if l[i+1]-l[i]<T:
        ans+=l[i+1]-l[i]
    else:
        ans+=T
print(ans+T)