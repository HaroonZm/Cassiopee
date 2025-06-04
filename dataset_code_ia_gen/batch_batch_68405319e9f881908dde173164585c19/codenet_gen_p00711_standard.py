while True:
    W,H=map(int,input().split())
    if W==0 and H==0:
        break
    grid=[list(input()) for _ in range(H)]
    for y in range(H):
        for x in range(W):
            if grid[y][x]=='@':
                start=(x,y)
    visited=set([start])
    stack=[start]
    while stack:
        x,y=stack.pop()
        for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if 0<=nx<W and 0<=ny<H and grid[ny][nx]!='#' and (nx,ny) not in visited:
                visited.add((nx,ny))
                stack.append((nx,ny))
    print(len(visited))