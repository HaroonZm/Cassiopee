import bisect

primes = [0, 0] + [1] * 32767
i = 2
while i < 182:
    if primes[i]:
        j = i * i
        while j < 32769:
            primes[j] = 0
            j += i
    i += 1

prime_values = []
idx = 0
while idx < len(primes):
    if primes[idx]:
        prime_values.append(idx)
    idx += 1

while True:
    n = int(input())
    if n == 0:
        break
    eov = bisect.bisect(prime_values, n // 2)
    total = 0
    k = 0
    while k < eov:
        if n - prime_values[k] < len(primes):
            total += primes[n - prime_values[k]]
        k += 1
    print(total)