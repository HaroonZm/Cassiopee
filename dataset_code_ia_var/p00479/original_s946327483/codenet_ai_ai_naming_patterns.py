input_total = input()
for iteration_index in range(input()):
    value_a, value_b = map(int, raw_input().split())
    min_distance = min(value_a - 1, input_total - value_a, value_b - 1, input_total - value_b)
    result = (min_distance % 3) + 1
    print result