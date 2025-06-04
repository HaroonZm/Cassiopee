num_steps, start_value, lower_bound, step_min, step_max = map(int, input().split())

step_sum = step_min + step_max
for index in range(num_steps):
    current_min = start_value + (num_steps - 1) * step_min - step_sum * index
    current_max = start_value + (num_steps - 1) * step_max - step_sum * index
    if current_min <= lower_bound <= current_max:
        print("YES")
        exit()
print("NO")