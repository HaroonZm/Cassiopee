def calculate_minimum_steps(target_velocity):
    current_step = 1
    gravity_constant = 4.9
    while True:
        vertical_displacement = 5 * current_step - 5
        expected_velocity = 2 * gravity_constant * (vertical_displacement / gravity_constant) ** 0.5
        if expected_velocity >= target_velocity:
            return current_step
        else:
            current_step += 1

while True:
    try:
        input_velocity = float(input())
        print(calculate_minimum_steps(input_velocity))
    except EOFError:
        break