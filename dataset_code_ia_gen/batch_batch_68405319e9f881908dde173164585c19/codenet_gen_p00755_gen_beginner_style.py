import sys
sys.setrecursionlimit(10**7)

# directions for adjacency (up, down, left, right)
directions = [(-1,0),(1,0),(0,-1),(0,1)]

def inside(h,w,x,y):
    return 0<=x<h and 0<=y<w

# find unit panels united with panel at (0,0)
def find_united(panel,h,w):
    color = panel[0][0]
    visited = [[False]*w for _ in range(h)]
    stack = [(0,0)]
    visited[0][0] = True
    united = []
    while stack:
        x,y = stack.pop()
        united.append((x,y))
        for dx,dy in directions:
            nx,ny = x+dx,y+dy
            if inside(h,w,nx,ny) and not visited[nx][ny] and panel[nx][ny]==color:
                visited[nx][ny] = True
                stack.append((nx,ny))
    return set(united), color

# change color of united panels and fuse adjacent panels with same color
def change_color_and_fuse(panel,h,w,new_color):
    united,pos_color = find_united(panel,h,w)
    # change color of united panel
    new_panel = [row[:] for row in panel]
    for x,y in united:
        new_panel[x][y] = new_color

    # fuse adjacent panels with same color iteratively
    changed = True
    while changed:
        changed = False
        united, _ = find_united(new_panel,h,w)
        # look for adjacent same color panels to unite with united
        for x,y in united.copy():
            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                if inside(h,w,nx,ny) and (nx,ny) not in united and new_panel[nx][ny]==new_color:
                    united.add((nx,ny))
                    changed = True
        # update colors for newly united panels
        if changed:
            for x,y in united:
                new_panel[x][y] = new_color
    return new_panel, len(united)

def dfs(panel,h,w,target_color,step,max_step,memo):
    # memo key is (step, tuple of tuple panel)
    key = (step, tuple(tuple(row) for row in panel))
    if key in memo:
        return memo[key]
    if step == max_step:
        united, c = find_united(panel,h,w)
        if c == target_color:
            memo[key] = len(united)
            return len(united)
        else:
            memo[key] = 0
            return 0

    max_size = 0
    # get current color of united panel
    united, current_color = find_united(panel,h,w)
    # try to change to each color except current color
    for color in range(1,7):
        if color != current_color:
            next_panel, size = change_color_and_fuse(panel,h,w,color)
            res = dfs(next_panel,h,w,target_color,step+1,max_step,memo)
            if res > max_size:
                max_size = res
    memo[key] = max_size
    return max_size

while True:
    line = sys.stdin.readline()
    if not line:
        break
    h,w,c = map(int,line.strip().split())
    if h==0 and w==0 and c==0:
        break
    panel = []
    for _ in range(h):
        row = list(map(int,sys.stdin.readline().strip().split()))
        panel.append(row)
    memo = {}
    ans = dfs(panel,h,w,c,0,5,memo)
    print(ans)