user_inputs = []

prime_counts = [2]

while True:
    try:
        user_input = int(input())
        user_inputs.append(user_input)
    except:
        break

def generate_prime_numbers_up_to(limit):
    is_number_prime = [True] * (limit + 1)
    is_number_prime[0] = False
    is_number_prime[1] = False

    for candidate in range(2, int(limit ** 0.5) + 1):

        if not is_number_prime[candidate]:
            continue

        for multiple in range(candidate * 2, limit + 1, candidate):
            is_number_prime[multiple] = False

    prime_number_list = [
        number for number in range(limit + 1) if is_number_prime[number]
    ]
    return prime_number_list

list_of_primes = generate_prime_numbers_up_to(max(user_inputs))

for input_value in user_inputs:

    count_of_primes_less_than_or_equal_to_input = len([
        prime for prime in list_of_primes if prime <= input_value
    ])

    print(count_of_primes_less_than_or_equal_to_input)