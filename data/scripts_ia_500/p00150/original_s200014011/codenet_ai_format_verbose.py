import math


maximum_value = 10000

prime_flags = [1 for index in range(maximum_value + 1)]
prime_flags[0] = 0

upper_limit_for_sieve = int(math.sqrt(maximum_value)) + 1

for current_number in range(2, upper_limit_for_sieve):
    
    if prime_flags[current_number] != 0:
        
        multiple = current_number * 2
        
        while multiple < maximum_value:
            
            prime_flags[multiple] = 0
            
            multiple += current_number


prime_numbers = []

for candidate_number in range(maximum_value + 1):
    
    if prime_flags[candidate_number] == 1:
        
        prime_numbers.append(candidate_number)


prime_numbers.reverse()


while True:
    
    input_number = int(input())
    
    if input_number == 0:
        
        quit()
    
    for index in range(len(prime_numbers) - 1):
        
        larger_prime = prime_numbers[index]
        
        smaller_prime = prime_numbers[index + 1]
        
        if larger_prime <= input_number and (larger_prime - smaller_prime) == 2:
            
            print(smaller_prime, larger_prime)
            
            break