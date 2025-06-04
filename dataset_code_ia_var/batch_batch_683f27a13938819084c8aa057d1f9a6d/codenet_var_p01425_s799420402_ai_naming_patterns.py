import math

GRAVITY_ACCELERATION = 9.8
EPSILON = 1e-6

def projectile_position(velocity_y, time_duration):
    return velocity_y * time_duration - GRAVITY_ACCELERATION * time_duration * time_duration / 2

def compare_interval(lower_bound, upper_bound, value):
    if value < lower_bound + EPSILON:
        return -1
    elif upper_bound - EPSILON < value:
        return 1
    else:
        return 0

def is_path_clear(target_x, target_y):
    quadratic_a = (GRAVITY_ACCELERATION ** 2) / 4
    quadratic_b = GRAVITY_ACCELERATION * target_y - INITIAL_VELOCITY ** 2
    quadratic_c = target_x ** 2 + target_y ** 2
    discriminant = quadratic_b ** 2 - 4 * quadratic_a * quadratic_c

    if discriminant < 0 and -EPSILON < discriminant:
        discriminant = 0

    if discriminant < 0:
        return False

    for sign in (-1, 1):
        t_squared = (-quadratic_b + sign * math.sqrt(discriminant)) / (2 * quadratic_a)
        if t_squared <= 0:
            continue

        time = math.sqrt(t_squared)
        velocity_x = target_x / time
        velocity_y = (target_y + GRAVITY_ACCELERATION * time * time / 2) / time

        y_at_goal_x = projectile_position(velocity_y, GOAL_X / velocity_x)
        if y_at_goal_x < GOAL_Y - EPSILON:
            continue
        is_valid = True

        for segment_index in range(NUM_SEGMENTS):
            if SEGMENT_LEFT[segment_index] >= GOAL_X:
                continue

            if (SEGMENT_RIGHT[segment_index] == GOAL_X and 
                GOAL_Y <= SEGMENT_TOP[segment_index] and 
                SEGMENT_BOTTOM[segment_index] <= y_at_goal_x):
                is_valid = False

            y_at_left = compare_interval(
                SEGMENT_BOTTOM[segment_index], 
                SEGMENT_TOP[segment_index], 
                projectile_position(velocity_y, SEGMENT_LEFT[segment_index] / velocity_x)
            )
            y_at_right = compare_interval(
                SEGMENT_BOTTOM[segment_index], 
                SEGMENT_TOP[segment_index], 
                projectile_position(velocity_y, SEGMENT_RIGHT[segment_index] / velocity_x)
            )

            x_at_apex = compare_interval(
                SEGMENT_LEFT[segment_index], 
                SEGMENT_RIGHT[segment_index], 
                velocity_x * (velocity_y / GRAVITY_ACCELERATION)
            )
            y_at_apex = compare_interval(
                SEGMENT_BOTTOM[segment_index], 
                SEGMENT_TOP[segment_index], 
                projectile_position(velocity_y, velocity_y / GRAVITY_ACCELERATION)
            )
            if x_at_apex == 0 and y_at_apex >= 0 and y_at_left < 0:
                is_valid = False
            if y_at_left * y_at_right <= 0:
                is_valid = False
        if is_valid:
            return True
    return False

if __name__ == '__main__':
    NUM_SEGMENTS, INITIAL_VELOCITY, GOAL_X, GOAL_Y = list(map(int, input().split()))
    SEGMENT_LEFT = []
    SEGMENT_BOTTOM = []
    SEGMENT_RIGHT = []
    SEGMENT_TOP = []
    for _ in range(NUM_SEGMENTS):
        seg_left, seg_bottom, seg_right, seg_top = list(map(int, input().split()))
        SEGMENT_LEFT.append(seg_left)
        SEGMENT_BOTTOM.append(seg_bottom)
        SEGMENT_RIGHT.append(seg_right)
        SEGMENT_TOP.append(seg_top)

    for segment_index in range(NUM_SEGMENTS):
        SEGMENT_RIGHT[segment_index] = min(SEGMENT_RIGHT[segment_index], GOAL_X)

    is_possible = is_path_clear(GOAL_X, GOAL_Y)
    for segment_index in range(NUM_SEGMENTS):
        if SEGMENT_LEFT[segment_index] == 0 and SEGMENT_TOP[segment_index] != 0:
            pass
        else:
            is_possible |= is_path_clear(SEGMENT_LEFT[segment_index], SEGMENT_TOP[segment_index])

        if SEGMENT_RIGHT[segment_index] == 0 and SEGMENT_TOP[segment_index] != 0:
            pass
        else:
            is_possible |= is_path_clear(SEGMENT_RIGHT[segment_index], SEGMENT_TOP[segment_index])

    print("Yes" if is_possible else "No")