dp_array = [1.0] + [0.0] * 1000
input_total_steps, input_max_jump = map(int, input().split())
for current_step in range(input_total_steps):
    jump_distance = 1
    while (current_step + jump_distance) <= input_total_steps and jump_distance <= input_max_jump:
        dp_array[current_step + jump_distance] += dp_array[current_step] / (input_total_steps - current_step)
        jump_distance += 1
print('%.10f' % dp_array[input_total_steps])