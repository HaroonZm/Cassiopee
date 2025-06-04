import sys
sys.setrecursionlimit(10**7)

H,W=map(int,input().split())
grid=[list(input()) for _ in range(H)]

# Directions and their delta: U,D,L,R
dir_map={'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}
# For each facing direction, moves allowed: forward, left, right (relative)
move_dir={
    'U':['U','L','R'],
    'D':['D','R','L'],
    'L':['L','D','U'],
    'R':['R','U','D']
}

# Encode grid in bitmask: 0 to H*W-1, 1=leaf present,0=water
# We also track frog's position (r,c) and direction
pos_to_bit=lambda r,c: r*W+c

leaves=0
frog_r=frog_c=frog_dir=None
for r in range(H):
    for c in range(W):
        ch=grid[r][c]
        if ch in 'UDLR':
            frog_r, frog_c, frog_dir = r,c,ch
            leaves |= 1<<pos_to_bit(r,c)
        elif ch=='o':
            leaves |= 1<<pos_to_bit(r,c)

target_leaves_count=1
total_leaves=bin(leaves).count('1')

memo=dict()

def neighbors(r,c,dir_facing, mask):
    # From current position, find possible jumps index and resulting positions+facing
    res=[]
    for ndir in move_dir[dir_facing]:
        dr,dc=dir_map[ndir]
        nr,nc=r+dr,c+dc
        while 0<=nr<H and 0<=nc<W:
            b=pos_to_bit(nr,nc)
            if (mask>>b)&1:
                res.append((nr,nc,ndir))
                break
            nr+=dr
            nc+=dc
    return res

def dfs(r,c,dir_facing,mask,remain):
    # returns path string or empty if no solution
    if remain==1:
        return ''
    key=(r,c,dir_facing,mask)
    if key in memo:
        return memo[key]
    for nr,nc,ndir in neighbors(r,c,dir_facing,mask):
        nb=pos_to_bit(nr,nc)
        cb=pos_to_bit(r,c)
        nmask=mask&( ~(1<<cb) ) # remove current leaf, it sinks
        res=dfs(nr,nc,ndir,nmask,remain-1)
        if res is not None:
            memo[key]=ndir+res
            return memo[key]
    memo[key]=None
    return None

ans=dfs(frog_r,frog_c,frog_dir,leaves,total_leaves)
print(ans)