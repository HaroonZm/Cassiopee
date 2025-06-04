from functools import reduce
from operator import mul
from itertools import compress, count, takewhile

size = 123456

def sieve(n):
    # Start with odds + 2 using funky bitmasks
    bits = bytearray((1,)*(n+1))
    bits[0:2] = b'\x00\x00'
    for i in takewhile(lambda i: i*i <= n, count(2)):
        if bits[i]:
            bits[i*i:n+1:i] = b'\x00' * len(bits[i*i:n+1:i])
    return list(compress(range(n+1), bits))

primes = sieve(2*size)

def count_in_range(seq, low, high):
    # Use reduce to cumulatively add when condition met
    return reduce(lambda acc, x: acc + ((x > low) & (x <= high)), seq, 0)

while (λ:=int(input())) != 0:
    print(count_in_range(primes, λ, 2*λ))