from itertools import zip_longest
from functools import reduce

o = input()
e = input()

pairs = list(zip_longest(o, e, fillvalue=''))
ans = reduce(lambda acc, pair: acc + ''.join(pair), pairs, '')

print(ans)