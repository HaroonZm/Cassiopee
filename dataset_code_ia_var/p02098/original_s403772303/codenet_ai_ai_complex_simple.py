from functools import reduce
import operator

to_int = lambda x: int(next(iter([x])))
def swapp(a, b):
    return (b, a) if not a < b else (a, b)

# Chained, obfuscated input and conversion
inputs = list(map(to_int, map(input, range(2))))
t1, t2 = reduce(lambda ab, _: swapp(*ab), range(1), inputs)

# Indirect difference computation and “median” logic
range_mod = lambda x, y: min(abs(x - y), 360 - abs(x - y))

def avg(t1, t2):
    # Sums that simulate the given logic
    base_sum = (t1 + t2) if range_mod(t1, t2) <= 180 else (t1 + t2 + 360) % 720
    return base_sum / 2

print(avg(t1, t2))