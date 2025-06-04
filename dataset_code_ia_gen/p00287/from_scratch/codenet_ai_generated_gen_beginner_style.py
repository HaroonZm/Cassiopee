W, H, M = map(int, input().split())
walls = []
for _ in range(M):
    px, py, qx, qy = map(int, input().split())
    walls.append((px, py, qx, qy))

Q = int(input())
queries = []
for _ in range(Q):
    sx, sy, gx, gy = map(int, input().split())
    queries.append((sx, sy, gx, gy))

def crosses_wall(x1, y1, x2, y2, wall):
    px, py, qx, qy = wall
    # Wall is vertical
    if px == qx:
        wx = px
        # Check if the segment crosses the vertical line wx
        # The path crosses the wall if x1 and x2 are on opposite sides of wx
        if (x1 - wx) * (x2 - wx) < 0:
            # Now check if the segment's y projection overlap with the wall segment y projection
            miny, maxy = min(py, qy), max(py, qy)
            # Find the y coordinate where path crosses wx
            # line from (x1,y1) to (x2,y2):
            # (y - y1) = (y2 - y1)/(x2 - x1)*(x - x1)
            if x2 != x1:
                cross_y = y1 + (y2 - y1) * (wx - x1) / (x2 - x1)
                if miny < cross_y < maxy:
                    return True
    else:
        # Wall is horizontal
        wy = py
        # Check if the segment crosses the horizontal line wy
        if (y1 - wy) * (y2 - wy) < 0:
            minx, maxx = min(px, qx), max(px, qx)
            if y2 != y1:
                cross_x = x1 + (x2 - x1) * (wy - y1) / (y2 - y1)
                if minx < cross_x < maxx:
                    return True
    return False

for sx, sy, gx, gy in queries:
    count = 0
    for wall in walls:
        if crosses_wall(sx, sy, gx, gy, wall):
            count += 1
    print(count)