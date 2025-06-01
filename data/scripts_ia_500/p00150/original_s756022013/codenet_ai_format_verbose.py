MAX_LIMIT = 10001
SQRT_LIMIT = 100  # Approximate square root of MAX_LIMIT

is_prime = [True] * MAX_LIMIT

def generate_prime_sieve():
    
    # Mark non-prime even numbers (except 2) as False (optional optimization)
    # for num in range(4, MAX_LIMIT, 2):
    #     is_prime[num] = False
    
    # Use Sieve of Eratosthenes to mark primes
    for current_num in range(3, SQRT_LIMIT, 2):
        if is_prime[current_num]:
            for multiple in range(current_num * current_num, MAX_LIMIT, current_num):
                is_prime[multiple] = False

generate_prime_sieve()

twin_prime_table = [0] * MAX_LIMIT
latest_twin_prime = 0

for candidate_num in range(5, MAX_LIMIT, 2):
    if is_prime[candidate_num] and is_prime[candidate_num - 2]:
        latest_twin_prime = candidate_num
    twin_prime_table[candidate_num] = latest_twin_prime

while True:
    input_number = int(input())
    
    if input_number == 0:
        break
    
    if input_number % 2 == 0:
        input_number -= 1
    
    lower_twin_prime = twin_prime_table[input_number] - 2
    upper_twin_prime = twin_prime_table[input_number]
    
    print(lower_twin_prime, upper_twin_prime)