for loop_index in range(4):
    input_type, input_quantity = map(int, input().split())
    if input_type == 1:
        result_value = 6000 * input_quantity
    elif input_type == 2:
        result_value = 4000 * input_quantity
    elif input_type == 3:
        result_value = 3000 * input_quantity
    else:
        result_value = 2000 * input_quantity
    print(result_value)