h,w=map(int,input().split())
t1=[input() for _ in range(h)]
h,w=map(int,input().split())
t2=[input() for _ in range(h)]
h,w=map(int,input().split())
t3=[input() for _ in range(h)]
h,w=map(int,input().split())
t4=[input() for _ in range(h)]

tetrominos=[t1,t2,t3,t4]

n=int(input())
boards=[]
for _ in range(n*4):
    boards.append(input())

def get_blocks(t):
    cells=[]
    for i,r in enumerate(t):
        for j,c in enumerate(r):
            if c=='#':
                cells.append((i,j))
    return cells

tet_blocks=[get_blocks(t) for t in tetrominos]

def can_place(board, used, block, r, c):
    for br,bc in block:
        rr=r+br
        cc=c+bc
        if rr<0 or rr>=4 or cc<0 or cc>=10:
            return False
        if board[rr][cc]!='#' or used[rr][cc]:
            return False
    return True

def place(used, block, r, c, val):
    for br,bc in block:
        rr=r+br
        cc=c+bc
        used[rr][cc]=val

from itertools import combinations

for i in range(n):
    board=boards[4*i:4*i+4]
    # all 10*4=40 cells, but only 28 blocks with #
    used=[[False]*10 for _ in range(4)]
    found=False
    # try all combinations of 3 tetrominos out of 4
    for combo in combinations(range(4),3):
        # backtracking placement
        def backtrack(idx):
            if idx==3:
                # all 3 placed
                # check if whole board covered exactly by these 3 tetrominos
                count=0
                for rr in range(4):
                    for cc in range(10):
                        if board[rr][cc]=='#' and used[rr][cc]:
                            count+=1
                return count==28
            tid=combo[idx]
            block=tet_blocks[tid]
            for r in range(4):
                for c in range(10):
                    if can_place(board,used,block,r,c):
                        place(used,block,r,c,True)
                        if backtrack(idx+1):
                            return True
                        place(used,block,r,c,False)
            return False
        if backtrack(0):
            found=True
            break
    print("Yes" if found else "No")