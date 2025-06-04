h,w,n = map(int,input().split())
field = [list(input()) for _ in range(h)]

def in_field(r,c): return 0<=r<h and 0<=c<w

def erase_and_drop(board):
    while True:
        to_erase = [[False]*w for _ in range(h)]
        for i in range(h):
            cnt = 1
            for j in range(1,w):
                if board[i][j] != '.' and board[i][j] == board[i][j-1]:
                    cnt += 1
                else:
                    if cnt >= n:
                        for k in range(j-cnt,j): to_erase[i][k] = True
                    cnt = 1
            if cnt >= n:
                for k in range(w-cnt,w): to_erase[i][k] = True
        for j in range(w):
            cnt = 1
            for i in range(1,h):
                if board[i][j] != '.' and board[i][j] == board[i-1][j]:
                    cnt += 1
                else:
                    if cnt >= n:
                        for k in range(i-cnt,i): to_erase[k][j] = True
                    cnt = 1
            if cnt >= n:
                for k in range(h-cnt,h): to_erase[k][j] = True
        changed = False
        for i in range(h):
            for j in range(w):
                if to_erase[i][j]:
                    board[i][j] = '.'
                    changed = True
        if not changed:
            break
        for j in range(w):
            stack = [board[i][j] for i in range(h) if board[i][j] != '.']
            for i in range(h-len(stack)):
                board[i][j] = '.'
            for i,c in enumerate(stack):
                board[h-len(stack)+i][j] = c
    return board

def simulate(board,r,c,r2,c2):
    b = [row[:] for row in board]
    b[r][c],b[r2][c2] = b[r2][c2],b[r][c]
    b = erase_and_drop(b)
    return all(all(cell == '.' for cell in row) for row in b)

for i in range(h):
    for j in range(w-1):
        if field[i][j] != '.' or field[i][j+1] != '.':
            if simulate(field,i,j,i,j+1):
                print("YES")
                exit()
for i in range(h-1):
    for j in range(w):
        if field[i][j] != '.' or field[i+1][j] != '.':
            if simulate(field,i,j,i+1,j):
                print("YES")
                exit()
print("NO")