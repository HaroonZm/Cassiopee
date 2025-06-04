def compute_gcd(value_a, value_b):
    return value_a if value_b == 0 else compute_gcd(value_b, value_a % value_b)

while True:
    residue_1, modulus_1, residue_2, modulus_2, residue_3, modulus_3 = map(int, raw_input().split())
    if residue_1 == 0:
        break

    power_1 = 1
    power_2 = 1
    power_3 = 1

    power_1 = residue_1 * power_1 % modulus_1
    power_2 = residue_2 * power_2 % modulus_2
    power_3 = residue_3 * power_3 % modulus_3

    order_1 = 1
    order_2 = 1
    order_3 = 1

    while power_1 != 1:
        power_1 = residue_1 * power_1 % modulus_1
        order_1 += 1
    while power_2 != 1:
        power_2 = residue_2 * power_2 % modulus_2
        order_2 += 1
    while power_3 != 1:
        power_3 = residue_3 * power_3 % modulus_3
        order_3 += 1

    lcm_12 = order_1 * order_2 // compute_gcd(order_1, order_2)
    lcm_123 = lcm_12 * order_3 // compute_gcd(lcm_12, order_3)
    print lcm_123