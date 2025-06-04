import sys

def solve(field):
    BLANK = 0
    OBSTACLE = 1
    JUMP = 2

    from collections import deque

    dx = [0, -1, 1]
    x_limit = len(field[0])
    y_limit = len(field)

    path = {}
    queue = deque()
    ans = 0

    for x in range(x_limit):
        if field[0][x] == BLANK:
            key = (x, 0)
            queue.append(key)
            path[key] = 1

    while queue:
        cx, cy = queue.popleft()
        num = path[(cx, cy)]
        del path[(cx, cy)]

        if field[cy][cx] == OBSTACLE:
            continue
        elif field[cy][cx] == JUMP:
            if cy + 2 > y_limit - 1:
                ans += num
            else:
                next_key = (cx, cy + 2)
                if next_key not in path:
                    queue.append(next_key)
                    path[next_key] = 0
                path[next_key] += num
            continue
        elif cy == y_limit - 1:
            ans += num
            continue

        for i in range(3):
            nx = cx + dx[i]
            ny = cy + 1
            if 0 <= nx < x_limit:
                if field[ny][nx] == JUMP and dx[i] == 0:
                    if ny + 2 > y_limit - 1:
                        ans += num
                    else:
                        jump_key = (nx, ny + 2)
                        if jump_key not in path:
                            queue.append(jump_key)
                            path[jump_key] = 0
                        path[jump_key] += num
                elif field[ny][nx] == BLANK:
                    if ny >= y_limit - 1:
                        ans += num
                    else:
                        blank_key = (nx, ny)
                        if blank_key not in path:
                            queue.append(blank_key)
                            path[blank_key] = 0
                        path[blank_key] += num
    return ans

def main():
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        X_Y = line.strip().split()
        if not X_Y:
            continue
        X, Y = map(int, X_Y)
        if X == 0 and Y == 0:
            break
        field = []
        for _ in range(Y):
            row = sys.stdin.readline().strip().split()
            field.append([int(cell) for cell in row])
        print(solve(field))

if __name__ == '__main__':
    main()