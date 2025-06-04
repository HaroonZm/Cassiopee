total_time, max_distance = map(int, input().split())
time_a, time_b = map(int, input().split())
dist_step_a, dist_step_b = map(int, input().split())

min_time_difference = min(
    [
        abs(
            total_time - (time_a * distance_a + time_b * distance_b) / (distance_a + distance_b)
        )
        for distance_a in range(0, max_distance + 1, dist_step_a)
        for distance_b in range(0, max_distance + 1, dist_step_b)
        if 1 <= distance_a + distance_b <= max_distance
    ]
)

print(min_time_difference)