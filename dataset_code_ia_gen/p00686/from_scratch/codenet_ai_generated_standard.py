def main():
    directions = ['N', 'E', 'S', 'W']
    move = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
    while True:
        line = ''
        while line.strip() == '':
            line = input()
        m, n = map(int, line.strip().split())
        if m == 0 and n == 0:
            break
        x, y = 1, 1
        facing = 0  # 0:N,1:E,2:S,3:W
        while True:
            cmd = input().strip()
            if not cmd:
                continue
            parts = cmd.split()
            c = parts[0]
            if c == 'STOP':
                print(x, y)
                break
            elif c == 'RIGHT':
                facing = (facing + 1) % 4
            elif c == 'LEFT':
                facing = (facing - 1) % 4
            else:
                k = int(parts[1])
                dx, dy = move[directions[facing]]
                if c == 'BACKWARD':
                    dx, dy = -dx, -dy
                for _ in range(k):
                    nx, ny = x + dx, y + dy
                    if nx < 1 or nx > m or ny < 1 or ny > n:
                        break
                    x, y = nx, ny

main()