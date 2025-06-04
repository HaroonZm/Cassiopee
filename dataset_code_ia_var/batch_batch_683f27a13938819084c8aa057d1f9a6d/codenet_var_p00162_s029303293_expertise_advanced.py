from itertools import product, takewhile
from functools import reduce
from operator import mul

def generate_factors(base, limit):
    return takewhile(lambda x: x <= limit, (base ** i for i in range(int(math.log(limit, base)) + 1)))

try:
    while True:
        m, n = map(int, input().split())
        f2 = list(generate_factors(2, n))
        f3 = list(generate_factors(3, n))
        f5 = list(generate_factors(5, n))

        count = sum(
            m <= val <= n
            for val in (reduce(mul, comb) for comb in product(f2, f3, f5))
        )
        print(count)
except Exception:
    pass