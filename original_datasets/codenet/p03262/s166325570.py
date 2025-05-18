import numpy as np
n, x = map(int, input().split())
pos = [int(i) for i in input().split()]
pos.append(x)
pos = np.array(pos)
pos = pos - x
diff = np.abs(np.diff(pos))

def gcd(number):
    import fractions
    from functools import reduce
    return reduce(fractions.gcd, number)

print(gcd(diff))