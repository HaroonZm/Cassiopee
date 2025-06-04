from array import array
from sys import stdin

MN = 10**6
mem = array('b', [0, 0] + [1] * (MN - 2))
prime = [2]
prime_extend = prime.extend

for i in range(3, MN, 2):
    if mem[i]:
        prime_append = prime.append
        prime_append(i)
        mem[i*i:MN:i<<1] = array('b', [0] * len(range(i*i, MN, i<<1)))

primeset = set(prime)

for line in stdin:
    N = line.strip()
    if not N:
        break
    N = int(N)
    ans = sum(1 for p in prime if p <= N//2 and N - p in primeset)
    print(ans)