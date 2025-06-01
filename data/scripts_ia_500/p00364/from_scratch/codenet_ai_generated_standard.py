N, t = map(int, input().split())
buildings = [tuple(map(int, input().split())) for _ in range(N)]
max_height = 0.0
for x, h in buildings:
    slope = h / (t - x)
    max_height = max(max_height, slope * t)
print(f"{max_height:.6f}")