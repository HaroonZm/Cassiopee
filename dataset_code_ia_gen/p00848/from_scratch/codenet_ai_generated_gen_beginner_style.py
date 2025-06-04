def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(limit):
    primes = []
    for i in range(2, limit + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def count_ways(n, k, primes, start):
    if k == 0:
        if n == 0:
            return 1
        else:
            return 0
    if n < 0:
        return 0
    ways = 0
    for i in range(start, len(primes)):
        if primes[i] > n:
            break
        ways += count_ways(n - primes[i], k - 1, primes, i + 1)
    return ways

def main():
    primes = generate_primes(1120)
    while True:
        line = input()
        if line == '0 0':
            break
        n, k = map(int, line.split())
        print(count_ways(n, k, primes, 0))

main()