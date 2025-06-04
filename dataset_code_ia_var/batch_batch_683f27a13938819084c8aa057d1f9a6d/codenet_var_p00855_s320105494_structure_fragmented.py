import sys
import bisect

def get_max():
    return 1299710

def initialize_prime_list(size):
    return [-1] * size

def append_prime(prime_list, value):
    prime_list.append(value)

def is_prime_unmarked(prime, idx):
    return prime[idx - 1] == -1

def mark_prime(prime, idx):
    prime[idx - 1] = 0

def mark_non_prime(prime, idx):
    prime[idx - 1] = 1

def sieve_primes(prime, prime_list, max_value):
    i = 2
    while i < max_value:
        if is_prime_unmarked(prime, i):
            mark_prime(prime, i)
            append_prime(prime_list, i)
            multiple = i * 2
            while multiple < max_value:
                mark_non_prime(prime, multiple)
                multiple += i
        i = get_next_candidate(i)
    return prime_list

def get_next_candidate(current):
    if current == 2:
        return current + 1
    else:
        return current + 2

def get_input():
    return sys.stdin.readline()

def process_input_line(line):
    return int(line)

def should_break(n):
    return n == 0

def get_bisect_start(prime_list, value):
    return bisect.bisect_left(prime_list, value)

def get_bisect_end(prime_list, value):
    return bisect.bisect_right(prime_list, value)

def is_prime_at_index(prime_list, idx, n):
    if idx < len(prime_list):
        return prime_list[idx] == n
    return False

def output_zero():
    print 0

def output_difference(prime_list, end, start):
    print prime_list[end] - prime_list[start - 1]

def main_loop(prime_list):
    while True:
        line = get_input()
        n = process_input_line(line)
        if should_break(n):
            break
        start = get_bisect_start(prime_list, n)
        end = get_bisect_end(prime_list, n)
        if is_prime_at_index(prime_list, start, n):
            output_zero()
        else:
            output_difference(prime_list, end, start)

def main():
    MAX = get_max()
    prime = initialize_prime_list(MAX)
    prime_list = []
    sieve_primes(prime, prime_list, MAX)
    main_loop(prime_list)

main()