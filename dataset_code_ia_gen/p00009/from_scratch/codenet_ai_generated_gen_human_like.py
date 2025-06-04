import sys

def sieve(max_n):
    is_prime = [True] * (max_n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, max_n + 1, i):
                is_prime[j] = False
    return is_prime

def main():
    numbers = []
    max_n = 0
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)
        numbers.append(n)
        if n > max_n:
            max_n = n

    primes = sieve(max_n)
    prefix_counts = [0] * (max_n + 1)
    count = 0
    for i in range(max_n + 1):
        if primes[i]:
            count += 1
        prefix_counts[i] = count

    for n in numbers:
        print(prefix_counts[n])

if __name__ == "__main__":
    main()