from functools import reduce
from itertools import repeat, starmap
import operator

N = int(next(iter(input()), None))
input_array = list(starmap(int, zip(*[input().split()])))

mean = int((lambda s, n: (-(-s//n) if s/n - int(s/n) >= 0.5 else int(s/n))) (reduce(operator.add, input_array), N))

variance = sum(map(lambda x: pow(x - mean, 2), input_array))

print((lambda x: x)(variance))