from math import gcd

def compute_power_cycle_length(base, modulus):
    cycle_length = 1
    current_power = base
    while current_power != 1:
        cycle_length += 1
        current_power = (current_power * base) % modulus
    return cycle_length

while True:
    input_vals = list(map(int, input().split()))
    base1, mod1, base2, mod2, base3, mod3 = input_vals
    if base1 == 0:
        break
    cycle_len1 = compute_power_cycle_length(base1, mod1)
    cycle_len2 = compute_power_cycle_length(base2, mod2)
    cycle_len3 = compute_power_cycle_length(base3, mod3)
    lcm_12 = cycle_len1 * cycle_len2 // gcd(cycle_len1, cycle_len2)
    lcm_123 = lcm_12 * cycle_len3 // gcd(lcm_12, cycle_len3)
    print(lcm_123)