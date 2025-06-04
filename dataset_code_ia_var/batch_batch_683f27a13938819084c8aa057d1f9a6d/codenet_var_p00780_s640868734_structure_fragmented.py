def initialize_prime_list(size):
    return [1 for _ in range(size)]

def set_non_prime_indices(p):
    p[0] = 0
    p[1] = 0

def mark_multiples_as_non_prime(p, start, end, max_index):
    for i in range(start, end):
        mark_multiples_for_i(p, i, max_index)

def mark_multiples_for_i(p, i, max_index):
    for j in range(2, max_index // i + 1):
        mark_composite(p, i, j)

def mark_composite(p, i, j):
    p[i * j] = 0

def sieve_primes(limit):
    p = initialize_prime_list(limit + 1)
    set_non_prime_indices(p)
    mark_multiples_as_non_prime(p, 2, limit // 2, limit)
    return p

def read_integer():
    return int(input())

def process_input_loop(p):
    while True:
        n = get_next_input()
        if check_zero(n):
            break
        process_number(n, p)

def get_next_input():
    return read_integer()

def check_zero(n):
    return n == 0

def process_number(n, p):
    s = count_prime_pairs(n, p)
    print_result(s)

def count_prime_pairs(n, p):
    s = 0
    for i in generate_candidate_indices(n):
        if is_prime_pair(i, n, p):
            s = update_sum(s)
    return s

def generate_candidate_indices(n):
    return range(1, n // 2 + 1)

def is_prime_pair(i, n, p):
    return p[i] == 1 and p[n - i] == 1

def update_sum(s):
    return s + 1

def print_result(s):
    print(s)

def main():
    prime_limit = 1000000
    p = sieve_primes(prime_limit)
    process_input_loop(p)

main()