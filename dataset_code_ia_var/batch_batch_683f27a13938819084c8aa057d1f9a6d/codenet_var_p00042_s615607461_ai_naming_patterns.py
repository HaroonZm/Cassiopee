case_index = 0
for capacity_input in iter(input, '0'):
    case_index += 1
    capacity = int(capacity_input)
    dp_values = [0] * (capacity + 1)
    for _ in range(int(input())):
        value, weight = map(int, input().split(','))
        for curr_capacity in range(capacity, weight - 1, -1):
            if dp_values[curr_capacity] < dp_values[curr_capacity - weight] + value:
                dp_values[curr_capacity] = dp_values[curr_capacity - weight] + value
    for weight_sum in range(capacity + 1):
        if dp_values[capacity] == dp_values[weight_sum]:
            print(f'Case {case_index}:\n{dp_values[capacity]}\n{weight_sum}')
            break