import sys
from collections import deque
from itertools import product

def solve(data, w, h):
    WALL, EMPTY = 1, 0
    offsets = (
        [(-1, 0), (1, 0), (-1, -1), (0, -1), (-1, 1), (0, 1)],  # odd row (y % 2 == 1)
        [(-1, 0), (1, 0), (0, -1), (1, -1), (0, 1), (1, 1)]     # even row (y % 2 == 0)
    )

    invisible_area = set()
    visible_area = set()
    visited = set()

    for y, x in product(range(h), range(w)):
        if (x, y) in visited or data[y][x] == WALL:
            if data[y][x] == WALL:
                invisible_area.add((x, y))
            continue

        # BFS identifies a region and whether it's at the border (thus visible)
        queue = deque([(x, y)])
        region = {(x, y)}
        visited.add((x, y))
        is_visible = False

        while queue:
            cx, cy = queue.popleft()
            for dx, dy in offsets[cy % 2]:
                nx, ny = cx + dx, cy + dy
                if not (0 <= nx < w and 0 <= ny < h):
                    is_visible = True
                    continue
                if data[ny][nx] == EMPTY and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    region.add((nx, ny))
                    queue.append((nx, ny))
        (visible_area if is_visible else invisible_area).update(region)

    ans = 0
    for y, x in product(range(h), range(w)):
        if data[y][x] == WALL:
            neighbors = [(x + dx, y + dy) for dx, dy in offsets[y % 2]]
            ans += sum((nx, ny) not in invisible_area for nx, ny in neighbors)
    return ans

def main(_):
    w, h = map(int, sys.stdin.readline().split())
    data = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    print(solve(data, w, h))

if __name__ == '__main__':
    main(sys.argv[1:])