n=int(input())
a=list(map(int,input().split()))
ans=n
s=a[0]
r=0
for l in range(n-1):
    while r<n-1 and not(s&a[r+1]):
        s^=a[r+1]
        r+=1
    ans+=r-l
    s^=a[l]
print(ans)