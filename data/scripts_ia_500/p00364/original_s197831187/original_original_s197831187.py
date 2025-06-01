n,t=map(int,input().split())
ans=0
for i in range(n):
    x,h=map(int,input().split())
    ans=max(ans,h*t/x)
print(ans)