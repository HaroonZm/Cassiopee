def trajectory_calc_y(velocity_y, time_elapsed):
    return velocity_y * time_elapsed - GRAVITY / 2 * time_elapsed * time_elapsed

def interval_compare(lower_bound, upper_bound, value):
    if value < lower_bound + EPSILON:
        return -1
    elif value > upper_bound - EPSILON:
        return 1
    return 0

def trajectory_check(target_x, target_y):
    if target_x == 0:
        return 0
    coeff_a = GRAVITY * GRAVITY / 4
    coeff_b = target_y * GRAVITY - VELOCITY * VELOCITY
    coeff_c = target_x * target_x + target_y * target_y
    discriminant = coeff_b * coeff_b - 4 * coeff_a * coeff_c
    if discriminant < -EPSILON:
        return 0
    if -EPSILON <= discriminant < 0:
        discriminant = 0
    for direction in (-1, 1):
        solution_tt = (-coeff_b + direction * discriminant ** 0.5) / (2 * coeff_a)
        if solution_tt <= 0:
            continue
        total_time = solution_tt ** 0.5
        velocity_x = target_x / total_time
        velocity_y = target_y / total_time + GRAVITY * total_time / 2
        if trajectory_calc_y(velocity_y, TARGET_X / velocity_x) < TARGET_Y - EPSILON:
            return 0
        for obs_left, obs_bottom, obs_right, obs_top in OBSTACLE_LIST:
            compare_left = interval_compare(obs_bottom, obs_top, trajectory_calc_y(velocity_y, obs_left / velocity_x))
            compare_right = interval_compare(obs_bottom, obs_top, trajectory_calc_y(velocity_y, obs_right / velocity_x))
            compare_x_apex = interval_compare(obs_left, obs_right, velocity_x * (velocity_y / GRAVITY))
            compare_y_apex = interval_compare(obs_bottom, obs_top, trajectory_calc_y(velocity_y, velocity_y / GRAVITY))
            if compare_left * compare_right <= 0 or (not compare_x_apex and compare_y_apex * compare_left <= 0):
                break
        else:
            return 1
    return 0

GRAVITY = 9.8
EPSILON = 1e-10

NUM_OBSTACLES, VELOCITY, TARGET_X, TARGET_Y = map(int, input().split())
OBSTACLE_LIST = []
for obstacle_index in range(NUM_OBSTACLES):
    input_left, input_bottom, input_right, input_top = map(int, input().split())
    if input_left < TARGET_X:
        OBSTACLE_LIST.append((input_left, input_bottom, min(input_right, TARGET_X), input_top))

if trajectory_check(TARGET_X, TARGET_Y):
    print('Yes')
    exit()
for obs_left, obs_bottom, obs_right, obs_top in OBSTACLE_LIST:
    if not obs_left or not obs_right:
        continue
    if trajectory_check(obs_left, obs_top) or trajectory_check(obs_right, obs_top):
        print('Yes')
        exit()
print('No')