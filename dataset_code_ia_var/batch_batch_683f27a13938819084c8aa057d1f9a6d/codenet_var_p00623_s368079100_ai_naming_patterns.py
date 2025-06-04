def calculate_expression_tree():
    global buffer_index
    current_index = buffer_index
    buffer_index += 1
    if expression_tree_tokens[0] == '(':
        del expression_tree_tokens[0]
        left_values = calculate_expression_tree()
        del expression_tree_tokens[0]
        right_values = calculate_expression_tree()
        del expression_tree_tokens[0]
        for left_mask in range(16):
            for right_mask in range(16):
                combinations = left_values[left_mask] * right_values[right_mask]
                if combinations:
                    result_buffers[current_index][left_mask & right_mask] += combinations
                    result_buffers[current_index][left_mask | right_mask] += combinations
                    result_buffers[current_index][left_mask ^ right_mask] += combinations
    else:
        result_buffers[current_index][input_info[int(expression_tree_tokens.pop(0)) - 1]] = 1
    return result_buffers[current_index]

while True:
    expression_tree_tokens = list(input())
    if expression_tree_tokens[0] == 'E':
        break
    result_buffers = [[0 for _ in range(16)] for _ in range(20)]
    buffer_index = 0
    input_info = [0] * 10
    variable_count = int(input())
    for variable_index in range(variable_count):
        variable_values = list(map(int, input().split()))
        for bit_index in range(4):
            if variable_values[bit_index]:
                input_info[variable_index] |= (1 << bit_index)
    print(calculate_expression_tree()[15])