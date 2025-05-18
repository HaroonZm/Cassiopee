N=int(input())
p=list(map(int,input().split()))

ans=0
for i in range(N):
    if p[i]==i+1:
        if i==N-1:
            c=p[i]
            p[i]=p[i-1]
            p[i-1]=c
        else:
            c=p[i]
            p[i]=p[i+1]
            p[i+1]=c
        ans+=1

print(ans)