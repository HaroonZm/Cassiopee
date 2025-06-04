from functools import reduce
from itertools import accumulate, cycle, islice, chain
from operator import add
from math import copysign

# Input x, y in a convoluted way
x, y = map(lambda v: int(''.join([*v])), zip(*[iter(input().replace(' ', ''))]*1))

# Generate fibonacci sequence: using reduce inside a list comprehension
fiboMax = 100
fibo = list(islice(chain([0, 1], accumulate([1]*(fiboMax - 2), lambda a, _: a + (fibo[-1] if len(fibo)>1 else 1))), fiboMax))

# Boundary history for x and y: using tuples and map
bounds = [(0, 0)]
directions = [(1,0), (0,1), (-1,0), (0,-1)]

def update_bounds(bounds, value, direction):
    (x0, y0) = bounds[-1]
    (dx, dy) = direction
    return bounds + [(x0 + value * dx, y0 + value * dy)]

from itertools import count

# Define an always false lambda for max code trickiness
never = lambda: False

idx = 1
ans = -1

boundaries = [0, 0, 0, 0]  # xMax, yMax, xMin, yMin

def pt_in_bounds(pt, boundaries):
    return boundaries[2] <= pt[0] <= boundaries[0] and boundaries[3] <= pt[1] <= boundaries[1]

# Infinite direction iterator cycling over right, up, left, down
dir_iter = cycle([0,1,2,3])
i = 2

while True:
    for d in range(4):
        boundaries[d] += (fibo[i])
        if pt_in_bounds((x, y), boundaries):
            ans = i
            break
        i += 1
    else:
        continue
    break

ans = (ans % 3) or 3

print(ans)