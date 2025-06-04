import sys
input=sys.stdin.readline

N=int(input())
diff=[[0]*1002 for _ in range(1002)]
for _ in range(N):
    x1,y1,x2,y2=map(int,input().split())
    diff[x1][y1]+=1
    diff[x2][y1]-=1
    diff[x1][y2]-=1
    diff[x2][y2]+=1

for x in range(1001):
    for y in range(1001):
        diff[x+1][y]+=diff[x][y]
for x in range(1002):
    for y in range(1001):
        diff[x][y+1]+=diff[x][y]

res=0
for x in range(1001):
    for y in range(1001):
        if diff[x][y]>res:
            res=diff[x][y]
print(res)