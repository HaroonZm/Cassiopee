import sys
from collections import deque
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

H,W=map(int,input().split())
grid=[list(input().rstrip()) for _ in range(H)]

# directions 8 neighbors
dirs=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

# Count adjacent '.' for each block
adj_empty=[[0]*W for _ in range(H)]
for i in range(1,H-1):
    for j in range(1,W-1):
        if grid[i][j]!='.':
            c=0
            for dx,dy in dirs:
                ni, nj = i+dx, j+dy
                if grid[ni][nj]=='.':
                    c+=1
            adj_empty[i][j]=c

queue=deque()
for i in range(1,H-1):
    for j in range(1,W-1):
        if grid[i][j]!='.' and adj_empty[i][j]>=int(grid[i][j]):
            queue.append((i,j))

ans=0
while queue:
    ans+=1
    next_queue=deque()
    while queue:
        i,j=queue.popleft()
        if grid[i][j]=='.':
            continue
        grid[i][j]='.'  # collapse
        for dx,dy in dirs:
            ni, nj = i+dx, j+dy
            if 0<=ni<H and 0<=nj<W and grid[ni][nj]!='.':
                adj_empty[ni][nj]+=1
                if adj_empty[ni][nj]>=int(grid[ni][nj]):
                    next_queue.append((ni,nj))
    queue=next_queue

print(ans)