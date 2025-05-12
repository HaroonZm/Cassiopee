from sys import stdin
readline = stdin.readline

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
Block = namedtuple('Block', ['color', 'direction', 'x', 'y'])

def occupation_point(block):
    x, y = block.x, block.y
    d = [(0, 0), (1, 0), (0, 1), (1, 1)]
    for dx, dy in d:
        yield x + dx, y + dy
    if block.direction:
        y += 2
    else:
        x += 2
    for dx, dy in d:
        yield x + dx, y + dy

def paintout(board, start, value):
    color = board[start.y][start.x]
    if color == 0:
        return
    que =[(start.x, start.y)]
    while que:
        x,y = que.pop()
        if board[y][x] == color:
            board[y][x] = value
            que.extend([(x + dx, y + dy) for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]])

def is_reachable(size, start, goal, blocks):
    board = [[0] * (size.x + 2) for _ in range(size.y + 2)]
    for bi in blocks:
        for x, y in occupation_point(bi):
            board[y][x] = bi.color
    paintout(board, start, -1)
    return board[goal.y][goal.x] == -1

while True:
    size = Point(*map(int, readline().split()))
    if size.x == 0:
        break
    start = Point(*map(int, readline().split()))
    goal = Point(*map(int, readline().split()))
    blocks = []
    for _ in range(int(readline())):
        blocks.append(Block(*map(int, readline().split())))
    print('OK' if is_reachable(size, start, goal, blocks) else 'NG')