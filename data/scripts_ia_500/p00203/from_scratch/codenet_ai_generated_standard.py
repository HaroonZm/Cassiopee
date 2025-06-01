import sys
sys.setrecursionlimit(10**7)

def solve(X, Y, grid):
    from functools import lru_cache

    # 残りyがYを超えればゴール
    @lru_cache(None)
    def dfs(x, y):
        if y >= Y:
            return 1
        if x < 0 or x >= X or y < 0 or y >= Y:
            return 0
        if grid[y][x] == 1:
            return 0
        ans = 0
        if grid[y][x] == 2:
            # ジャンプ台：xは変わらずy+2へ
            if y + 2 <= Y:
                ans += dfs(x, y + 2)
        else:
            # 通常移動：x-1,y+1   x,y+1   x+1,y+1
            for nx in (x - 1, x, x + 1):
                ny = y + 1
                if 0 <= nx < X and ny < Y and grid[ny][nx] != 1:
                    # ジャンプ台に進入するなら、xは同じでないといけない
                    if grid[ny][nx] == 2 and nx != x:
                        continue
                    ans += dfs(nx, ny)
                elif ny >= Y:
                    # コースからはみ出る＝ゴール
                    ans += 1
        return ans

    total = 0
    # y=0は上端(問題のy=1に対応)
    for x in range(X):
        if grid[0][x] == 0:
            total += dfs(x, 0)
    return total

def main():
    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        X, Y = map(int, line.split())
        if X == 0 and Y == 0:
            break
        grid = [list(map(int, input().split())) for _ in range(Y)]
        print(solve(X,Y,grid))

if __name__ == '__main__':
    main()