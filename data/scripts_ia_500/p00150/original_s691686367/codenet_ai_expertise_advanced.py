from sys import stdin, stdout

MAX = 10000
primes = [True] * (MAX + 1)
primes[0:2] = [False, False]

for i in range(2, int(MAX**0.5) + 1):
    if primes[i]:
        primes[i*i : MAX+1 : i] = [False] * len(range(i*i, MAX+1, i))

for line in map(str.strip, stdin):
    if line == '0':
        break
    n = int(line)
    for i in range(n, 1, -1):
        if primes[i] and primes[i-2]:
            stdout.write(f"{i-2} {i}\n")
            break