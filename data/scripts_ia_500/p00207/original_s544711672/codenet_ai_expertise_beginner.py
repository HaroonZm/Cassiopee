import sys

def occupation_point(block):
    x = block['x']
    y = block['y']
    directions = [(0, 0), (1, 0), (0, 1), (1, 1)]
    points = []
    for dx, dy in directions:
        points.append((x + dx, y + dy))
    if block['direction'] == 1:
        y = y + 2
    else:
        x = x + 2
    for dx, dy in directions:
        points.append((x + dx, y + dy))
    return points

def paintout(board, start, value):
    color = board[start[1]][start[0]]
    if color == 0:
        return
    stack = [start]
    while stack:
        x, y = stack.pop()
        if board[y][x] == color:
            board[y][x] = value
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx = x + dx
                ny = y + dy
                if 0 <= ny < len(board) and 0 <= nx < len(board[0]):
                    stack.append((nx, ny))

def is_reachable(size, start, goal, blocks):
    w = size['x'] + 2
    h = size['y'] + 2
    board = [[0 for _ in range(w)] for _ in range(h)]

    for b in blocks:
        for x, y in occupation_point(b):
            board[y][x] = b['color']

    paintout(board, start, -1)
    return board[goal['y']][goal['x']] == -1

def main():
    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        x, y = map(int, line.split())
        if x == 0:
            break
        size = {'x': x, 'y': y}
        sx, sy = map(int, input().split())
        start = (sx, sy)
        gx, gy = map(int, input().split())
        goal = {'x': gx, 'y': gy}
        n = int(input())
        blocks = []
        for _ in range(n):
            c, d, bx, by = map(int, input().split())
            blocks.append({'color': c, 'direction': d, 'x': bx, 'y': by})
        if is_reachable(size, start, goal, blocks):
            print('OK')
        else:
            print('NG')

if __name__ == '__main__':
    main()