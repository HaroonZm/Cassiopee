import sys
sys.setrecursionlimit(10**7)
M,N=map(int,sys.stdin.readline().split())
board=[list(sys.stdin.readline().rstrip('\n')) for _ in range(M)]

pos=dict()
for i in range(M):
    for j in range(N):
        c=board[i][j]
        if c!='.':
            if c not in pos:
                pos[c]=[]
            pos[c].append((i,j))

dirs=[(0,-1),(0,1),(-1,0),(1,0)]
def reachable(i,j):
    if 0<=i<M and 0<=j<N:
        return True
    return False

# Precompute for each empty cell the tile seen in each direction
# To optimize, for each column, precompute nearest tile above and below each cell
up=[[(-1,'')]*N for _ in range(M)]
down=[[(-1,'')]*N for _ in range(M)]
left=[[(-1,'')]*N for _ in range(M)]
right=[[(-1,'')]*N for _ in range(M)]

for j in range(N):
    last=-1
    lastc='.'
    for i in range(M):
        if board[i][j]!='.':
            last=i
            lastc=board[i][j]
        up[i][j]=(last,lastc)
    last=-1
    lastc='.'
    for i in reversed(range(M)):
        if board[i][j]!='.':
            last=i
            lastc=board[i][j]
        down[i][j]=(last,lastc)

for i in range(M):
    last=-1
    lastc='.'
    for j in range(N):
        if board[i][j]!='.':
            last=j
            lastc=board[i][j]
        left[i][j]=(last,lastc)
    last=-1
    lastc='.'
    for j in reversed(range(N)):
        if board[i][j]!='.':
            last=j
            lastc=board[i][j]
        right[i][j]=(last,lastc)

memo=dict()

def board_to_key(bd):
    return tuple(tuple(row) for row in bd)

def score_state(bd):
    key=board_to_key(bd)
    if key in memo:
        return memo[key]
    res=0
    moved=False
    # For all empty cells
    for i in range(M):
        for j in range(N):
            if bd[i][j]!='.':
                continue
            tiles=[]
            # up
            ux,uc=up[i][j]
            if ux!=-1 and bd[ux][j]==uc:
                tiles.append((ux,j,uc))
            # down
            dx,dc=down[i][j]
            if dx!=-1 and bd[dx][j]==dc:
                tiles.append((dx,j,dc))
            # left
            ly,lc=left[i][j]
            if ly!=-1 and bd[i][ly]==lc:
                tiles.append((i,ly,lc))
            # right
            ry,rc=right[i][j]
            if ry!=-1 and bd[i][ry]==rc:
                tiles.append((i,ry,rc))
            if not tiles:
                continue
            color_count=dict()
            for _,_,c in tiles:
                color_count[c]=color_count.get(c,0)+1
            colors_to_remove = [c for c,v in color_count.items() if v>=2]
            if not colors_to_remove:
                continue
            new_bd = [row[:] for row in bd]
            removed=0
            for c in colors_to_remove:
                for x,y,ch in tiles:
                    if ch==c:
                        new_bd[x][y]='.'
                        removed+=1
            moved=True
            res=max(res,removed+score_state(new_bd))
    if not moved:
        memo[key]=0
        return 0
    memo[key]=res
    return res

print(score_state(board))