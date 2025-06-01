MAX = 10**6
SQRT = int(MAX**0.5) + 1

comp = bytearray(MAX + 1)
comp[0:2] = 1, 1  # 0 and 1 are not prime

for i in range(3, SQRT, 2):
    if not comp[i]:
        comp[i*i:MAX+1:i] = b'\x01' * len(comp[i*i:MAX+1:i])

# Precompute prefix sums of primes
tbl = [0] * (MAX + 1)
count = 1  # count primes, starts from 2
tbl[2] = count
for i in range(3, MAX + 1, 2):
    if not comp[i]:
        count += 1
    tbl[i] = count
    tbl[i - 1] = count  # fill even indices

import sys
input = sys.stdin.readline

while (line := input().strip()) != '0':
    n = int(line)
    ans = 0
    for _ in range(n):
        p, m = map(int, input().split())
        a, b = max(p - m, 2), min(p + m, MAX)
        # Calculate primes in (a, b) excluding endpoints
        res = tbl[b - 1] - tbl[a]
        ans += max(res, 0)
    print(ans)