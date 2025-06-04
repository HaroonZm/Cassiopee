import sys
input=sys.stdin.readline

n,u,v,m=map(int,input().split())
size=n*n

def read_matrix():
    mat=[list(map(int,input().split())) for _ in range(n)]
    pos=dict()
    for i in range(n):
        for j in range(n):
            pos[mat[i][j]]=(i,j)
    return pos

pos_usagi=read_matrix()
pos_neko=read_matrix()

cards=[int(input()) for _ in range(m)]

# Directions: horizontal, vertical, diag1, diag2
dirs=[(0,1),(1,0),(1,1),(1,-1)]

def check_win(marked,u_bound):
    count=0
    for i in range(n):
        for j in range(n):
            if not marked[i][j]:
                continue
            for dx,dy in dirs:
                x,y=i,j
                seq=0
                while 0<=x<n and 0<=y<n and marked[x][y]:
                    seq+=1
                    x+=dx
                    y+=dy
                if seq>=u_bound:
                    return True
    return False

marked_usagi=[[False]*n for _ in range(n)]
marked_neko=[[False]*n for _ in range(n)]

won=None

for i,c in enumerate(cards):
    turn=i%2
    if won is not None:
        continue
    if turn==0 and c in pos_usagi:
        x,y=pos_usagi[c]
        marked_usagi[x][y]=True
        if check_win(marked_usagi,u):
            won="USAGI"
    elif turn==1 and c in pos_neko:
        x,y=pos_neko[c]
        marked_neko[x][y]=True
        if check_win(marked_neko,v):
            if won is None:
                won="NEKO"

if won is None:
    print("DRAW")
else:
    print(won)