def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True

def generate_primes_up_to(n):
    return [x for x in range(2,n+1) if is_prime(x)]

def count_consecutive_prime_sums(target, primes):
    count = 0
    start = 0
    end = 0
    current_sum = 0
    while True:
        if current_sum >= target:
            if current_sum == target:
                count += 1
            current_sum -= primes[start]
            start += 1
        else:
            if end == len(primes):
                break
            current_sum += primes[end]
            end += 1
    return count

import sys

primes = generate_primes_up_to(10000)
for line in sys.stdin:
    n = int(line)
    if n == 0:
        break
    print(count_consecutive_prime_sums(n, primes))