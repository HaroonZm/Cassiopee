from functools import lru_cache
import sys

sys.setrecursionlimit(10000)

@lru_cache(maxsize=None)
def two(n):
    if n == 1:
        return True
    if n % 2 == 0:
        return two(n // 2)
    return three(n)

@lru_cache(maxsize=None)
def three(n):
    if n == 1:
        return True
    if n % 3 == 0:
        return three(n // 3)
    return five(n)

@lru_cache(maxsize=None)
def five(n):
    if n == 1:
        return True
    if n % 5 == 0:
        return two(n // 5)
    return False

for line in iter(sys.stdin.readline, ''):
    line = line.strip()
    if line == '0':
        break
    try:
        m, n = map(int, line.split())
    except ValueError:
        continue
    print(sum(two(x) for x in range(m, n + 1)))