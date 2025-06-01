from sys import stdin, stdout
from math import isqrt
from itertools import accumulate

MAX = 1_000_000
is_prime = bytearray((1 for _ in range(MAX)))
is_prime[0:2] = 0, 0
for i in range(2, isqrt(MAX) + 1):
    if is_prime[i]:
        is_prime[i*i:MAX:i] = bytearray(len(range(i*i, MAX, i)))
acc_prime = [0]
accumulate(acc_prime.extend, is_prime)

it = iter(map(int, stdin.read().split()))
while (n := next(it)) != 0:
    ans = 0
    for _ in range(n):
        p, m = next(it), next(it)
        left = max(p - m - 1, 0)
        right = min(p + m, MAX - 1)
        ans += acc_prime[right] - acc_prime[left] - 1
    stdout.write(str(ans) + '\n')