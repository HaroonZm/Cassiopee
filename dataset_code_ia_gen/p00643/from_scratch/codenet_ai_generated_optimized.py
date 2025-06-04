import sys
import heapq

input = sys.stdin.readline

# Dice faces ordering: [top, bottom, north, south, west, east]
# sum of opposite faces =7: top(1)-bottom(6), north(5)-south(2), west(4)-east(3)
# initial: top=1, south=2, east=3 => north=5, bottom=6, west=4
# Rolling updates faces according to direction

def roll(dice, direction):
    top, bottom, north, south, west, east = dice
    if direction == 0:  # north
        return (south, north, top, bottom, west, east)
    elif direction == 1:  # south
        return (north, south, bottom, top, west, east)
    elif direction == 2:  # west
        return (east, west, north, south, top, bottom)
    else:  # east
        return (west, east, north, south, bottom, top)

while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break

    grid = [list(map(int, input().split())) for _ in range(h)]
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())

    # Distances: 3D (y,x,dice_state)
    # dice_state can be represented by the 6 faces values, but to reduce memory,
    # we assign an index to each dice orientation; since dice orientation is huge,
    # we store dice faces to detect visited states.

    # To reduce state space, we store dice faces as a tuple of 6 numbers.

    # initial dice faces
    dice0 = (1,6,5,2,4,3)

    dist = {}
    # heap elements: (cost, y, x, dice_faces)
    heap = []
    heapq.heappush(heap, (0, sy, sx, dice0))
    dist[(sy, sx, dice0)] = 0

    dy = [-1,1,0,0]
    dx = [0,0,-1,1]

    res = -1
    while heap:
        cost, y, x, dice = heapq.heappop(heap)
        if (y, x) == (gy, gx):
            res = cost
            break
        if dist[(y, x, dice)] < cost:
            continue
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < h and 0 <= nx < w:
                ndice = roll(dice, d)
                bottom = ndice[1]
                ncost = cost + bottom * grid[ny][nx]
                state = (ny, nx, ndice)
                if state not in dist or dist[state] > ncost:
                    dist[state] = ncost
                    heapq.heappush(heap, (ncost, ny, nx, ndice))
    print(res)