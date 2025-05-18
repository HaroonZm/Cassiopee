# python template for atcoder1
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def solve():
    grid_wid, grid_hei, t, p = map(int, input().split())
    if grid_wid == 0:
        exit()
    grid = [[1]*grid_wid for _ in range(grid_hei)]

    fold = [list(map(int, input().split())) for _ in range(t)]
    pin = [list(map(int, input().split())) for _ in range(p)]

    # 区間の左端と右端[L,R)
    L = 0
    R = grid_wid
    # 区間の下端と上端[B,H)
    B = 0
    H = grid_hei

    for ope, axis in fold:
        if ope == 1:
            # 横におる
            current_width = R-L
            if axis > current_width/2:  # kaiten
                alter_axis = current_width-axis
                for i in range(alter_axis):
                    for j in range(grid_hei):
                        grid[j][axis-i-1+L] += grid[j][axis+i+L]
                        grid[j][axis+i+L] = 0

                # 回転させる
                for j in range(grid_hei):
                    grid[j] = list(reversed(grid[j]))
                # 区間の更新
                L, R = grid_wid-R+alter_axis, grid_wid-L

            else:
                for i in range(axis):
                    for j in range(grid_hei):
                        grid[j][axis+i+L] += grid[j][axis-i-1+L]
                        grid[j][axis-i-1+L] = 0
                L += axis

        if ope == 2:
            # 縦におる
            current_hei = H-B
            if axis > current_hei/2:  # kaiten
                alter_axis = current_hei-axis
                for i in range(alter_axis):
                    for j in range(grid_wid):
                        grid[axis-i-1+B][j] += grid[axis+B+i][j]
                        grid[axis+i+B][j] = 0

                # 回転させる
                grid = list(reversed(grid))
                # 区間の更新
                B, H = grid_hei-H+alter_axis, grid_hei-B
            else:
                for i in range(axis):
                    for j in range(grid_wid):
                        grid[axis+i+B][j] += grid[axis-i-1+B][j]
                        grid[axis-i-1+B][j] = 0
                B += axis
    for px, py in pin:
        ans = grid[B+py][L+px]
        print(ans)

while True:
    solve()