from collections import deque
import sys

# 指定された色で flood fill を行う関数
def flood_fill(grid, x, y, new_color):
    # 元の色
    original_color = grid[y][x]
    if original_color == new_color:
        return grid  # 変更不要の場合はそのまま返す
    
    # コピーを作成して元のgridを変更しないようにする
    new_grid = [row[:] for row in grid]
    
    queue = deque()
    queue.append((x, y))
    new_grid[y][x] = new_color
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            # 範囲内かつ元の色と一致する場合
            if 0 <= nx < len(new_grid[0]) and 0 <= ny < len(new_grid):
                if new_grid[ny][nx] == original_color:
                    new_grid[ny][nx] = new_color
                    queue.append((nx, ny))
    return new_grid

# グリッドがすべて同じ色かどうか判定
def is_uniform(grid):
    first_color = grid[0][0]
    for row in grid:
        for c in row:
            if c != first_color:
                return False
    return True

# BFSで最短手順を探索する
def bfs_min_steps(grid):
    # 各ノードはグリッドの状態、手数
    start = tuple(tuple(row) for row in grid)  # 状態はイミュータブルにして管理
    queue = deque()
    queue.append( (start,0) )
    visited = set()
    visited.add(start)
    
    colors = ['R','G','B']
    while queue:
        state, step = queue.popleft()
        # すべて同じ色なら終了
        if len(set(c for row in state for c in row)) == 1:
            return step
        # 現在左上の色
        current_color = state[0][0]
        # 各色を試す
        for color in colors:
            if color == current_color:
                # 同じ色に変える意味はないのでスキップ
                continue
            # flood fillをシミュレーション
            grid_list = [list(row) for row in state]
            new_grid = flood_fill(grid_list,0,0,color)
            # 新状態作成
            new_state = tuple(tuple(row) for row in new_grid)
            if new_state not in visited:
                visited.add(new_state)
                queue.append( (new_state, step+1) )
    # 理論上ここに来ることはない（必ず解けるはず）
    return -1

def main():
    input = sys.stdin.readline
    while True:
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
            if line == '':
                return
        X, Y = map(int, line.strip().split())
        if X == 0 and Y == 0:
            break
        grid = []
        for _ in range(Y):
            row = sys.stdin.readline().strip().split()
            grid.append(row)
        # 最短手数を求めて出力
        ans = bfs_min_steps(grid)
        print(ans)

if __name__ == "__main__":
    main()