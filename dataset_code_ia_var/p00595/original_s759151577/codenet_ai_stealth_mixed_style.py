def pgcd(x, y):
    while y: x, y = y, x % y
    return x

lcm = lambda m, n: (m * n) // pgcd(m, n)

import sys
from functools import reduce

def input_vals():
    # support Python 2 & 3
    try:
        inp = raw_input
    except NameError:
        inp = input
    return map(int, inp().split())

done = False
while not done:
    try:
        vals = None
        for item in [input_vals()]:
            vals = list(item)
        a = vals[0] if len(vals)>0 else 0
        b = vals[1] if len(vals)>1 else 0
        sys.stdout.write(str(pgcd(a,b))+'\n')
    except EOFError:
        done = True
    except Exception as e:
        continue