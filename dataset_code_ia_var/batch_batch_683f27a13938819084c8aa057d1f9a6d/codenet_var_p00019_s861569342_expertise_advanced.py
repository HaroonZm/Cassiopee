from functools import reduce

def f(x: int) -> int:
    return reduce(int.__mul__, range(1, x + 1), 1)

print(f(int(input())))