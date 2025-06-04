input_value = int(input())
current_total = 0
step_count = 0
while True:
    step_count += 1
    current_total += input_value
    if current_total % 360 == 0:
        print(step_count)
        exit()