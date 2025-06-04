import math

# Génération de la liste des nombres premiers jusqu'à 500
prime_numbers_list = [2]
current_prime_candidate = 2
possible_prime_candidates = [2 * x - 1 for x in range(2, 500)]

while current_prime_candidate < math.sqrt(500):
    current_prime_candidate = possible_prime_candidates[0]
    prime_numbers_list.append(current_prime_candidate)
    filtered_candidates = []
    for candidate in possible_prime_candidates:
        if candidate % current_prime_candidate != 0:
            filtered_candidates.append(candidate)
    possible_prime_candidates = filtered_candidates

prime_numbers_list = prime_numbers_list + possible_prime_candidates

def calculate_prime_factor_points(number_to_factor):
    unique_prime_factors = []
    current_number = number_to_factor
    while current_number > 1:
        has_factor_been_found = False
        for possible_prime in prime_numbers_list:
            if current_number % possible_prime == 0:
                has_factor_been_found = True
                current_number = current_number / possible_prime
                if possible_prime not in unique_prime_factors:
                    unique_prime_factors.append(possible_prime)
                break
        if not has_factor_been_found:
            unique_prime_factors.append(current_number)
            current_number = 1
    sorted_prime_factors = sorted(unique_prime_factors)
    calculation_points = unique_prime_factors[-1] - sum(sorted_prime_factors[:-1])
    return calculation_points

while True:
    user_input = raw_input()
    input_numbers = [int(x) for x in user_input.split()]
    first_number = input_numbers[0]
    second_number = input_numbers[1]
    if first_number == 0:
        break
    else:
        first_number_points = calculate_prime_factor_points(first_number)
        second_number_points = calculate_prime_factor_points(second_number)
        if first_number_points > second_number_points:
            print 'a'
        else:
            print 'b'