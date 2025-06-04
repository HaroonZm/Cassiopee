number_of_steps = int(input())

color_sequence = [int(input()) for _ in range(number_of_steps)]

ways_to_reach_step = [0 for _ in range(number_of_steps)]
ways_to_reach_step[0] = 1

MODULO = 10**9 + 7

next_occurrence_of_color = [-1 for _ in range(number_of_steps)]
last_position_of_color = [-1 for _ in range(max(color_sequence) + 1)]

for current_position in range(number_of_steps):
    current_color = color_sequence[current_position]
    if (
        last_position_of_color[current_color] != -1
        and last_position_of_color[current_color] + 1 != current_position
    ):
        previous_position = last_position_of_color[current_color]
        next_occurrence_of_color[previous_position] = current_position
    last_position_of_color[current_color] = current_position

for step_index in range(number_of_steps - 1):
    if next_occurrence_of_color[step_index] != -1:
        next_position = next_occurrence_of_color[step_index]
        ways_to_reach_step[next_position] += ways_to_reach_step[step_index]
        ways_to_reach_step[next_position] %= MODULO
    ways_to_reach_step[step_index + 1] += ways_to_reach_step[step_index]
    ways_to_reach_step[step_index + 1] %= MODULO

print(ways_to_reach_step[number_of_steps - 1] % MODULO)