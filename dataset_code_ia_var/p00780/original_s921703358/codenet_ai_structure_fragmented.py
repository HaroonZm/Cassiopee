import bisect

def initialize_primes_list(size):
    return [0, 0] + [1] * (size - 2)

def mark_non_primes(primes, start, stop):
    for i in range(start, stop):
        if primes[i]:
            mark_multiples(primes, i, stop)

def mark_multiples(primes, base, limit):
    for j in range(base*base, limit, base):
        primes[j] = 0

def get_prime_values(primes):
    return [i for i, v in enumerate(primes) if v]

def get_input():
    return int(input())

def should_continue(n):
    return n != 0

def get_half_index(prime_values, n):
    return bisect.bisect(prime_values, n//2)

def count_goldbach_pairs(primes, prime_values, n):
    eov = get_half_index(prime_values, n)
    relevant_primes = prime_values[:eov]
    return sum(is_pair(primes, n, p) for p in relevant_primes)

def is_pair(primes, n, p):
    return primes[n - p]

def main_loop(primes, prime_values):
    while True:
        n = get_input()
        if not should_continue(n):
            break
        print(count_goldbach_pairs(primes, prime_values, n))

def main():
    size = 32769
    primes = initialize_primes_list(size)
    mark_non_primes(primes, 2, 182)
    prime_values = get_prime_values(primes)
    main_loop(primes, prime_values)

main()