import sys
sys.setrecursionlimit(10**7)

def input():
    return sys.stdin.readline()

def line_puzzle(n, grid, starts):
    used = [[False]*n for _ in range(n)]
    dxy = [(0,1),(0,-1),(1,0),(-1,0)]
    start_positions = starts

    # pre-mark start points as used
    for (x,y,_) in start_positions:
        used[x][y] = True

    def get_paths(sx, sy, target):
        paths = []
        for dx,dy in dxy:
            path = []
            cx, cy = sx, sy
            s = 0
            while True:
                cx += dx
                cy += dy
                if not (0 <= cx < n and 0 <= cy < n):
                    break
                if used[cx][cy]:
                    break
                s += grid[cx][cy]
                path.append((cx,cy))
                if s == target:
                    paths.append(path[:])
                    break
                if s > target:
                    break
        return paths

    mem = {}
    def backtrack(i):
        if i == len(start_positions):
            for x in range(n):
                for y in range(n):
                    if not used[x][y]:
                        return False
            return True
        sx, sy, val = start_positions[i]
        if (i, tuple(map(tuple, used))) in mem:
            return False
        paths = get_paths(sx, sy, -val)
        for path in paths:
            # check if path crosses another start point (other than current)
            invalid = False
            for (px, py) in path:
                if grid[px][py] < 0:
                    invalid = True
                    break
            if invalid:
                continue
            # mark path used
            for (px, py) in path:
                used[px][py] = True
            if backtrack(i+1):
                return True
            for (px, py) in path:
                used[px][py] = False
        mem[(i, tuple(map(tuple, used)))] = False
        return False

    return backtrack(0)

def main():
    while True:
        n = int(sys.stdin.readline())
        if n == 0:
            break
        grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
        starts = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] < 0:
                    starts.append((i,j,grid[i][j]))
        starts.sort()
        print("YES" if line_puzzle(n, grid, starts) else "NO")

if __name__ == "__main__":
    main()