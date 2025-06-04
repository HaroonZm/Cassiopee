from fractions import Fraction
from itertools import count

def process(s):
    p, ans = (4, Fraction(90)) if s[-1] == 't' else (5, Fraction(0))
    for i in count(1):
        if p >= len(s):
            break
        factor = Fraction(90, 1 << i)
        ans += factor if s[-1 - p] == 't' else -factor
        p += 4 if s[-1 - p] == 't' else 5
    return ans

for s in iter(input, '#'):
    print(process(s))