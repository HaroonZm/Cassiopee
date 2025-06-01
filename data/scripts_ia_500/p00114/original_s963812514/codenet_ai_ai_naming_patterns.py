from math import gcd
from functools import reduce

def compute_lcm(number_1, number_2):
    return number_1 * number_2 // gcd(number_1, number_2)

def compute_orders(base_list, modulus_list):
    for base, modulus in zip(base_list, modulus_list):
        order = 1
        residue = base % modulus
        while residue != 1:
            residue = (residue * base) % modulus
            order += 1
        yield order

while True:
    input_values = map(int, raw_input().split())
    if all(value == 0 for value in input_values):
        break
    bases = input_values[::2]
    moduli = input_values[1::2]
    orders = compute_orders(bases, moduli)
    result = reduce(compute_lcm, orders)
    print(result)