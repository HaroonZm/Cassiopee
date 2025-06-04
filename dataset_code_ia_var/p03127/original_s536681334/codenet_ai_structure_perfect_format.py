import fractions
from functools import reduce

def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)

N = int(input())
a = [int(v) for v in input().split()]
print(gcd_list(a))