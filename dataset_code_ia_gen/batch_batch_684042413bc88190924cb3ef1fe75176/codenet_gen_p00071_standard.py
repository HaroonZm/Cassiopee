n=int(input())
input()
for t in range(1,n+1):
    grid=[list(input()) for _ in range(8)]
    input()
    x,y=int(input())-1,int(input())-1
    from collections import deque
    q=deque()
    if grid[y][x]=='1':
        q.append((x,y))
    exploded=[[False]*8 for _ in range(8)]
    while q:
        cx,cy=q.popleft()
        if exploded[cy][cx]:
            continue
        exploded[cy][cx]=True
        grid[cy][cx]='0'
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            for dist in range(1,4):
                nx=cx+dx*dist
                ny=cy+dy*dist
                if 0<=nx<8 and 0<=ny<8:
                    if grid[ny][nx]=='1' and not exploded[ny][nx]:
                        q.append((nx,ny))
    print(f"Data {t}:")
    for row in grid:
        print(''.join(row))