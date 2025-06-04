num_steps = int(input())
dp_table = [[0] * (num_steps + 1) for row_idx in range(num_steps + 1)]
dp_table[0][0] = 1
modulo_const = 10 ** 9 + 7

for step_idx in range(num_steps):
    step_type = input()
    for level_idx in range(step_idx + 1):
        current_value = dp_table[step_idx][level_idx]
        if step_type == "-":
            next_level = level_idx
            dp_table[step_idx + 1][next_level] = (dp_table[step_idx + 1][next_level] + current_value) % modulo_const
        elif step_type == "U":
            next_level = level_idx + 1
            dp_table[step_idx + 1][next_level] = (dp_table[step_idx + 1][next_level] + current_value) % modulo_const

            next_level = level_idx
            multiplier = level_idx
            dp_table[step_idx + 1][next_level] = (dp_table[step_idx + 1][next_level] + current_value * multiplier) % modulo_const
        elif step_type == "D":
            next_level = level_idx
            multiplier = level_idx
            dp_table[step_idx + 1][next_level] = (dp_table[step_idx + 1][next_level] + current_value * multiplier) % modulo_const

            if next_level == 0:
                continue
            next_level = level_idx - 1
            multiplier = level_idx * level_idx
            dp_table[step_idx + 1][next_level] = (dp_table[step_idx + 1][next_level] + current_value * multiplier) % modulo_const

print(dp_table[num_steps][0])