while True:
    input_number = int(input())
    if input_number == 0:
        break
    divisor_list = []
    for divisor_candidate in range(1, int(input_number**0.5) + 1):
        if input_number % divisor_candidate == 0:
            divisor_list.append(divisor_candidate)
            corresponding_divisor = input_number // divisor_candidate
            divisor_list.append(corresponding_divisor)
    divisor_set = set(divisor_list)
    if input_number in divisor_set:
        divisor_set.remove(input_number)
    divisor_sum = sum(divisor_set)
    if divisor_sum == input_number:
        print("perfect number")
    elif divisor_sum < input_number:
        print("deficient number")
    else:
        print("abundant number")