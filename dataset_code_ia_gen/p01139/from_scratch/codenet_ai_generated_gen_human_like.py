import sys
sys.setrecursionlimit(10**7)

def inside(x, y, w, h):
    return 0 <= x < w and 0 <= y < h

def dfs_expand_adjacent(x, y, w, h, grid, adj_set, target_h):
    # target_h: 'B' or 'W'
    stack = [(x, y)]
    adj_set.add((x, y))
    while stack:
        cx, cy = stack.pop()
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = cx+dx, cy+dy
            if inside(nx, ny, w, h) and grid[ny][nx] == '.' and (nx, ny) not in adj_set:
                # check if adjacent to target_h
                # but we added only the connected empty cells adjacent to target_h in the initial DFS
                adj_set.add((nx, ny))
                stack.append((nx, ny))

def find_expand_adjacent_cells(w,h,grid,target_h):
    # find all cells that are "expanded adjacent" to target_h
    adj_set = set()
    # first find all empty cells adjacent to target_h
    for y in range(h):
        for x in range(w):
            if grid[y][x]=='.':
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx, ny = x+dx, y+dy
                    if inside(nx, ny, w, h) and grid[ny][nx]==target_h:
                        adj_set.add((x,y))
                        break
    # then expand recursively those adjacent cells (their neighbors empty cells)
    # BFS/DFS over adj_set area
    # Actually, the above collects the start points for recursion.
    # We run DFS covering all connected '.' cells connected to these starting points.
    # Use BFS/DFS to expand
    total_adj = set(adj_set)
    stack = list(adj_set)
    while stack:
        cx, cy = stack.pop()
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = cx+dx, cy+dy
            if inside(nx, ny, w, h) and grid[ny][nx]=='.' and (nx, ny) not in total_adj:
                total_adj.add((nx, ny))
                stack.append((nx, ny))
    return total_adj

def has_adjacent_to_other_pile(x,y,w,h,grid,other_h):
    # check if cell (x,y) adjacent to a cell with pile other_h ('B' or 'W')
    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx, ny = x+dx, y+dy
        if inside(nx, ny, w, h) and grid[ny][nx]==other_h:
            return True
    return False

def main():
    input_iter = iter(sys.stdin.read().strip().split('\n'))
    while True:
        line = next(input_iter)
        if not line:
            continue
        w, h = map(int,line.split())
        if w==0 and h==0:
            break
        grid = []
        for _ in range(h):
            row = next(input_iter)
            grid.append(list(row))

        black_adj = find_expand_adjacent_cells(w,h,grid,'B')
        white_adj = find_expand_adjacent_cells(w,h,grid,'W')

        black_count = 0
        white_count = 0

        for y in range(h):
            for x in range(w):
                c = grid[y][x]
                if c in ('B','W'):
                    # these are piles, not land cells
                    continue
                in_black = (x,y) in black_adj
                in_white = (x,y) in white_adj
                if in_black and not has_adjacent_to_other_pile(x,y,w,h,grid,'W'):
                    # enclosed by black piles
                    black_count += 1
                if in_white and not has_adjacent_to_other_pile(x,y,w,h,grid,'B'):
                    # enclosed by white piles
                    white_count += 1
        print(black_count, white_count)

if __name__ == '__main__':
    main()