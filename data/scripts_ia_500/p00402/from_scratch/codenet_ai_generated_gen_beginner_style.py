N = int(input())
positions = list(map(int, input().split()))

min_time = float('inf')

for meeting_point in range(min(positions), max(positions) + 1):
    max_dist = 0
    for p in positions:
        dist = abs(p - meeting_point)
        if dist > max_dist:
            max_dist = dist
    if max_dist < min_time:
        min_time = max_dist

print(min_time)