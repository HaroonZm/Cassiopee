import sys
sys.setrecursionlimit(10**7)

def dfs(grid, x, y, visited):
    # Directions: up, down, left, right
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    stack = [(x,y)]
    visited[x][y] = True
    while stack:
        cx, cy = stack.pop()
        for dx, dy in directions:
            nx, ny = cx+dx, cy+dy
            if 0 <= nx < 12 and 0 <= ny < 12:
                if not visited[nx][ny] and grid[nx][ny] == 1:
                    visited[nx][ny] = True
                    stack.append((nx, ny))

def count_islands(grid):
    visited = [[False]*12 for _ in range(12)]
    count = 0
    for i in range(12):
        for j in range(12):
            if grid[i][j] == 1 and not visited[i][j]:
                dfs(grid, i, j, visited)
                count += 1
    return count

def main():
    lines = []
    for line in sys.stdin:
        line = line.strip()
        if line == "" and lines:
            # 空行で区切られたデータセット終了時
            grid = [list(map(int, list(row))) for row in lines]
            print(count_islands(grid))
            lines = []
        elif line != "":
            lines.append(line)

    # 最終データセットが空行なしで終わる場合に備えて
    if lines:
        grid = [list(map(int, list(row))) for row in lines]
        print(count_islands(grid))

if __name__ == "__main__":
    main()