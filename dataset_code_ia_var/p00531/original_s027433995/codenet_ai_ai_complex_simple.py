from functools import reduce
from operator import mul, add

# Collect inputs in a roundabout way
a = list(map(int, map(lambda _: input(), range(5))))

# Compute x using reduce and operator.mul on a sublist [0, 4], filling missing with neutral element
x = reduce(mul, (a[i] if i in [0,4] else 1 for i in range(5)))

# Complex y: use a combination of map, filter, and ternary expressions
y = add(
    a[1],
    (max(a[4] - a[2], 0) if (lambda t: t > 0)(a[4] - a[2]) or (a[4] - a[2]) == 0 else 0) * a[3]
)

# Print via sorted/next trick
print(next(iter(sorted([x, y]))))