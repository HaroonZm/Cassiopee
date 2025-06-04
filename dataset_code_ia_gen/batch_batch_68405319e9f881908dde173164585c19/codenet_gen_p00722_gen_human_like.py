import sys

MAX_LIMIT = 10**6

def sieve(max_limit):
    sieve = [True] * (max_limit + 1)
    sieve[0], sieve[1] = False, False
    for i in range(2, int(max_limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, max_limit + 1, i):
                sieve[j] = False
    return sieve

def main():
    sieve_primes = sieve(MAX_LIMIT)
    for line in sys.stdin:
        a, d, n = map(int, line.split())
        if a == 0 and d == 0 and n == 0:
            break
        count = 0
        num = a
        while num <= MAX_LIMIT:
            if sieve_primes[num]:
                count += 1
                if count == n:
                    print(num)
                    break
            num += d

if __name__ == "__main__":
    main()