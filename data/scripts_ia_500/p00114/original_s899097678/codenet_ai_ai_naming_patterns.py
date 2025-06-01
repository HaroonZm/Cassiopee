from math import gcd as greatest_common_divisor

def calculate_multiplicative_order(base_value, modulus_value):
    current_power = base_value
    order_count = 1
    while current_power != 1:
        current_power = (current_power * base_value) % modulus_value
        order_count += 1
    return order_count

while True:
    base1, mod1, base2, mod2, base3, mod3 = map(int, input().split())
    if base1 == 0:
        break
    order_base1 = calculate_multiplicative_order(base1, mod1)
    order_base2 = calculate_multiplicative_order(base2, mod2)
    order_base3 = calculate_multiplicative_order(base3, mod3)
    order_base12 = order_base1 * order_base2 // greatest_common_divisor(order_base1, order_base2)
    order_base123 = order_base12 * order_base3 // greatest_common_divisor(order_base12, order_base3)
    print(order_base123)