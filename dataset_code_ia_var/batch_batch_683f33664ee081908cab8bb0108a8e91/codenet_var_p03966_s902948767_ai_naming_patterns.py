def process_sequence():
    input_count = int(input())
    value_x = 1
    value_y = 1
    for _ in range(input_count):
        factor_t, factor_a = map(int, input().split())
        multiplier_z = -1 * min(-value_x // factor_t, -value_y // factor_a)
        value_x = multiplier_z * factor_t
        value_y = multiplier_z * factor_a
    print(value_x + value_y)

process_sequence()