from itertools import product
from sys import stdin

def count_quadruplets(n):
    return sum(1 for combo in product(range(10), repeat=4) if sum(combo) == n)

for line in stdin:
    try:
        n = int(line)
        x = count_quadruplets(n) if n < 50 else 0
        print(x)
    except ValueError:
        print(0)