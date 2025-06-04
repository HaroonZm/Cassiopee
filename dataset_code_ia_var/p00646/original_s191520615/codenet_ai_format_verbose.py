from collections import defaultdict

def get_prime_factors_exponents(number):
    prime_factor_exponents = defaultdict(int)
    divisor = 2
    while divisor * divisor <= number:
        while number % divisor == 0:
            prime_factor_exponents[divisor] += 1
            number //= divisor
        divisor += 1
    if number != 1:
        prime_factor_exponents[number] += 1
    return list(prime_factor_exponents.values())

def count_divisor_pairs(exponents_list, current_product, current_index, total_exponents):
    if current_index == total_exponents:
        return current_product
    return (
        count_divisor_pairs(
            exponents_list, 
            current_product * exponents_list[current_index], 
            current_index + 1,
            total_exponents
        ) * 2 +
        count_divisor_pairs(
            exponents_list, 
            current_product,
            current_index + 1,
            total_exponents
        )
    )

while True:
    number_input = int(input())
    if number_input == 0:
        break
    prime_exponents_list = get_prime_factors_exponents(number_input)
    total_pairs = count_divisor_pairs(prime_exponents_list, 1, 0, len(prime_exponents_list))
    print((total_pairs + 1) // 2)