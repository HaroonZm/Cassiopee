input_time = int(input())

step_count = 0
current_speed = 1
speed_margin = 0

while input_time > 0:
    input_time -= current_speed
    step_count += 1
    if speed_margin + current_speed * 3 <= input_time:
        current_speed *= 3
        speed_margin += current_speed
    elif input_time < speed_margin:
        speed_margin -= current_speed
        current_speed /= 3

print(step_count)