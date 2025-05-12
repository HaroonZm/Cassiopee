import sys
sys.setrecursionlimit(1000000)

def check(i,j):
    global n
    global m
    if m[i][j]==0:
        m[i][j]=-1
        if i+1<n*4+2:
            check(i+1,j)
        if i-1>=0:
            check(i-1,j)
        if j+1<n*4+2:
            check(i,j+1)
        if j-1>=0:
            check(i,j-1)

while True:
    n=int(input())
    if n==0:
        break
    points=[]
    plane=[[-1,-1,-1,-1] for i in range(n)]
    dic={}
    for i in range(n):
        a,b,x,y=map(int,input().split())
        dic[(a,b,i)]=0
        dic[(x,y,i)]=1
        points.append((a,b,i))
        points.append((x,y,i))
    points=sorted(points)
    p=0
    for i in range(len(points)):
        if dic[points[i]]==0:
            plane[points[i][2]][0]=p
        else:
            plane[points[i][2]][2]=p
        if i+1<len(points) and points[i][0]==points[i+1][0]:
            pass
        else:
            p+=1
    points=sorted(points,key=lambda q:q[1])
    p=0
    for i in range(len(points)):
        if dic[points[i]]==0:
            plane[points[i][2]][1]=p
        else:
            plane[points[i][2]][3]=p
        if i+1<len(points) and points[i][1]==points[i+1][1]:
            pass
        else:
            p+=1
    m=[[0 for i in range(n*4+2)]for i in range(n*4+2)]
    for p in plane:
        for j in range((p[1]-p[3])*2+1):
            m[p[0]*2+1][p[3]*2+j+1]=1
            m[p[2]*2+1][p[3]*2+j+1]=1
        for j in range((p[2]-p[0])*2+1):
            m[p[0]*2+j+1][p[3]*2+1]=1
            m[p[0]*2+j+1][p[1]*2+1]=1
    ans=0
    for i in range(n*4+2):
        for j in range(n*4+2):
            if m[i][j]==0:
                ans+=1
                check(i,j)
    print(ans)