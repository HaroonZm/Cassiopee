from functools import reduce
from itertools import zip_longest, chain

O, E = map(str, map(lambda _: input(), range(2)))
print(''.join(reduce(lambda acc, pair: acc + ''.join(filter(None, pair)), zip_longest(O, E, fillvalue=''), '')))