while True:
    num_input_a, num_input_b = map(int, input().split())
    if num_input_a == 0 and num_input_b == 0:
        break
    if num_input_a <= num_input_b:
        num_input_a, num_input_b = num_input_b, num_input_a
    num_gcd_steps = 1
    while True:
        num_mod_result = num_input_a % num_input_b
        if num_mod_result == 0:
            break
        if num_mod_result != 0:
            num_input_a, num_input_b = num_input_b, num_mod_result
            num_gcd_steps += 1
    print(num_input_b, num_gcd_steps)