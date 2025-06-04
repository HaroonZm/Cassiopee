h,w,d,n=map(int,input().split())
grid=[list(input()) for _ in range(h)]
r=list(map(int,input().split()))
qs=[tuple(map(int,input().split())) for _ in range(n)]

from collections import deque

# find start D
for y in range(h):
    for x in range(w):
        if grid[y][x]=='D':
            start=(x,y)
            break

def dist_map(sx,sy):
    dist=[[-1]*w for _ in range(h)]
    dist[sy][sx]=0
    q=deque([(sx,sy)])
    while q:
        x,y=q.popleft()
        for dx,dy in[(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny=x+dx,y+dy
            if 0<=nx<w and 0<=ny<h and grid[ny][nx]!='#' and dist[ny][nx]<0:
                dist[ny][nx]=dist[y][x]+1
                q.append((nx,ny))
    return dist

dist_from_start=dist_map(*start)

# For each query, define the possible treasure positions set
# 0: square radius r_1 around (x,y)
# s in [1,d-1]: annulus between r_{s} and r_{s+1}
# d: outside r_d

# compute Manhattan distance? No, problem uses square
# Square radius means |dx|<=r, |dy|<=r
def in_square(cx,cy,x,y,radius):
    return abs(cx-x)<=radius and abs(cy-y)<=radius

ans_mask=[[True]*w for _ in range(h)]

for (xq,yq,sq) in qs:
    # reachable from start
    if dist_from_start[yq][xq]<0:
        # problem states D's location can always reach queries
        # but just in case
        print("Broken")
        exit()

    new_mask=[[False]*w for _ in range(h)]
    if sq==0:
        # inside r_1 square
        r1=r[0]
        for y in range(h):
            for x in range(w):
                if grid[y][x]!='#' and in_square(xq,yq,x,y,r1):
                    new_mask[y][x]=True
    elif 1<=sq<=d-1:
        r_outer=r[sq]
        r_inner=r[sq-1]
        for y in range(h):
            for x in range(w):
                if grid[y][x]=='#': continue
                dist_x=abs(xq - x)
                dist_y=abs(yq - y)
                if (dist_x<=r_outer and dist_y<=r_outer) and not (dist_x<=r_inner and dist_y<=r_inner):
                    new_mask[y][x]=True
    else: # sq==d
        r_d=r[d-1]
        for y in range(h):
            for x in range(w):
                if grid[y][x]=='#': continue
                if not (abs(xq - x)<=r_d and abs(yq - y)<=r_d):
                    new_mask[y][x]=True

    # intersect answer mask with new_mask
    changed=False
    for y in range(h):
        for x in range(w):
            if ans_mask[y][x] and not new_mask[y][x]:
                ans_mask[y][x]=False
                changed=True

# Check how many possible treasure cells remain
candidates=[]
for y in range(h):
    for x in range(w):
        if ans_mask[y][x]:
            candidates.append((x,y))

if not candidates:
    print("Broken")
    exit()

if len(candidates)>1:
    print("Unknown")
    exit()

tx,ty=candidates[0]

# Check if treasure cell reachable from start
if dist_from_start[ty][tx]<0:
    print("No")
    exit()

# BFS from treasure to find reachable from it
dist_from_treasure=dist_map(tx,ty)

# Check if start reachable from treasure
if dist_from_treasure[start[1]][start[0]]<0:
    # treasure can't reach start, so D can't reach treasure
    print("No")
    exit()

# Check if all queries make sense, i.e. treasure inside or outside specified regions
def check_query(xq,yq,sq,tx,ty):
    if sq==0:
        return in_square(xq,yq,tx,ty,r[0])
    elif 1<=sq<=d-1:
        r_outer=r[sq]
        r_inner=r[sq-1]
        dist_x=abs(xq - tx)
        dist_y=abs(yq - ty)
        inside_outer=dist_x<=r_outer and dist_y<=r_outer
        inside_inner=dist_x<=r_inner and dist_y<=r_inner
        return inside_outer and not inside_inner
    else:
        r_d=r[d-1]
        return not (abs(xq - tx)<=r_d and abs(yq - ty)<=r_d)

for (xq,yq,sq) in qs:
    if not check_query(xq,yq,sq,tx,ty):
        print("Broken")
        exit()

print("Yes")