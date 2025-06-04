import math

# Entrée de deux entiers séparés par un espace
number_of_elements, number_of_selections = map(int, input().split())

def compute_modular_combination(total_elements, selected_elements, modulus):
    """
    Calcule (total_elements C selected_elements) modulo modulus en utilisant la décomposition des factorielles et l'inverse modulaire.
    """
    from math import factorial
    
    if total_elements < 0 or selected_elements < 0 or total_elements < selected_elements:
        return 0
    
    if total_elements == 0 or selected_elements == 0:
        return 1

    numerator = factorial(total_elements) % modulus
    denominator_selected = factorial(selected_elements) % modulus
    denominator_remaining = factorial(total_elements - selected_elements) % modulus

    modular_inverse_denominator_selected = compute_modular_power(denominator_selected, modulus - 2, modulus)
    modular_inverse_denominator_remaining = compute_modular_power(denominator_remaining, modulus - 2, modulus)

    result = (numerator * modular_inverse_denominator_selected * modular_inverse_denominator_remaining) % modulus

    return result

def compute_modular_power(base, exponent, modulus):
    """
    Calcule (base^exponent) modulo modulus via exponentiation rapide.
    """
    if exponent == 0:
        return 1

    if exponent % 2 == 0:
        half_power = compute_modular_power(base, exponent // 2, modulus)
        return (half_power * half_power) % modulus

    if exponent % 2 == 1:
        return (base * compute_modular_power(base, exponent - 1, modulus)) % modulus

modulus_prime = 1000000007

modular_combination_result = compute_modular_combination(number_of_selections, number_of_elements, modulus_prime)

print(int(modular_combination_result))