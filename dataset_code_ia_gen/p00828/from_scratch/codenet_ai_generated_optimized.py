def main():
    import sys
    input = sys.stdin.readline

    directions = [(1,0,0), (0,1,0), (0,0,1),
                  (1,1,0), (1,-1,0), (1,0,1), (1,0,-1), (0,1,1), (0,1,-1),
                  (1,1,1), (1,1,-1), (1,-1,1), (1,-1,-1)]

    while True:
        n,m,p = map(int,input().split())
        if n == 0 and m == 0 and p == 0:
            break
        # board[x][y] = height of stack (z count)
        board = [[[0]*n for _ in range(n)] for _ in range(n)]
        heights = [[0]*n for _ in range(n)]
        winner = None
        win_move = 0

        # Store each ball: color by number, 1=Black, 2=White
        # We'll store color on board[x][y][z]
        def in_range(x,y,z):
            return 0 <= x < n and 0 <= y < n and 0 <= z < n

        # Check if placing at (x,y,z) wins for color
        def check_win(x,y,z,color):
            for dx,dy,dz in directions:
                count = 1
                # Forward
                nx, ny, nz = x+dx, y+dy, z+dz
                while in_range(nx,ny,nz) and board[nx][ny][nz] == color:
                    count +=1
                    nx += dx
                    ny += dy
                    nz += dz
                # Backward
                nx, ny, nz = x-dx, y-dy, z-dz
                while in_range(nx,ny,nz) and board[nx][ny][nz] == color:
                    count +=1
                    nx -= dx
                    ny -= dy
                    nz -= dz
                if count >= m:
                    return True
            return False

        for move_num in range(1,p+1):
            x,y = map(int,input().split())
            x-=1
            y-=1
            if heights[x][y]<n:
                z = heights[x][y]
                if winner is None:
                    color = 1 if move_num%2==1 else 2
                    board[x][y][z] = color
                    heights[x][y]+=1
                    if check_win(x,y,z,color):
                        winner = color
                        win_move = move_num
                else:
                    # After game ended, ignore moves
                    pass

        if winner is None:
            print("Draw")
        else:
            print(("Black" if winner==1 else "White") + " " + str(win_move))

if __name__=="__main__":
    main()