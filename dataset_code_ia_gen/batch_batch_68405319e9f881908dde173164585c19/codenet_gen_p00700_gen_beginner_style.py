n = int(input())
for _ in range(n):
    x, y = 0, 0
    max_dist = 0
    treasure_x = 0
    treasure_y = 0
    while True:
        dx, dy = map(int, input().split())
        if dx == 0 and dy == 0:
            break
        x += dx
        y += dy
        dist = (x*x + y*y)**0.5
        if dist > max_dist or (dist == max_dist and x > treasure_x):
            max_dist = dist
            treasure_x = x
            treasure_y = y
    print(treasure_x, treasure_y)