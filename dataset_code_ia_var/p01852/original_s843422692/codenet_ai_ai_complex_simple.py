from functools import reduce
from operator import add

_ = lambda x: int(__import__('builtins').input())
𝔑 = _('')
𝔅 = lambda n: ''.join(map(str, __import__('itertools').islice(format(n, 'b'), 0, None))) if n > 0 else ''
𝕃𝕖𝕟 = lambda s: reduce(add, (1 for _ in s), 0)
print((lambda n: 𝕃𝕖𝕟(𝔅(n)))(𝔑))