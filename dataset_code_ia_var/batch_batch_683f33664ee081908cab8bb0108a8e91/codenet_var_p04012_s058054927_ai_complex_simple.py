from collections import Counter
from functools import reduce
from itertools import chain, repeat

a = input()
counter = Counter(a)
outcome = (lambda xs: reduce(lambda acc, x: acc and x, (v % 2 == 0 for v in xs.values()), True))(counter)
not_out = {False: lambda: print('No') or exit(), True: lambda: print('Yes')}
(list(chain.from_iterable(repeat(not_out[outcome](), 1))))