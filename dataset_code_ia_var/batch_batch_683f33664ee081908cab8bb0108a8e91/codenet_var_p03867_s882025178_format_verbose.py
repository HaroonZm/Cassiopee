modulus = 10**9 + 7

divisors_list = []
divisor_candidate = 1

result_sum = 0

target_number, exponent_base = map(int, raw_input().split())

while divisor_candidate * divisor_candidate <= target_number:
    
    if target_number % divisor_candidate == 0:
        divisors_list.append(divisor_candidate)
        if divisor_candidate * divisor_candidate < target_number:
            divisors_list.append(target_number // divisor_candidate)
    
    divisor_candidate += 1

divisors_list.sort()

power_contributions = []

for index_current in range(len(divisors_list)):
    
    current_divisor = divisors_list[index_current]
    
    current_power = pow(exponent_base, (-(current_divisor + 1) // 2), modulus)
    power_contributions.append(current_power)
    
    for index_previous in range(index_current):
        previous_divisor = divisors_list[index_previous]
        if current_divisor % previous_divisor == 0:
            power_contributions[index_current] = (power_contributions[index_current] - power_contributions[index_previous]) % modulus
    
    if current_divisor % 2 == 0:
        inverse_of_2 = pow(2, modulus - 2, modulus)
    else:
        inverse_of_2 = pow(2, modulus - 1, modulus)
    
    term = (power_contributions[index_current] * current_divisor * inverse_of_2) % modulus
    result_sum = (result_sum + term) % modulus

print result_sum