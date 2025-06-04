#!/usr/bin/env python3

def compute_gcd(value_a, value_b):
    while value_b:
        value_a, value_b = value_b, value_a % value_b
    return value_a

def compute_lcm(value_a, value_b):
    return value_a // compute_gcd(value_a, value_b) * value_b

class ModularCongruenceSystem(object):
    def __init__(self):
        self.current_solution = 0
        self.current_modulus = 1
    def add_congruence(self, remainder, modulus):
        temp_solution = self.current_solution
        temp_modulus = self.current_modulus
        combined_modulus = compute_lcm(temp_modulus, modulus)
        while temp_solution < combined_modulus:
            if (temp_solution % modulus) == remainder:
                self.current_solution = temp_solution
                self.current_modulus = combined_modulus
                return
            temp_solution += temp_modulus
        else:
            raise ValueError('conflict_in_congruences')
    def get_current_congruence(self):
        return (self.current_solution, self.current_modulus)

def main_process():
    total_range, modulus_count, rounds = list(map(int, input().split()))
    modulus_values = list(map(int, input().split()))

    for round_index in range(rounds):
        remainders = list(map(int, input().split()))
        congruence_system = ModularCongruenceSystem()
        for input_remainder, input_modulus in zip(remainders, modulus_values):
            if input_remainder == -1:
                continue
            congruence_system.add_congruence(input_remainder, input_modulus)

        solution_value, modulus_product = congruence_system.get_current_congruence()
        if total_range < solution_value:
            print(-1)
            return 0

        closest_solution = (total_range-solution_value) // modulus_product * modulus_product + solution_value
        if not 0 <= closest_solution <= total_range:
            print(-1)
            return 0

        total_range = closest_solution

    print(total_range)
    return 0

try:
    main_process()
except ValueError:
    print(-1)