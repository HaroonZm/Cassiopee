from sys import stdin
from collections import deque

def count_islands(grid):
    visited = [[False]*12 for _ in range(12)]
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    islands = 0
    for i in range(12):
        for j in range(12):
            if grid[i][j] == '1' and not visited[i][j]:
                islands += 1
                queue = deque([(i,j)])
                visited[i][j] = True
                while queue:
                    x,y = queue.popleft()
                    for dx,dy in directions:
                        nx,ny = x+dx,y+dy
                        if 0 <= nx < 12 and 0 <= ny < 12 and not visited[nx][ny] and grid[nx][ny] == '1':
                            visited[nx][ny] = True
                            queue.append((nx,ny))
    return islands

data = []
for line in stdin:
    l=line.strip()
    if l=='': 
        if data:
            print(count_islands(data))
            data=[]
    else:
        data.append(l)
if data:
    print(count_islands(data))