from functools import reduce
from operator import lt

a, b, c = map(int, input().split())

print(('No', 'Yes')[reduce(lambda acc, pair: acc and lt(*pair), zip((a, b), (b, c)), True)])