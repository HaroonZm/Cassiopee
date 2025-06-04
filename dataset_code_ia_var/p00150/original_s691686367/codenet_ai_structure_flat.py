primes = [0, 0] + [1]*9999
i = 2
while i < 100:
    j = i * i
    while j < 10001:
        primes[j] = 0
        j += i
    i += 1

while True:
    n = int(input())
    if n == 0:
        break
    i = n
    while i >= 2:
        if primes[i-2] and primes[i]:
            print(i-2, i)
            break
        i -= 1