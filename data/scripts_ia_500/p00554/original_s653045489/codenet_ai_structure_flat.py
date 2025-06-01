n,m=map(int,input().split())
point=[]
for _ in range(m):
    atari,hazure=map(int,input().split())
    point.append([atari,hazure])
point.sort(reverse=True)
ans=0
for i in range(m-1):
    if point[i][0]<n:
        ans+=n - point[i][0]
print(ans)