primes = [0, 0] + [1]*9999
for i in range(2, 100):
    for j in range(i*i, 10001, i):
        primes[j] = 0

while True:
    n = int(input())
    if n == 0:
        break
    for i in range(2, n+1)[::-1]:
        if primes[i-2] and primes[i]:
            print(i-2, i)
            break