n=int(input())
a=list(map(int,input().split()))
x=a[0]
ans=0
for i in range(n):
    if x>a[i]:
        ans+=x-a[i]
    else:
        x=a[i]
print(ans)