from functools import reduce
import itertools

O, E = (input() for _ in range(2))

pairs = list(itertools.zip_longest(O, E, fillvalue=''))
S = reduce(lambda acc, tpl: acc + ''.join(filter(None, tpl)), pairs, '')
print(S)