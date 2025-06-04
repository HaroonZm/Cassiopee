from functools import reduce

def fact(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)

print(fact(int(input())))