H,W=map(int,input().split())
grid=[list(input()) for _ in range(H)]
from collections import deque

d=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def count_dot(i,j):
    c=0
    for dx,dy in d:
        x,y=i+dx,j+dy
        if 0<=x<H and 0<=y<W and grid[x][y]=='.':
            c+=1
    return c

queue=deque()
for i in range(1,H-1):
    for j in range(1,W-1):
        if grid[i][j] != '.':
            if count_dot(i,j)>=int(grid[i][j]):
                queue.append((i,j))

res=0
while queue:
    res+=1
    next_queue=deque()
    while queue:
        i,j=queue.popleft()
        if grid[i][j]=='.':
            continue
        if count_dot(i,j)>=int(grid[i][j]):
            grid[i][j]='.'
            for dx,dy in d:
                x,y=i+dx,j+dy
                if 0<x<H-1 and 0<y<W-1 and grid[x][y]!='.':
                    if count_dot(x,y)>=int(grid[x][y]):
                        next_queue.append((x,y))
    queue=next_queue
print(res)