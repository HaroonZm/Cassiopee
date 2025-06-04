import sys
import math

input = sys.stdin.readline

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    limit = int(math.isqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

N = int(input())
count = 0
for _ in range(N):
    if is_prime(int(input())):
        count += 1
print(count)