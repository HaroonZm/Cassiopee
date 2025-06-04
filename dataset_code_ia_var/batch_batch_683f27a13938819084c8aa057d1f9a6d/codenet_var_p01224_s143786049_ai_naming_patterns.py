def calculate_divisor_sum(target_number):
    divisor_sum = 1
    if target_number <= 5:
        return 0
    for divisor_candidate in range(2, int(target_number ** 0.5) + 1):
        if target_number % divisor_candidate == 0:
            paired_divisor = target_number // divisor_candidate
            if divisor_candidate != paired_divisor:
                divisor_sum += divisor_candidate + paired_divisor
            else:
                divisor_sum += divisor_candidate
    return divisor_sum

while True:
    input_number = int(input())
    if input_number == 0:
        break
    proper_divisor_sum = calculate_divisor_sum(input_number)
    if input_number == proper_divisor_sum:
        print('perfect number')
    elif input_number > proper_divisor_sum:
        print('deficient number')
    else:
        print('abundant number')