W, H, N = map(int, input().split())
spots = [tuple(map(int, input().split())) for _ in range(N)]

total_steps = 0
for i in range(N - 1):
    x1, y1 = spots[i]
    x2, y2 = spots[i + 1]
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    # Distance is max of dx and dy because diagonal moves are allowed
    total_steps += max(dx, dy)

print(total_steps)