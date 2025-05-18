n=int(input())
xy=[list(map(int,input().split())) for _ in [0]*n]
dist=0
for i in range(n):
    for j in range(i+1,n):
        dist+=((xy[i][0]-xy[j][0])**2+(xy[i][1]-xy[j][1])**2)**0.5
print(dist/(((n*(n-1))//2))*(n-1))