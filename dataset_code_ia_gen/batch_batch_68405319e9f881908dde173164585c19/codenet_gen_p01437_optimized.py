import sys
input=sys.stdin.readline
directions = ['N','E','S','W']
dx = [-1,0,1,0]
dy = [0,1,0,-1]

while True:
    H,W,L= map(int,input().split())
    if H==0 and W==0 and L==0:
        break
    maze=[]
    for i in range(H):
        row=list(input().rstrip('\n'))
        maze.append(row)
    for i in range(H):
        for j in range(W):
            if maze[i][j] in directions:
                x,y=i,j
                d=directions.index(maze[i][j])
                maze[i][j] = '.'
                break
        else:
            continue
        break

    # States: position and direction
    visited = dict()
    path = []
    step=0

    while step<L:
        state=(x,y,d)
        if state in visited:
            start=visited[state]
            cycle_len=step - start
            rem = (L-step)//cycle_len
            step += rem*cycle_len
            if step==L:
                break
        else:
            visited[state]=step

        # Try to move forward
        nx,ny = x+dx[d], y+dy[d]
        if 0<=nx<H and 0<=ny<W and maze[nx][ny]=='.':
            x,y=nx,ny
            step+=1
            if step==L:
                break
        else:
            d = (d+1)%4

    print(x+1,y+1,directions[d])