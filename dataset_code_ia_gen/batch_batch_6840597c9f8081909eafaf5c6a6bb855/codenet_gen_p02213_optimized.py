H,W=map(int,input().split())
grid=[input() for _ in range(H)]

# サイコロの状態：底(bottom), 上(top), 前(front), 後(back), 右(right), 左(left)
# 初期状態：bottom=6, front=2, right=3
# topは6の対面なので1, backは2の対面なので5, leftは3の対面なので4
# 状態は(bottom, front, right)の3つで管理（残りは一意に決まる）

from collections import deque

def roll(dice, direction):
    b,f,r = dice
    # bottom, front, right を90度回転させる（転がす）
    # 上方向(i増加方向)に転がす: bottom->front, front->top, top->back, back->bottom のサイクル
    # 左右方向(j増加方向)に転がす: bottom->right, right->top, top->left, left->bottom のサイクル
    # top=7 - bottom, back=7 - front, left=7 - right
    
    top = 7 - b
    back = 7 - f
    left = 7 - r
    if direction == 0:  # 上(i+1)
        # bottom->front, front->top, top->back, back->bottom
        nb = f
        nf = top
        nr = r
    elif direction == 1:  # 下(i-1)
        # bottom->back, back->top, top->front, front->bottom の逆
        nb = back
        nf = b
        nr = r
    elif direction == 2:  # 右(j+1)
        # bottom->right, right->top, top->left, left->bottom
        nb = r
        nf = f
        nr = top
    else: # 左(j-1)
        # bottom->left, left->top, top->right, right->bottom の逆
        nb = left
        nf = f
        nr = b
    return (nb,nf,nr)

# directions: 上(i+1), 下(i-1), 右(j+1), 左(j-1)
dirs = [(1,0),( -1,0),(0,1),(0,-1)]

start = (0,0)  # 0-indexed
start_dice = (6,2,3)

from collections import deque
q = deque()
q.append((start[0],start[1],start_dice))
visited = set()
visited.add((start[0],start[1],start_dice))

while q:
    i,j,dice = q.popleft()
    if (i,j)==(H-1,W-1):
        print("YES")
        break
    for di,dj in dirs:
        ni,nj = i+di,j+dj
        if 0<=ni<H and 0<=nj<W:
            c=grid[ni][nj]
            if c=='#': continue
            ndice = roll(dice, dirs.index((di,dj)))
            bottom = ndice[0]
            if bottom == int(c):
                key=(ni,nj,ndice)
                if key not in visited:
                    visited.add(key)
                    q.append((ni,nj,ndice))
else:
    print("NO")