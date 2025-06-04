N = int(input())
houses = list(map(int, input().split()))

min_time = 10**9
for meet_point in range(min(houses), max(houses)+1):
    max_dist = 0
    for h in houses:
        dist = abs(h - meet_point)
        if dist > max_dist:
            max_dist = dist
    if max_dist < min_time:
        min_time = max_dist

print(min_time)