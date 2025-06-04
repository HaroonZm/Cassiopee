num_cases = int(input())

def calculate_max_steps(value_a, value_b):
    if value_a == value_b:
        return 2 * value_a - 2
    if value_b < value_a:
        return calculate_max_steps(value_b, value_a)
    lower_bound = value_a
    upper_bound = 2 * value_b
    target_value = value_a * value_b
    while upper_bound - lower_bound > 1:
        middle = (lower_bound + upper_bound) // 2
        max_product = ((middle + 1) // 2) * (middle + 1 - (middle + 1) // 2)
        if max_product < target_value:
            lower_bound = middle
        else:
            upper_bound = middle
    return lower_bound - 1

for case_index in range(num_cases):
    input_a, input_b = map(int, input().split())
    print(calculate_max_steps(input_a, input_b))