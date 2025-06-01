W, H, N = map(int, input().split())
spots = [tuple(map(int, input().split())) for _ in range(N)]

total_distance = 0
for i in range(N - 1):
    x1, y1 = spots[i]
    x2, y2 = spots[i+1]
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    # On peut se déplacer diagonalement → la distance minimale est max(dx, dy)
    total_distance += max(dx, dy)

print(total_distance)