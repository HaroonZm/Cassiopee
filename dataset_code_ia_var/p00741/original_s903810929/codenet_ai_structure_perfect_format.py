from collections import deque

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    areas = [list(map(int, input().split())) for _ in range(h)]
    move_positions = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1], [0, 1],
        [1, -1], [1, 0], [1, 1]
    ]
    count = 0
    queue = deque()
    for i in range(h):
        for j in range(w):
            start_position = [i, j]
            queue.append(start_position)
            has_island = False
            while queue:
                now_position = queue.popleft()
                x, y = now_position
                if areas[x][y] == 0:
                    continue
                has_island = True
                areas[x][y] = 0
                for move_position in move_positions:
                    nx = x + move_position[0]
                    ny = y + move_position[1]
                    if 0 <= nx < h and 0 <= ny < w:
                        queue.append([nx, ny])
            if has_island:
                count += 1
    print(count)