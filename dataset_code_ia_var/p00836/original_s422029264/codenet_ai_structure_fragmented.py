def get_prime_flags(size):
    return [1 for _ in range(size)]

def set_non_primes(flags):
    flags[:2] = [0, 0]
    return flags

def sieve_limit(limit):
    return int(math.sqrt(limit)) + 1

def mark_composites(flags, sieve_end, limit):
    def mark_for_i(flags, i, limit):
        def mark_multiple(flags, j):
            flags[j] = 0
        for j in range(i*i, limit, i):
            mark_multiple(flags, j)
    for i in range(2, sieve_end):
        if flags[i]:
            mark_for_i(flags, i, limit)
    return flags

def extract_primes(flags, limit):
    def is_a_prime(i):
        return flags[i] == 1
    def collect_prime(prime_list, i):
        prime_list.append(i)
    prime_list = []
    for i in range(limit):
        if is_a_prime(i):
            collect_prime(prime_list, i)
    return prime_list

def input_n():
    return int(input())

def should_break(n):
    return n == 0

def count_prime_sums(n, prime):
    total = 0
    l = len(prime)
    def count_from_i(i, n, prime):
        s = 0
        for j in range(i, l):
            s += prime[j]
            if s == n:
                return 1
            if s > n:
                return 0
        return 0
    for i in range(l+1):
        total += count_from_i(i, n, prime)
    return total

def print_count(cnt):
    print(cnt)

def process_queries(prime):
    while True:
        n = input_n()
        if should_break(n):
            break
        cnt = count_prime_sums(n, prime)
        print_count(cnt)

def main():
    SIZE = 10002
    LIMIT = 10001
    flags = get_prime_flags(SIZE)
    flags = set_non_primes(flags)
    sieve_end = sieve_limit(LIMIT)
    flags = mark_composites(flags, sieve_end, LIMIT)
    prime = extract_primes(flags, LIMIT)
    process_queries(prime)

main()