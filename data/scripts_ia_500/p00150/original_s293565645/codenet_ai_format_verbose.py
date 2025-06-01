MAX_LIMIT = 10000
SQRT_LIMIT = 100  # approximate square root of MAX_LIMIT

is_prime = [True for _ in range(MAX_LIMIT)]

def generate_prime_sieve():
    
    # Mark even numbers greater than 2 as not prime
    for number in range(4, MAX_LIMIT, 2):
        is_prime[number] = False
    
    # Check odd numbers for primality using sieve of Eratosthenes
    for current_number in range(3, SQRT_LIMIT, 2):
        if is_prime[current_number]:
            for multiple in range(current_number * current_number, MAX_LIMIT, current_number):
                is_prime[multiple] = False

generate_prime_sieve()

while True:
    
    input_number = int(input())
    
    if input_number == 0:
        break
    
    # Ensure input number is odd to check for twin primes
    if input_number % 2 == 0:
        input_number -= 1
    
    # Find the largest twin prime pair less than or equal to input_number
    while not (is_prime[input_number] and is_prime[input_number - 2]):
        input_number -= 2
    
    print(input_number - 2, input_number)