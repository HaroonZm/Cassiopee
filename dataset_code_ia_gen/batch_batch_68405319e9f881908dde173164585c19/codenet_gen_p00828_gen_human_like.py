def main():
    directions = [
        (1,0,0), (0,1,0), (0,0,1),
        (1,1,0), (1,-1,0), (1,0,1), (1,0,-1), (0,1,1), (0,1,-1),
        (1,1,1), (1,1,-1), (1,-1,1), (1,-1,-1)
    ]

    while True:
        n,m,p = map(int, input().split())
        if n==0 and m==0 and p==0:
            break

        board = [[[None for _ in range(n)] for _ in range(n)] for _ in range(n)]  # board[x][y][z]
        heights = [[0]*n for _ in range(n)]
        winner = None
        win_move = 0

        def valid_pos(x,y,z):
            return 0<=x<n and 0<=y<n and 0<=z<n

        def check_win(x,y,z):
            color = board[x][y][z]
            for dx,dy,dz in directions:
                count = 1
                # forward
                nx, ny, nz = x+dx, y+dy, z+dz
                while valid_pos(nx, ny, nz) and board[nx][ny][nz]==color:
                    count += 1
                    nx += dx
                    ny += dy
                    nz += dz
                # backward
                nx, ny, nz = x-dx, y-dy, z-dz
                while valid_pos(nx, ny, nz) and board[nx][ny][nz]==color:
                    count += 1
                    nx -= dx
                    ny -= dy
                    nz -= dz
                if count >= m:
                    return True
            return False

        for i in range(p):
            x,y = map(int,input().split())
            x -= 1
            y -= 1
            if winner is not None:
                continue
            z = heights[x][y]
            board[x][y][z] = "Black" if i%2==0 else "White"
            heights[x][y] += 1
            if check_win(x,y,z):
                winner = board[x][y][z]
                win_move = i+1

        if winner:
            print(winner,win_move)
        else:
            print("Draw")

if __name__=="__main__":
    main()