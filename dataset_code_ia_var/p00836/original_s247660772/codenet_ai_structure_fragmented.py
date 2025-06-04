def initialize_primes(size):
    return [0, 0] + [1] * (size - 1)

def sieve(primes, upper):
    for i in range(2, upper + 1):
        if primes[i]:
            mark_multiples(primes, i, len(primes))
            
def mark_multiples(primes, base, limit):
    for j in range(base * base, limit, base):
        primes[j] = 0

def get_input():
    return int(input())

def find_largest_prime_leq(n, primes):
    m = n
    while not primes[m]:
        m -= 1
    return m

def list_primes_till(m, primes):
    return [i for i in range(m + 1) if primes[i]]

def count_consecutive_prime_sums(n, pnum):
    ans = 0
    for i in range(len(pnum)):
        tmp = 0
        for j in range(i, len(pnum)):
            tmp += pnum[j]
            if tmp == n:
                ans += 1
                break
            if tmp > n:
                break
    return ans

def solve_case(n, primes):
    m = find_largest_prime_leq(n, primes)
    pnum = list_primes_till(m, primes)
    return count_consecutive_prime_sums(n, pnum)

def main():
    PRIME_LIMIT = 10000
    SIEVE_LIMIT = 100
    primes = initialize_primes(PRIME_LIMIT)
    sieve(primes, SIEVE_LIMIT)
    while True:
        n = get_input()
        if n == 0:
            break
        ans = solve_case(n, primes)
        print(ans)

main()