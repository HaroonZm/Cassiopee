H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

directions = {'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}
# Moves allowed relative to facing direction
move_dirs = {
    'U': ['U', 'L', 'R'],
    'D': ['D', 'L', 'R'],
    'L': ['L', 'U', 'D'],
    'R': ['R', 'U', 'D']
}

# Find frog start
frog_r, frog_c, frog_f = -1,-1,''
leaves = 0
for i in range(H):
    for j in range(W):
        if grid[i][j] in 'UDLR':
            frog_r, frog_c, frog_f = i,j,grid[i][j]
            grid[i][j] = 'o'
            leaves += 1
        elif grid[i][j] == 'o':
            leaves += 1

def in_grid(r,c):
    return 0 <= r < H and 0 <= c < W

def next_leaf(r,c,dr,dc):
    r += dr
    c += dc
    while in_grid(r,c):
        if grid[r][c] == 'o':
            return r,c
        r += dr
        c += dc
    return None

path = []
found = False

def dfs(r,c,facing,leaf_count):
    global found
    if found:
        return
    if leaf_count == 1:
        found = True
        print(''.join(path))
        return
    for nd in move_dirs[facing]:
        dr, dc = directions[nd]
        nxt = next_leaf(r,c,dr,dc)
        if nxt is None:
            continue
        nr,nc = nxt
        # jump
        grid[r][c] = '.'  # current leaf sinks
        path.append(nd)
        grid[nr][nc] = '.'  # frog stands on a leaf but it remains until he jumps away, so keep 'o'
        dfs(nr,nc,nd,leaf_count-1)
        if found:
            return
        grid[r][c] = 'o'  # backtrack
        path.pop()

dfs(frog_r,frog_c,frog_f,leaves)