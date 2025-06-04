import sys
from collections import deque

input=sys.stdin.readline
directions=[(0,1),(0,-1),(1,0),(-1,0)]

def bfs(w,h,board,start,goal):
    visited=set()
    q=deque()
    q.append((start[0],start[1],0,tuple(tuple(row) for row in board)))
    visited.add((start[0],start[1],tuple(tuple(row) for row in board)))
    while q:
        x,y,moves,b= q.popleft()
        if moves>10:
            return -1
        if (x,y)==goal:
            return moves
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if not (0<=nx<w and 0<=ny<h):
                continue
            if b[ny][nx]==1:
                continue
            # check immediate block
            if b[ny][nx]==1:
                continue
            # Cannot throw if immediate next cell is block
            # So first step must be vacant or goal
            stepx,stepy=dx,dy
            # move the stone until it hits block or goal or out of board
            cx,cy=x,y
            while True:
                cx+=dx
                cy+=dy
                if not (0<=cx<w and 0<=cy<h):
                    # out of board => fail, do not enqueue
                    break
                if b[cy][cx]==1:
                    # hit a block, stop before block
                    cx-=dx
                    cy-=dy
                    # must be different from current position (moved at least one step)
                    if (cx,cy)==(x,y):
                        break
                    # remove block
                    nb=[list(row) for row in b]
                    nb[cy+dy][cx+dx]=0
                    nbt=tuple(tuple(row) for row in nb)
                    if (cx,cy,nbt) not in visited:
                        visited.add((cx,cy,nbt))
                        q.append((cx,cy,moves+1,nbt))
                    break
                if (cx,cy)==goal:
                    # reached goal, success
                    return moves+1
            else:
                continue
    return -1

while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    board=[]
    start=None
    goal=None
    for i in range(h):
        row=list(map(int,input().split()))
        board.append(row)
        for j,v in enumerate(row):
            if v==2:
                start=(j,i)
            elif v==3:
                goal=(j,i)
    print(bfs(w,h,board,start,goal))