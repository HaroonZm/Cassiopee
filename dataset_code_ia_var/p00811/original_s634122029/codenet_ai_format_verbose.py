import sys

sys.setrecursionlimit(10000000)

def read_input():
    return sys.stdin.readline().rstrip()

def generate_list_of_primes_up_to(maximum_prime_value):
    is_prime = [False, False, True] + [False if index % 2 != 0 else True for index in range(maximum_prime_value - 2)]
    current_candidate = 3
    list_of_primes = []
    while current_candidate * current_candidate <= maximum_prime_value:
        if is_prime[current_candidate]:
            sieve_position = current_candidate * current_candidate
            while sieve_position <= maximum_prime_value:
                is_prime[sieve_position] = False
                sieve_position += current_candidate
        current_candidate += 2
    for index in range(len(is_prime)):
        if is_prime[index]:
            list_of_primes.append(index)
    return list_of_primes

maximum_prime_limit = 50001
list_of_primes_up_to_limit = generate_list_of_primes_up_to(maximum_prime_limit)

while True:
    max_product_value, ratio_numerator, ratio_denominator = map(int, read_input().split())
    if max_product_value == ratio_numerator == ratio_denominator == 0:
        break
    left_prime_index = 0
    current_max_triple = (0, 0, 0)
    for right_prime_index in range(len(list_of_primes_up_to_limit)):
        while True:
            left_prime = list_of_primes_up_to_limit[left_prime_index]
            right_prime = list_of_primes_up_to_limit[right_prime_index]
            current_product = left_prime * right_prime
            if (current_max_triple[0] < current_product <= max_product_value 
                and left_prime / right_prime >= ratio_numerator / ratio_denominator):
                current_max_triple = (current_product, left_prime_index, right_prime_index)
            if current_product > max_product_value and left_prime_index - 1 >= 0:
                left_prime_index -= 1
            elif left_prime_index + 1 <= right_prime_index and (list_of_primes_up_to_limit[left_prime_index + 1]) * right_prime <= max_product_value:
                left_prime_index += 1
            else:
                break
    print(list_of_primes_up_to_limit[current_max_triple[1]], list_of_primes_up_to_limit[current_max_triple[2]])