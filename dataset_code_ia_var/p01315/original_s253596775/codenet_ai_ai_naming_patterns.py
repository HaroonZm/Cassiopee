while True:
    input_count = input()
    if input_count == 0:
        break
    result_list = []
    for index in range(input_count):
        input_line = raw_input().split()
        name_value = input_line[0]
        price_value, param_a, param_b, param_c, param_d, param_e, param_f, speed_value, multiplier_value = map(int, input_line[1:])
        denominator = param_a + param_b + param_c + (param_d + param_e) * multiplier_value
        numerator = (multiplier_value * param_f * speed_value - price_value)
        metric_value = numerator * 1.0 / denominator
        result_list.append([name_value, metric_value])
    result_list = sorted(sorted(result_list), key=lambda pair: pair[1], reverse=True)
    for result_item, metric in result_list:
        print result_item
    print "#"