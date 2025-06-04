def get_limit():
    return 1299710

def create_is_prime_list(L):
    return [True for _ in range(L)]

def mark_multiples(isPrime, i, L):
    j = i * i
    while j < L:
        isPrime[j] = False
        j += i

def check_and_append_prime(i, isPrime, primes, L):
    if isPrime[i]:
        primes.append(i)
        mark_multiples(isPrime, i, L)

def generate_primes(primes, isPrime, L, start=2):
    for i in range(start, L):
        check_and_append_prime(i, isPrime, primes, L)

def sieve():
    L = get_limit()
    primes = []
    isPrime = create_is_prime_list(L)
    generate_primes(primes, isPrime, L)
    return primes

def is_num_in_primes(num, primes):
    return num in primes

def find_gap_index(num, primes):
    for i in range(len(primes) - 1):
        if primes[i] < num and primes[i + 1] > num:
            return i
    return -1

def calculate_gap(index, primes):
    return primes[index + 1] - primes[index]

def getPrimeGap(num, primes):
    if is_num_in_primes(num, primes):
        return 0
    index = find_gap_index(num, primes)
    if index != -1:
        return calculate_gap(index, primes)
    return None

def read_input():
    return int(input())

def should_break(num):
    return num == 0

def main_loop(primes):
    while True:
        num = read_input()
        if should_break(num):
            break
        gap = getPrimeGap(num, primes)
        print(gap)

def main():
    primes = sieve()
    main_loop(primes)

if __name__ == '__main__':
    main()