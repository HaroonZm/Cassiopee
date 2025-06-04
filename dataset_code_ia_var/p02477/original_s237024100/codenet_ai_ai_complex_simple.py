from functools import reduce
from operator import mul

exec('globals().update(dict(zip("AB".split(),map(int,input().split()))))')
print(reduce(mul, [globals()[c] for c in "AB"]))