def compute_gcd(value_a, value_b):
    if value_b == 0:
        return value_a
    return compute_gcd(value_b, value_a % value_b)

while True:
    input_values = list(map(int, input().split()))
    if input_values.count(0) == 6:
        break
    base_x, mod_x = input_values[0], input_values[1]
    base_y, mod_y = input_values[2], input_values[3]
    base_z, mod_z = input_values[4], input_values[5]

    remainder_x = base_x % mod_x
    order_x = 1
    while remainder_x != 1:
        remainder_x = (base_x * remainder_x) % mod_x
        order_x += 1

    remainder_y = base_y % mod_y
    order_y = 1
    while remainder_y != 1:
        remainder_y = (base_y * remainder_y) % mod_y
        order_y += 1

    remainder_z = base_z % mod_z
    order_z = 1
    while remainder_z != 1:
        remainder_z = (base_z * remainder_z) % mod_z
        order_z += 1

    order_xy = order_x * order_y // compute_gcd(order_x, order_y)
    print(order_xy * order_z // compute_gcd(order_xy, order_z))