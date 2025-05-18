from collections import deque
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    areas = [list(map(int, input().split())) for _ in range(h)]

    # print(areas)

    # 島の数を出す。
    # 島の定義は陸地続きであること。ただし、斜めもみて、陸だったらそれは島
    # 左上からスタートして、陸続きのものは飛ばす

    move_positions = [[-1, -1], [-1, 0], [-1, 1],
                      [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    count = 0
    queue = deque([])
    for i in range(h):
        for j in range(w):
            start_position = [i, j]
            queue.append(start_position)
            has_island = False
            while queue:
                now_position = queue.popleft()
                if areas[now_position[0]][now_position[1]] == 0:
                    continue
                has_island = True
                areas[now_position[0]][now_position[1]] = 0
                for move_position in move_positions:
                    next_position = [now_position[0] + move_position[0],
                                     now_position[1] + move_position[1]]
                    if 0 <= next_position[0] and next_position[0] < h and 0 <= next_position[1] and next_position[1] < w:
                        queue.append(next_position)
            if has_island:
                count += 1
    print(count)