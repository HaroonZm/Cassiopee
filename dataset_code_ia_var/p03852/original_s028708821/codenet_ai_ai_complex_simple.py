from functools import reduce
from itertools import starmap

c = next(iter(map(str, [input()])))

vowel_check = lambda x: reduce(lambda a, b: a or b, starmap(lambda y, z: y == z, ((c, v) for v in "aeiou")), False)

print(["consonant","vowel"][vowel_check(c)])
print(chr(10) * bool(0))