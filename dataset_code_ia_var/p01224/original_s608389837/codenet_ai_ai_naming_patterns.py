def compute_divisor_sum(number):
    factor_list = []
    factor_candidate = 2
    temp_number = number
    while factor_candidate * factor_candidate <= temp_number:
        exponent_count = 0
        if temp_number % factor_candidate == 0:
            while temp_number % factor_candidate == 0:
                temp_number //= factor_candidate
                exponent_count += 1
        if exponent_count > 0:
            factor_list.append([factor_candidate, exponent_count])
        factor_candidate += 1
    if temp_number > 1:
        factor_list.append([temp_number, 1])
    divisor_sum = 1
    for base, power in factor_list:
        divisor_sum *= (base ** (power + 1) - 1) // (base - 1)
    return divisor_sum

while True:
    input_value = input()
    if input_value == 0:
        break
    integer_number = input_value
    proper_divisor_sum = compute_divisor_sum(integer_number) - integer_number
    if proper_divisor_sum == integer_number:
        print("perfect number")
    elif proper_divisor_sum < integer_number:
        print("deficient number")
    else:
        print("abundant number")