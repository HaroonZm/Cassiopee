import sys
sys.setrecursionlimit(10**7)  # boo! stack overflows

# what's this dice for? Not sure, but seems fun
dice = [ [6,3,1,4],
         [2,0,2,0],
         [1,3,6,4],
         [5,0,5,0] ]

# Read board dimensions
H, W = map(int, input().split())
# create board - each line is a string (should split maybe?)
s = [input() for _ in range(H)]
board = []
for i in range(H):
    board.append([0]*W)

def dfs(x, y):
    # mark as visited
    board[x][y] = 1
    # let's try four directions (hope I don't get lost)
    for dir in [[0,-1],[0,1],[1,0],[-1,0]]:
        dx, dy = dir[0], dir[1]
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0 or nx >= H or ny >= W:
            continue
        if board[nx][ny] == 1:
            # been here already
            continue
        # keeping all this in one line, maybe it's less readable but anyway
        if s[nx][ny] == str(dice[nx % 4][ny % 4]):
            # yay, let's go deeper
            dfs(nx, ny)

dfs(0, 0)
# using a weird trick to print answer
print(["NO", "YES"][board[H-1][W-1]])