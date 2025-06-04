input_sequence = list(input())
target_x, target_y = map(int, input().split())
current_state = "INIT"
forward_steps_group = []
x_axis_steps = [0]
y_axis_steps = [0]

step_count = 0
for idx in range(len(input_sequence)):
    if current_state == "INIT":
        if input_sequence[idx] == "F":
            step_count += 1
        else:
            forward_steps_group.append(step_count)
            step_count = 0
            current_state = "Y_AXIS"
    elif current_state == "X_AXIS":
        if input_sequence[idx] == "F":
            step_count += 1
        else:
            x_axis_steps.append(step_count)
            step_count = 0
            current_state = "Y_AXIS"
    else:
        if input_sequence[idx] == "F":
            step_count += 1
        else:
            y_axis_steps.append(step_count)
            step_count = 0
            current_state = "X_AXIS"
if current_state == "INIT":
    forward_steps_group.append(step_count)
elif current_state == "X_AXIS":
    x_axis_steps.append(step_count)
else:
    y_axis_steps.append(step_count)

reachable_x_positions = {}
reachable_x_positions[0] = True
temp_x_positions = {}
for segment in x_axis_steps:
    for pos in reachable_x_positions:
        temp_x_positions[pos + segment] = True
        temp_x_positions[pos - segment] = True
    reachable_x_positions = temp_x_positions
    temp_x_positions = {}

if (target_x - forward_steps_group[0]) in reachable_x_positions:
    is_x_reachable = True
else:
    is_x_reachable = False

reachable_y_positions = {}
reachable_y_positions[0] = True
temp_y_positions = {}
for segment in y_axis_steps:
    for pos in reachable_y_positions:
        temp_y_positions[pos + segment] = True
        temp_y_positions[pos - segment] = True
    reachable_y_positions = temp_y_positions
    temp_y_positions = {}

if target_y in reachable_y_positions:
    is_y_reachable = True
else:
    is_y_reachable = False

if is_x_reachable and is_y_reachable:
    print("Yes")
else:
    print("No")