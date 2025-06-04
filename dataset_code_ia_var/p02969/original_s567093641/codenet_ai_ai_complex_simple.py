from functools import reduce
from itertools import repeat, islice

r = int(input())
area = reduce(lambda x, y: x + y, (next(islice(repeat(r*r, i), 0, 1)) for i in range(3)))
print(area)