MAX_LIMIT = 1000000
SQRT_LIMIT = 1000

def generate_prime_numbers():
    prime_flags = [True] * MAX_LIMIT
    for even_index in range(4, MAX_LIMIT, 2):
        prime_flags[even_index] = False
    for candidate in range(3, SQRT_LIMIT, 2):
        if prime_flags[candidate]:
            for composite_index in range(candidate * 2, MAX_LIMIT, candidate):
                prime_flags[composite_index] = False
    prime_list = []
    for number in range(2, MAX_LIMIT):
        if prime_flags[number]:
            prime_list.append(number)
    return prime_list

prime_numbers_sequence = generate_prime_numbers()

while True:
    try:
        total_sum = 0
        input_count = int(input())
        if input_count == 0:
            break
        for prime_index in range(input_count):
            total_sum += prime_numbers_sequence[prime_index]
        print(total_sum)
    except:
        break