from functools import reduce
from operator import mul

a, b = map(int, (__import__('sys').stdin.readline()).split())

cases = {
    True: lambda: reduce(lambda x, y: x + y, [a, a - 1]),
    False: lambda: None  # Placeholder
}
cases_eq = {
    True: lambda: reduce(mul, [a, 2]),
    False: lambda: reduce(lambda x, y: x + y, [b, b - 1])
}
print([
    cases[a > b](),
    cases_eq[a == b]()
][0 if a > b else 1])