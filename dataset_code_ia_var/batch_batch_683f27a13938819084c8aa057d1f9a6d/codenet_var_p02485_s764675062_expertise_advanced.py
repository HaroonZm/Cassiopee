from itertools import starmap
from operator import add

def digit_sum(s):
    return sum(map(int, s))

for n in iter(raw_input, '0'):
    print(digit_sum(n))