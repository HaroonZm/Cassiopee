import sys
import heapq

dxy = [(dx, dy) for dx in range(-3,4) for dy in range(-3,4) if 0 < abs(dx)+abs(dy) <= 3]

def neighbors(x,y,w,h):
    for dx,dy in dxy:
        nx, ny = x+dx, y+dy
        if 0<=nx<w and 0<=ny<h:
            yield nx, ny

def solve(w,h,grid):
    S = [(x,h-1) for x in range(w) if grid[h-1][x] == 'S']
    T = set((x,0) for x in range(w) if grid[0][x] == 'T')
    # dist[(lx,ly,rx,ry,foot)] = time, foot=0 if next step left foot, 1 if right foot
    dist = {}
    heap = []
    for x in range(w):
        if grid[h-1][x] == 'S':
            # initial left foot only
            # start with right foot to move since left foot on block
            # so next move on right foot, foot=1
            # left foot (lx,ly), right foot (rx,ry)
            # But initial foot is only on one block, so we put other foot off cliff (-1,-1)
            # But constraints need lx < rx, so we can set right foot slightly on left of left foot 
            # Actually we must start with putting one foot on S, step first foot there, so next step on other foot
            # Start state: left foot on (x,h-1), right foot off cliff (-1,-1), next move right foot (1)
            dist[(x,h-1,-1,-1,1)] = 0
            heapq.heappush(heap,(0,(x,h-1,-1,-1,1)))
            dist[(-1,-1,x,h-1,0)] = 0
            heapq.heappush(heap,(0,(-1,-1,x,h-1,0)))
    while heap:
        t,(lx,ly,rx,ry,foot) = heapq.heappop(heap)
        if dist.get((lx,ly,rx,ry,foot),float('inf'))<t:
            continue
        # check if finished
        if foot == 0:
            # next move left foot
            # last foot was right foot at (rx,ry), check if rx,ry on T row
            if (rx,ry) in T:
                return t
        else:
            # next move right foot
            if (lx,ly) in T:
                return t
        # next step we move foot (foot), so place new foot on a block within constraints
        if foot == 0:
            ox, oy = rx, ry  # last foot right foot
            fixed_x, fixed_y = lx, ly
        else:
            ox, oy = lx, ly
            fixed_x, fixed_y = rx, ry
        # If fixed foot is off cliff (-1,-1), means first move, we can put other foot on any S adjacent?
        # But initial states handled above, so assuming fixed foot is on cliff
        for nx, ny in neighbors(fixed_x, fixed_y, w, h):
            # must satisfy lx < rx
            if foot == 0:
                # move left foot, so nx<rx or rx=-1, ly
                if rx != -1 and not (nx < rx):
                    continue
                # distance condition
                if rx != -1 and abs(nx - rx) + abs(ny - ry) > 3:
                    continue
                # left foot on nx,ny, right foot fixed at rx,ry
                if grid[ny][nx] == 'X':
                    continue
                timecost = 0 if grid[ny][nx] in ('S','T') else int(grid[ny][nx])
                nt = t + timecost
                key = (nx, ny, rx, ry, 1)
                if dist.get(key,float('inf'))>nt:
                    dist[key]=nt
                    heapq.heappush(heap,(nt,key))
            else:
                # move right foot, so lx<nx or lx=-1
                if lx != -1 and not (lx < nx):
                    continue
                # distance condition
                if lx != -1 and abs(nx - lx) + abs(ny - ly) > 3:
                    continue
                if grid[ny][nx] == 'X':
                    continue
                timecost = 0 if grid[ny][nx] in ('S','T') else int(grid[ny][nx])
                nt = t + timecost
                key = (lx, ly, nx, ny, 0)
                if dist.get(key,float('inf'))>nt:
                    dist[key]=nt
                    heapq.heappush(heap,(nt,key))
    return -1

input = sys.stdin.readline
while True:
    line = ''
    while line.strip() == '':
        line = input()
        if not line:
            exit()
    w,h = map(int,line.split())
    if w==0 and h==0:
        break
    grid = [input().split() for _ in range(h)]
    print(solve(w,h,grid))