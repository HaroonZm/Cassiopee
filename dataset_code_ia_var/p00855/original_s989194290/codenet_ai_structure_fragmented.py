import math

def initialize_prime_list(n):
    primes = [0, 0]
    primes += [1 for _ in range(n-1)]
    return primes

def get_upper_bound(n):
    return math.sqrt(n) + 1

def mark_multiples(prime, d, n):
    prod = 2
    def loop(prime, d, prod, n):
        if d * prod > n:
            return
        prime[d * prod] = 0
        loop(prime, d, prod+1, n)
    loop(prime, d, prod, n)

def check_and_mark(prime, d, n):
    if prime[d] == 0:
        return
    mark_multiples(prime, d, n)

def sieve_iterate(prime, ub, n):
    def step(d, prime, ub, n):
        if d > ub:
            return
        if prime[d] != 0:
            check_and_mark(prime, d, n)
        step(d+1, prime, ub, n)
    step(2, prime, ub, n)

def sieve(n):
    prime = initialize_prime_list(n)
    ub = get_upper_bound(n)
    sieve_iterate(prime, ub, n)
    return prime

def get_input():
    return int(raw_input())

def break_if_zero(k):
    if k == 0:
        return True
    return False

def search_left(prime, l):
    def move_left(p, idx):
        if p[idx] != 0:
            return idx
        return move_left(p, idx-1)
    return move_left(prime, l)

def search_right(prime, r):
    def move_right(p, idx):
        if p[idx] != 0:
            return idx
        return move_right(p, idx+1)
    return move_right(prime, r)

def print_prime_gap(left, right):
    print (right-1) - (left+1) + 2

def main_loop(prime):
    while True:
        k = get_input()
        if break_if_zero(k):
            break
        l = r = k
        left = search_left(prime, l)
        right = search_right(prime, r)
        print_prime_gap(left, right)

def main():
    prime = sieve(1299709)
    main_loop(prime)

main()