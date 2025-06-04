import sys

step_count = int(input())

prev_time, prev_x, prev_y = 0, 0, 0

for step_idx in range(step_count):
    curr_time, curr_x, curr_y = map(int, input().split())
    delta_x = abs(curr_x - prev_x)
    delta_y = abs(curr_y - prev_y)
    delta_time = curr_time - prev_time
    total_distance = delta_x + delta_y

    if (total_distance <= delta_time) and (delta_time % 2 == total_distance % 2):
        pass
    else:
        print("No")
        sys.exit()

    prev_time, prev_x, prev_y = curr_time, curr_x, curr_y

print("Yes")