while True:
    line = ''
    while line.strip() == '':
        line = input()
    m, n = map(int, line.strip().split())
    if m == 0 and n == 0:
        break
    x, y = 1, 1
    # directions: 0-North,1-East,2-South,3-West
    direction = 0
    while True:
        cmd_line = ''
        while cmd_line.strip() == '':
            cmd_line = input()
        parts = cmd_line.strip().split()
        cmd = parts[0]
        if cmd == 'STOP':
            print(x, y)
            break
        if cmd == 'RIGHT':
            direction = (direction + 1) % 4
        elif cmd == 'LEFT':
            direction = (direction - 1) % 4
        else:
            k = int(parts[1])
            dx, dy = 0, 0
            if direction == 0:
                dx, dy = 0, 1
            elif direction == 1:
                dx, dy = 1, 0
            elif direction == 2:
                dx, dy = 0, -1
            else:
                dx, dy = -1, 0
            if cmd == 'FORWARD':
                for _ in range(k):
                    nx, ny = x + dx, y + dy
                    if nx < 1 or nx > m or ny < 1 or ny > n:
                        break
                    x, y = nx, ny
            elif cmd == 'BACKWARD':
                for _ in range(k):
                    nx, ny = x - dx, y - dy
                    if nx < 1 or nx > m or ny < 1 or ny > n:
                        break
                    x, y = nx, ny