n,h,w=map(int,input().split())
ans=chk=0
for i in range(n):
    y,x=map(int,input().split())
    if h<=y and w<=x: ans+=1
print(ans)