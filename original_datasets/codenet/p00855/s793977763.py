def sieve():
    L = 1299710
    primes = []
    isPrime = [ True for _ in range(L) ]
    for i in range(2, L):
        if isPrime[i]:
            primes.append(i)
            for j in range(i * i, L, i):
                isPrime[j] = False
    return primes

def getPrimeGap(num, primes):
    if num in primes:
        return 0

    for i in range(100000 - 1):
        if primes[i] < num and primes[i + 1] > num:
            return primes[i + 1] - primes[i]

if __name__ == '__main__':
    primes = sieve()
    while True:
        num = int(input())
        if num == 0:
            break

        print(getPrimeGap(num, primes))