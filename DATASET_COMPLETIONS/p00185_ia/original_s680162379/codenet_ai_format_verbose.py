from bisect import bisect_left

def generate_primes_up_to(limit):
    
    is_prime_flags = [True] * (limit + 1)
    is_prime_flags[0] = False
    is_prime_flags[1] = False
    
    max_divisor = int(limit ** 0.5) + 1
    
    for number in range(2, max_divisor):
        if is_prime_flags[number]:
            for multiple in range(number * number, limit + 1, number):
                is_prime_flags[multiple] = False
                
    primes_list = [num for num, is_prime in enumerate(is_prime_flags) if is_prime]
    
    return primes_list


def count_prime_pairs_adding_to_target(target_sum, sorted_primes, primes_count):
    
    pair_count = 0
    
    for prime in sorted_primes:
        
        if prime > target_sum // 2:
            break
        
        complement_index = bisect_left(sorted_primes, target_sum - prime)
        
        if complement_index < primes_count and sorted_primes[complement_index] == target_sum - prime:
            pair_count += 1
            
    return pair_count


primes_list = generate_primes_up_to(1000000)
total_primes = len(primes_list)

while True:
    
    input_number = int(input())
    
    if input_number == 0:
        break
    
    result = count_prime_pairs_adding_to_target(input_number, primes_list, total_primes)
    
    print(result)