from sys import stdin
from collections import deque

def bfs(grid, visited, start):
    q = deque([start])
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    visited[start[0]][start[1]] = True
    while q:
        r,c = q.popleft()
        for dr,dc in directions:
            nr,nc = r+dr, c+dc
            if 0<=nr<12 and 0<=nc<12 and not visited[nr][nc] and grid[nr][nc]=='1':
                visited[nr][nc] = True
                q.append((nr,nc))

lines = [line.rstrip('\n') for line in stdin if line.strip() or line=='']
datasets = []
tmp = []
for line in lines:
    if not line.strip():
        if tmp:
            datasets.append(tmp)
            tmp = []
    else:
        tmp.append(line)
if tmp:
    datasets.append(tmp)

for grid in datasets:
    visited = [[False]*12 for _ in range(12)]
    count = 0
    for i in range(12):
        for j in range(12):
            if grid[i][j]=='1' and not visited[i][j]:
                bfs(grid, visited, (i,j))
                count +=1
    print(count)