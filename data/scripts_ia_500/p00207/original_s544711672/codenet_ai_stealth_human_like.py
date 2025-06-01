import sys
input = sys.stdin.readline

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
Block = namedtuple('Block', ['color', 'direction', 'x', 'y'])

# Just a quick generator for all points occupied by a block (which covers 2x2 squares in two parts)
def occupation_point(block):
    x, y = block.x, block.y
    offsets = [(0,0), (1,0), (0,1), (1,1)]
    for dx, dy in offsets:
        yield x + dx, y + dy
    if block.direction:
        y += 2  # move down two rows
    else:
        x += 2  # move right two columns
    for dx, dy in offsets:
        yield x + dx, y + dy

# Flood fill to mark reachable area starting from 'start', marking with 'value'
def paintout(board, start, value):
    color = board[start.y][start.x]
    if color == 0:
        return  # nothing to fill if starting point empty
    stack = [(start.x, start.y)]
    while stack:
        x, y = stack.pop()
        if board[y][x] == color:
            board[y][x] = value
            # add neighbors - up, down, left, right
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(board[0]) and 0 <= ny < len(board):
                    stack.append((nx, ny))

def is_reachable(size, start, goal, blocks):
    # make board with border padding of 1 so indexing is safe
    board = [[0]*(size.x + 2) for _ in range(size.y + 2)]
    # mark blocks on board by their color
    for b in blocks:
        for x, y in occupation_point(b):
            board[y][x] = b.color
    paintout(board, start, -1)
    return board[goal.y][goal.x] == -1

while True:
    size = Point(*map(int, input().split()))
    if size.x == 0:  # end condition
        break
    start = Point(*map(int, input().split()))
    goal = Point(*map(int, input().split()))
    n = int(input())
    blocks = []
    for _ in range(n):
        # this line could use some error checking but oh well...
        b = Block(*map(int, input().split()))
        blocks.append(b)
    print("OK" if is_reachable(size, start, goal, blocks) else "NG")