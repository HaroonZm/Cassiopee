from functools import reduce
from itertools import chain

c = reduce(lambda x, _: x, chain((input(),), ()), None)
advance = lambda ch: ''.join(map(chr, [(lambda code: code + 1)(ord(ch))]))
print(reduce(str.__add__, map(advance, c)))