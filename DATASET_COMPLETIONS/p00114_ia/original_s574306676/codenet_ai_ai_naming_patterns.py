def compute_gcd(value_a, value_b):
    dividend, divisor = value_a, value_b
    while divisor != 0:
        dividend, divisor = divisor, dividend % divisor
    return value_a // dividend * value_b

while True:
    input_numbers = map(int, raw_input().split())
    if any(input_numbers) == 0:
        break

    order_list = []
    for index in range(0, 6, 2):
        base_value, modulus_value = input_numbers[index:index+2]
        current_power = 1
        for exponent in range(1, modulus_value):
            current_power = (current_power * base_value) % modulus_value
            if current_power == 1:
                break
        order_list.append(exponent)

    order_a, order_b, order_c = order_list
    print compute_gcd(compute_gcd(order_a, order_b), order_c)