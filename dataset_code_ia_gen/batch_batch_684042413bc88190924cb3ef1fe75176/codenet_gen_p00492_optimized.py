W,H=map(int,input().split())
grid=[[0]*(W+2)]
for _ in range(H):
    grid.append([0]+list(map(int,input().split()))+[0])
grid.append([0]*(W+2))
from collections import deque
visited=[[False]*(W+2) for _ in range(H+2)]
q=deque()
q.append((0,0))
visited[0][0]=True
# 隣接方向（奇数行・偶数行で異なる）
dx_even=[1,-1,0,0,-1,1]
dy_even=[0,0,1,-1,1,1]
dx_odd=[1,-1,0,0,1,-1]
dy_odd=[0,0,1,-1,-1,-1]
perimeter=0
while q:
    x,y=q.popleft()
    directions=zip((dx_odd if y%2 else dx_even),(dy_odd if y%2 else dy_even))
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<=W+1 and 0<=ny<=H+1:
            if grid[ny][nx]==1:
                perimeter+=1
            elif not visited[ny][nx]:
                visited[ny][nx]=True
                q.append((nx,ny))
print(perimeter)