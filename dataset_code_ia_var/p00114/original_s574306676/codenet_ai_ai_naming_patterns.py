def calc_gcd(val_num_1, val_num_2):
    num_a, num_b = val_num_1, val_num_2
    while num_b != 0:
        num_a, num_b = num_b, num_a % num_b
    return val_num_1 // num_a * val_num_2

while True:
    input_values = list(map(int, raw_input().split()))
    if any(input_values) == 0:
        break
    period_list = []
    for idx in range(0, 6, 2):
        base_val, mod_val = input_values[idx], input_values[idx + 1]
        temp_result = 1
        for period in range(1, mod_val):
            temp_result = (temp_result * base_val) % mod_val
            if temp_result == 1:
                break
        period_list.append(period)
    period_a, period_b, period_c = period_list
    print(calc_gcd(calc_gcd(period_a, period_b), period_c))