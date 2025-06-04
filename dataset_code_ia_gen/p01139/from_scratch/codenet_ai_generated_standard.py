from sys import stdin
from collections import deque

DIRS = [(1,0),(-1,0),(0,1),(0,-1)]

def inside(x,y,w,h):
    return 0<=x<w and 0<=y<h

def solve():
    lines = iter(stdin.read().splitlines())
    while True:
        w,h = map(int,next(lines).split())
        if w==0 and h==0: break
        grid = [list(next(lines)) for _ in range(h)]

        black_adj = [[False]*w for _ in range(h)]
        white_adj = [[False]*w for _ in range(h)]

        # Mark black adjacency
        queue = deque()
        for y in range(h):
            for x in range(w):
                if grid[y][x]=='B':
                    black_adj[y][x] = True
                    queue.append((x,y))
        while queue:
            x,y = queue.popleft()
            for dx,dy in DIRS:
                nx,ny = x+dx,y+dy
                if inside(nx,ny,w,h) and not black_adj[ny][nx] and grid[ny][nx]=='.':
                    black_adj[ny][nx] = True
                    queue.append((nx,ny))

        # Mark white adjacency
        queue = deque()
        for y in range(h):
            for x in range(w):
                if grid[y][x]=='W':
                    white_adj[y][x] = True
                    queue.append((x,y))
        while queue:
            x,y = queue.popleft()
            for dx,dy in DIRS:
                nx,ny = x+dx,y+dy
                if inside(nx,ny,w,h) and not white_adj[ny][nx] and grid[ny][nx]=='.':
                    white_adj[ny][nx] = True
                    queue.append((nx,ny))

        black_count = 0
        white_count = 0

        for y in range(h):
            for x in range(w):
                if grid[y][x]=='.':
                    is_black = black_adj[y][x]
                    is_white = white_adj[y][x]
                    # Check adjacency of this cell to opposite color's pins
                    def adj_to_opposite(c):
                        for dx,dy in DIRS:
                            nx,ny = x+dx,y+dy
                            if inside(nx,ny,w,h) and grid[ny][nx]==c:
                                return True
                        return False
                    if is_black and not adj_to_opposite('W'):
                        black_count += 1
                    if is_white and not adj_to_opposite('B'):
                        white_count += 1

        print(black_count, white_count)

if __name__=="__main__":
    solve()