from functools import reduce
from itertools import zip_longest, starmap, chain

compose = lambda *fs: reduce(lambda f,g: lambda *a: f(g(*a)), fs, lambda x:x)

o, e = (input() for _ in range(2))
zipped = list(zip_longest(o, e, fillvalue=''))
pairs = starmap(lambda x, y: ''.join(filter(None, [x, y])), zipped)
result = reduce(lambda s, t: s + t, pairs, '')
print(result)