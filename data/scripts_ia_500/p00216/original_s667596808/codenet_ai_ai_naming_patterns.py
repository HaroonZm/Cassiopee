while True:
    input_value = int(input())
    if input_value == -1:
        break
    base_value_a = 4280
    base_value_b = 1150
    if input_value <= 10:
        result_value = base_value_a - base_value_b
    elif 10 < input_value <= 20:
        result_value = base_value_a - (base_value_b + (input_value - 10) * 125)
    elif 20 < input_value <= 30:
        result_value = base_value_a - (base_value_b + 1250 + (input_value - 20) * 140)
    else:
        result_value = base_value_a - (base_value_b + 1250 + 1400 + (input_value - 30) * 160)
    print(result_value)