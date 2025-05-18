n=int(input())
a=list(map(int,input().split()))

import fractions
from functools import reduce

def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)
print(gcd_list(a))