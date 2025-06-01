def greatest_common_divisor(value_a, value_b):
    return value_a if value_b == 0 else greatest_common_divisor(value_b, value_a % value_b)

while True:
    base_1, modulus_1, base_2, modulus_2, base_3, modulus_3 = map(int, raw_input().split())
    if base_1 == 0:
        break
    residue_1 = residue_2 = residue_3 = 1
    residue_1 = base_1 * residue_1 % modulus_1
    residue_2 = base_2 * residue_2 % modulus_2
    residue_3 = base_3 * residue_3 % modulus_3
    cycle_1 = cycle_2 = cycle_3 = 1
    while residue_1 != 1:
        residue_1 = base_1 * residue_1 % modulus_1
        cycle_1 += 1
    while residue_2 != 1:
        residue_2 = base_2 * residue_2 % modulus_2
        cycle_2 += 1
    while residue_3 != 1:
        residue_3 = base_3 * residue_3 % modulus_3
        cycle_3 += 1
    least_common_multiple_12 = cycle_1 * cycle_2 / greatest_common_divisor(cycle_1, cycle_2)
    least_common_multiple_123 = least_common_multiple_12 * cycle_3 / greatest_common_divisor(least_common_multiple_12, cycle_3)
    print least_common_multiple_123