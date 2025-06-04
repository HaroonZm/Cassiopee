from collections import deque
import sys
input=sys.stdin.readline

while True:
    w,h=map(int,input().split())
    if w==0 and h==0: break

    # Read walls
    # lines number = 2*h-1
    # horizontal walls lines start with space, contain w-1 ints
    # vertical walls lines start without space, contain w ints
    hor_walls = []
    ver_walls = []
    for i in range(2*h-1):
        line=input().rstrip('\n')
        parts=line.strip().split()
        if i%2==0:
            # horizontal walls line (between squares in same row)
            # length = w-1
            hor_walls.append(list(map(int,parts)))
        else:
            # vertical walls line (between rows)
            # length = w
            ver_walls.append(list(map(int,parts)))

    # BFS to find shortest path
    dist=[[-1]*w for _ in range(h)]
    dist[0][0]=1
    q=deque()
    q.append((0,0))

    while q:
        r,c=q.popleft()
        d=dist[r][c]
        # Move up
        if r>0 and ver_walls[r-1][c]==0 and dist[r-1][c]<0:
            dist[r-1][c]=d+1
            q.append((r-1,c))
        # Move down
        if r<h-1 and ver_walls[r][c]==0 and dist[r+1][c]<0:
            dist[r+1][c]=d+1
            q.append((r+1,c))
        # Move left
        if c>0 and hor_walls[r][c-1]==0 and dist[r][c-1]<0:
            dist[r][c-1]=d+1
            q.append((r,c-1))
        # Move right
        if c<w-1 and hor_walls[r][c]==0 and dist[r][c+1]<0:
            dist[r][c+1]=d+1
            q.append((r,c+1))

    print(dist[h-1][w-1] if dist[h-1][w-1]>=0 else 0)