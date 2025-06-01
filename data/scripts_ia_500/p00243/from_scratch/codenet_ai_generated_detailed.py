from collections import deque
import sys

def flood_fill(grid, x, y, new_color):
    """
    グリッドの左上セル(0,0)に対して、元の色と同じ隣接セルを
    new_colorに一斉に塗りつぶす処理を行う。
    """
    original_color = grid[0][0]
    if original_color == new_color:
        return  # 色が同じなら何もしない

    w, h = x, y
    visited = [[False]*w for _ in range(h)]
    queue = deque()
    queue.append((0,0))
    visited[0][0] = True

    while queue:
        cx, cy = queue.popleft()
        # 色を変更
        grid[cy][cx] = new_color
        # 隣接セル(上下左右)をチェック
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = cx+dx, cy+dy
            if 0 <= nx < w and 0 <= ny < h:
                if not visited[ny][nx] and grid[ny][nx] == original_color:
                    visited[ny][nx] = True
                    queue.append((nx, ny))

def is_one_color(grid):
    """
    グリッドがすべて同じ色か判定
    """
    first_color = grid[0][0]
    for row in grid:
        for c in row:
            if c != first_color:
                return False
    return True

def solve_puzzle(x, y, grid):
    """
    BFSで各状態を探索し、最短手順でグリッド全体を同色に塗りつぶす手順回数を返す。
    """
    colors = ['R','G','B']

    # 状態の記録用にグリッドを文字列に変換
    def grid_to_str(g):
        return ''.join(''.join(row) for row in g)

    start_state = grid_to_str(grid)
    if is_one_color(grid):
        return 0  # 最初から同色なら0回

    queue = deque()
    queue.append((grid, 0))
    visited = set()
    visited.add(start_state)

    while queue:
        current_grid, step = queue.popleft()
        # 現在の左上色
        current_color = current_grid[0][0]
        for new_color in colors:
            if new_color == current_color:
                # 同じ色のボタンを押しても変化なしなのでスキップ
                continue
            # 状態をコピーして塗りつぶし
            new_grid = [row[:] for row in current_grid]
            flood_fill(new_grid, x, y, new_color)
            new_state = grid_to_str(new_grid)
            if new_state not in visited:
                if is_one_color(new_grid):
                    return step + 1
                visited.add(new_state)
                queue.append((new_grid, step + 1))
    # 不可能なケースはないはずだが念のため
    return -1

def main():
    input = sys.stdin.readline
    while True:
        line = ''
        while line.strip() == '':
            line = input()
            if not line:
                return
        x,y = map(int,line.strip().split())
        if x == 0 and y == 0:
            break
        grid = []
        for _ in range(y):
            row = input().strip().split()
            grid.append(row)
        ans = solve_puzzle(x, y, grid)
        print(ans)

if __name__ == "__main__":
    main()