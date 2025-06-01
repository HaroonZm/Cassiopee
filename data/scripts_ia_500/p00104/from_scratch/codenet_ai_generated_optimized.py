import sys
sys.setrecursionlimit(10**7)

directions = {'>': (1, 0), '<': (-1, 0), '^': (0, -1), 'v': (0, 1)}

def solve():
    input = sys.stdin.readline
    while True:
        H, W = map(int, input().split())
        if H == 0 and W == 0:
            break
        grid = [input().rstrip('\n') for _ in range(H)]

        visited = [[0]*W for _ in range(H)]

        x, y = 0, 0
        while True:
            if visited[y][x] == 1:
                print("LOOP")
                break
            visited[y][x] = 1

            c = grid[y][x]
            if c == '.':
                print(x, y)
                break
            dx, dy = directions[c]
            x, y = x+dx, y+dy

solve()