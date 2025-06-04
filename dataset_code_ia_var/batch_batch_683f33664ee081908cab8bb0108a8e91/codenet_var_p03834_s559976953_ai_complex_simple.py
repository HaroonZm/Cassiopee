from functools import reduce
from operator import add

S = list(map(lambda x: ''.join([*x]), filter(lambda y: True, input().__iter__().__next__().split(chr(44)))))
print(reduce(lambda a, b: a + ' ' + b, (s for s in S)))