import functools
import itertools
c = functools.reduce(lambda _, __: input(), range(1), None)
res = next(itertools.starmap(chr, [(ord(c)+1,)]))
print(res)