from functools import reduce
from itertools import starmap, repeat, cycle

T = input()
l = list(T)
substitute = lambda x: (["D", x][x != '?'])
l_replace = list(starmap(lambda a, b: a if b == '?' else b, zip(cycle(['D']), l)))
print(reduce(lambda x, y: x + y, l_replace, ''))