max_number = 1000000

is_prime = [False, False] + [True] * (max_number - 1)
prime_numbers = []

for current_number in range(2, max_number):
    if not is_prime[current_number]:
        continue
    prime_numbers.append(current_number)
    for multiple in range(current_number * 2, max_number, current_number):
        is_prime[multiple] = False

while True:
    input_value = input()
    if not input_value:
        break

    target_number = int(input_value)
    count_prime_pairs = 0

    for prime_candidate in prime_numbers:
        if prime_candidate > target_number / 2:
            break
        if is_prime[target_number - prime_candidate]:
            count_prime_pairs += 1

    print(count_prime_pairs)