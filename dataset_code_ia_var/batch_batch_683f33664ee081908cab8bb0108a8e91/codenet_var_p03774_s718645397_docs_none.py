import math

n,m=[int(i) for i in input().split()]
ab=[]
cd=[]
for _ in range(n):
    x,y=[int(i) for i in input().split()]
    ab.append([x,y])
for _ in range(m):
    x,y=[int(i) for i in input().split()]
    cd.append([x,y])
for i in range(n):
    dist=10**9
    point=0
    for j in range(m):
        temp=abs(ab[i][0]-cd[j][0])+abs(ab[i][1]-cd[j][1])
        if temp<dist:
            dist=temp
            point=j+1
    print(point)