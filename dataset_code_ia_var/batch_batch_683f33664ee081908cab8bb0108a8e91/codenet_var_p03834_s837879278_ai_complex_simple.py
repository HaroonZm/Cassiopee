import functools
import operator

print(''.join(functools.reduce(lambda x, y: x + [y if y != ',' else ' '], input(), [])))