input_count = int(input())
current_value_a, current_value_b = 1, 1
for index_input in range(input_count):
    input_x, input_y = map(int, input().split())
    required_multiplier = max(-(-current_value_a // input_x), -(-current_value_b // input_y))
    current_value_a, current_value_b = required_multiplier * input_x, required_multiplier * input_y
print(current_value_a + current_value_b)