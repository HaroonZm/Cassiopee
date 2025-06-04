value_map = {1: 6000, 2: 4000, 3: 3000, 4: 2000}

for iteration_index in range(4):
    key_input, quantity_input = map(int, input().split())
    result_value = value_map[key_input] * quantity_input
    print(result_value)