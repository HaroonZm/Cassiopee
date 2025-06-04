number_to_analyze, power_base = map(int, input().split())
modulus_value = 10 ** 9 + 7

current_divisor = 1
maximum_divisor = number_to_analyze
divisors_of_number = []

while current_divisor * current_divisor <= number_to_analyze:
    if number_to_analyze % current_divisor == 0:
        divisors_of_number.append(current_divisor)
        if number_to_analyze // current_divisor != current_divisor:
            divisors_of_number.append(number_to_analyze // current_divisor)
    current_divisor += 1

divisors_of_number = sorted(divisors_of_number)
total_number_of_divisors = len(divisors_of_number)

distinct_powers_count = [0] * (total_number_of_divisors + 1)

cumulative_sum = 0

for current_index in range(total_number_of_divisors):
    current_divisor_value = divisors_of_number[current_index]
    exponent_value = (current_divisor_value + 1) // 2
    distinct_powers_count[current_index] = pow(power_base, exponent_value, modulus_value)
    
    for previous_index in range(current_index):
        previous_divisor_value = divisors_of_number[previous_index]
        if current_divisor_value % previous_divisor_value == 0:
            distinct_powers_count[current_index] = (distinct_powers_count[current_index] - distinct_powers_count[previous_index] + modulus_value) % modulus_value

    if current_divisor_value % 2 == 0:
        cumulative_sum = (cumulative_sum + (current_divisor_value * distinct_powers_count[current_index] // 2)) % modulus_value
    else:
        cumulative_sum = (cumulative_sum + (current_divisor_value * distinct_powers_count[current_index])) % modulus_value

print(cumulative_sum)