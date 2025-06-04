test_case_count = int(input())

def compute_gcd(value_left, value_right):
    remainder = value_left % value_right
    if remainder == 0:
        return value_right
    return compute_gcd(value_right, remainder)

def is_valid_configuration(limit_max, limit_min, threshold_min, threshold_max):
    if limit_min > limit_max or threshold_max < limit_min:
        return 0
    step_gcd = compute_gcd(limit_min, threshold_max)
    step_count = (limit_max - threshold_min - 1) // step_gcd
    candidate_value = limit_max - step_count * step_gcd
    if candidate_value - limit_min < 0:
        return 0
    return 1

for _ in range(test_case_count):
    input_a, input_b, input_c, input_d = map(int, input().split())
    is_possible = is_valid_configuration(input_a, input_b, input_c, input_d)
    print("Yes" if is_possible else "No")