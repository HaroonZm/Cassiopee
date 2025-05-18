from math import cos as cos_
from math import sin as sin_
from math import sqrt
from math import radians

def cos(degree):
    return cos_(radians(degree))

def sin(degree):
    return sin_(radians(degree))

def five_points(x,y,a,r):
    lis=[]
    for i in range(5):
        lis.append((x-r*sin(a-72*i*2),y+r*cos(a-72*i*2)))
    lis.append(lis[0])
    return lis

def distance2lines(r1,r2,r3,r4):
    #check crossing
    if (((r2[0]-r1[0])*(r3[1]-r1[1])-(r2[1]-r1[1])*(r3[0]-r1[0]))\
       *((r2[0]-r1[0])*(r4[1]-r1[1])-(r2[1]-r1[1])*(r4[0]-r1[0])) <= 0) and\
       (((r4[0]-r3[0])*(r1[1]-r3[1])-(r4[1]-r3[1])*(r1[0]-r3[0]))\
       *((r4[0]-r3[0])*(r2[1]-r3[1])-(r4[1]-r3[1])*(r2[0]-r3[0])) <= 0):
        return 0
    if (0<=((r2[0]-r1[0])*(r3[0]-r1[0])+(r2[1]-r1[1])*(r3[1]-r1[1]))<=((r2[0]-r1[0])**2+(r2[1]-r1[1])**2)):
        d3=abs((r2[0]-r1[0])*(r3[1]-r1[1])-(r2[1]-r1[1])*(r3[0]-r1[0]))/sqrt((r2[1]-r1[1])**2+(r2[0]-r1[0])**2)
    else:
        d3=min(sqrt((r3[1]-r1[1])**2+(r3[0]-r1[0])**2),sqrt((r3[1]-r2[1])**2+(r3[0]-r2[0])**2))
    if (0<=((r2[0]-r1[0])*(r4[0]-r1[0])+(r2[1]-r1[1])*(r4[1]-r1[1]))<=((r2[0]-r1[0])**2+(r2[1]-r1[1])**2)):
        d4=abs((r2[0]-r1[0])*(r4[1]-r1[1])-(r2[1]-r1[1])*(r4[0]-r1[0]))/sqrt((r2[1]-r1[1])**2+(r2[0]-r1[0])**2)
    else:
        d4=min(sqrt((r4[1]-r1[1])**2+(r4[0]-r1[0])**2),sqrt((r4[1]-r2[1])**2+(r4[0]-r2[0])**2))
    return min(d3,d4)
    

def distance2stars(x1,y1,a1,r1,x2,y2,a2,r2):
    star1=five_points(x1,y1,a1,r1)
    star2=five_points(x2,y2,a2,r2)
    ans=float('inf')
    for i in range(5):
        for j in range(5):
            ans=min(ans,distance2lines(star1[i],star1[i+1],star2[j],star2[j+1]))
            ans=min(ans,distance2lines(star2[i],star2[i+1],star1[j],star1[j+1]))
    return ans

N,M,L=map(int,input().split())
while N!=0:
    stars=[]
    for i in range(N):
        stars.append(tuple(map(int,input().split())))
    d=[[0]*N for i in range(N)]
    for i in range(N):
        x1,y1,a1,r1=stars[i]
        for j in range(i+1,N):
            x2,y2,a2,r2=stars[j]
            d[i][j]=distance2stars(x1,y1,a1,r1,x2,y2,a2,r2)
    for i in range(N):
        for j in range(0,i):
            d[i][j]=d[j][i]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    print(d[M-1][L-1])
    N,M,L=map(int,input().split())