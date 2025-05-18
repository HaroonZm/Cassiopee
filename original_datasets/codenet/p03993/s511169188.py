n=int(input())
ans=0
a=list(map(int,input().split()))
for i in range(n):
    if a[a[i]-1]==i+1:
        ans+=1
print(ans//2)