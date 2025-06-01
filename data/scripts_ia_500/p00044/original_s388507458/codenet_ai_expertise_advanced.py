from bisect import bisect
from sys import stdin, stdout

def sieve(n):
    p = [True] * (n + 1)
    p[:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if p[i]:
            p[i*i:n+1:i] = [False] * len(range(i*i, n+1, i))
    return [i for i, prime in enumerate(p) if prime]

primes = sieve(50021)

def solve(n):
    idx = bisect(primes, n)
    a = primes[idx-1] if idx else None
    b = primes[idx] if idx < len(primes) else None
    stdout.write(f"{a} {b}\n")

for line in stdin:
    n = int(line)
    solve(n)