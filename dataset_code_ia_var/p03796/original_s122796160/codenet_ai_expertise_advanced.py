from math import prod

n = int(input())

mod = 10**9 + 7
result = prod(range(1, n + 1)) % mod

print(result)