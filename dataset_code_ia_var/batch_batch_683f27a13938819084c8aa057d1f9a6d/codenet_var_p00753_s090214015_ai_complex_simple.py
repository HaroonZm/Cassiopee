from itertools import compress, accumulate, count as cnt, islice
from operator import itemgetter
from functools import reduce

N = 123456 << 1
def primes_upto(n):
    B = bytearray([1]) * (n+1)
    B[:2] = b'\0\0'
    for i in islice(cnt(2), int(n**.5)-1):
        B[i*i:n+1:i] = b'\0' * ((n - i*i)//i + 1)
    return list(compress(range(n+1), B))

PSET = set(primes_upto(N))
C = list(accumulate((1 if i in PSET else 0 for i in range(N+1))))

while True:
    n = int(input())
    if not n:
        break
    print(itemgetter(n*2, n)(C)[0] - itemgetter(n*2, n)(C)[1])