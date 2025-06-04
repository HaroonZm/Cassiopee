import sys
from collections import deque

def solve(field):
    h, w = 12, 6
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    chain = 0

    while True:
        visited = [[False]*w for _ in range(h)]
        to_erase = [[False]*w for _ in range(h)]
        erased_any = False

        # 1) Find connected blocks >=4 of same color (except 'O')
        for i in range(h):
            for j in range(w):
                if field[i][j] not in ['.', 'O'] and not visited[i][j]:
                    q = deque()
                    q.append((i,j))
                    visited[i][j] = True
                    comp = [(i,j)]
                    c = field[i][j]
                    while q:
                        x,y = q.popleft()
                        for dx,dy in dirs:
                            nx, ny = x+dx, y+dy
                            if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and field[nx][ny]==c:
                                visited[nx][ny] = True
                                q.append((nx,ny))
                                comp.append((nx,ny))
                    if len(comp) >=4:
                        erased_any = True
                        for x,y in comp:
                            to_erase[x][y] = True

        if not erased_any:
            return chain
        chain += 1

        # 2) Remove all connected basic blocks found above
        for i in range(h):
            for j in range(w):
                if to_erase[i][j]:
                    field[i][j] = '.'

        # 3) Remove 'O' blocks adjacent to removed basic blocks
        # First find O positions adjacent to erased basic blocks
        O_to_erase = set()
        for i in range(h):
            for j in range(w):
                if to_erase[i][j]:
                    for dx,dy in dirs:
                        nx, ny = i+dx, j+dy
                        if 0<=nx<h and 0<=ny<w and field[nx][ny]=='O':
                            O_to_erase.add((nx,ny))
        if O_to_erase:
            erased_any = True
            for x,y in O_to_erase:
                field[x][y] = '.'

        # 4) Gravity - let blocks fall down
        for col in range(w):
            stack = []
            for row in range(h-1,-1,-1):
                if field[row][col] != '.':
                    stack.append(field[row][col])
            for row in range(h-1,-1,-1):
                field[row][col] = stack[h-1 - row] if h-1 - row < len(stack) else '.'

# Read input and process datasets
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    field = [list(input().rstrip('\n')) for _ in range(12)]
    print(solve(field))