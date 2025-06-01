n=int(input())
for dataset in range(1,n+1):
    input()
    grid=[list(map(int,list(input().strip()))) for _ in range(8)]
    x=int(input())-1
    y=int(input())-1
    from collections import deque
    q=deque()
    if grid[y][x]==1:
        q.append((x,y))
        grid[y][x]=0
    while q:
        cx,cy=q.popleft()
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            for step in range(1,4):
                nx=cx+dx*step
                ny=cy+dy*step
                if 0<=nx<8 and 0<=ny<8:
                    if grid[ny][nx]==1:
                        grid[ny][nx]=0
                        q.append((nx,ny))
                else:
                    break
    print(f'Data {dataset}:')
    for row in grid:
        print(''.join(map(str,row)))