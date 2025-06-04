from functools import reduce
from operator import add
import itertools

inputs = list(map(int, ' '.join([input(), input()]).split()))
groups = list(zip(*[iter(inputs)]*4))

sums = list(map(lambda g: reduce(add, g), groups))
result = list(itertools.dropwhile(lambda x: x != max(sums), sums))[0]

print(result)