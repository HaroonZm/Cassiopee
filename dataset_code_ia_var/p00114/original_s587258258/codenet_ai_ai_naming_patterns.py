def compute_gcd(value_a, value_b):
    if value_b == 0:
        return value_a
    return compute_gcd(value_b, value_a % value_b)

while True:
    input_values = list(map(int, input().split()))
    if input_values.count(0) == 6:
        break

    base_x = input_values[0]
    mod_x = input_values[1]
    current_x = base_x % mod_x
    order_x = 1
    while current_x != 1:
        current_x = (base_x * current_x) % mod_x
        order_x += 1

    base_y = input_values[2]
    mod_y = input_values[3]
    current_y = base_y % mod_y
    order_y = 1
    while current_y != 1:
        current_y = (base_y * current_y) % mod_y
        order_y += 1

    base_z = input_values[4]
    mod_z = input_values[5]
    current_z = base_z % mod_z
    order_z = 1
    while current_z != 1:
        current_z = (base_z * current_z) % mod_z
        order_z += 1

    lcm_xy = order_x * order_y // compute_gcd(order_x, order_y)
    lcm_xyz = lcm_xy * order_z // compute_gcd(lcm_xy, order_z)
    print(lcm_xyz)