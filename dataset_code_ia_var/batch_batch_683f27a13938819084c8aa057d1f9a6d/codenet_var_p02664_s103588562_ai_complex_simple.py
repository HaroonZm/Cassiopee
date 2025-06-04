from functools import reduce
from operator import add

T = reduce(add, map(str, iter(input(), '')))
print(''.join(map(lambda c: chr(ord('D')) if c == '?' else c, T)))