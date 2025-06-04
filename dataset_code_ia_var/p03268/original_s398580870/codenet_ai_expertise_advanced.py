from sys import stdin

def count_tuples(n: int, k: int) -> int:
    cubes = lambda x: x * x * x
    base = cubes(n // k)
    if k & 1:
        return base
    half = cubes((n + (k >> 1)) // k)
    return base + half

n, k = map(int, stdin.readline().split())
print(count_tuples(n, k))