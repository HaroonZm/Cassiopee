import sys
sys.setrecursionlimit(10**7)

dice = [[6,3,1,4],
        [2,0,2,0],
        [1,3,6,4],
        [5,0,5,0]]
H,W = map(int,input().split())
s = list(input() for _ in range(H))
board = [[0]*W for _ in range(H)]

def dfs(x,y):
    board[x][y] = 1
    for dx,dy in [[0,-1],[0,1],[1,0],[-1,0]]:
        if not(0 <= dx+x < H and 0 <= dy+y < W):
            continue
        if(board[x+dx][y+dy] == 1):
            continue

        if s[x+dx][y+dy] == str(dice[(x+dx)%4][(y+dy)%4]):
            dfs(dx+x,dy+y)

dfs(0,0)
print(["NO","YES"][board[-1][-1]])