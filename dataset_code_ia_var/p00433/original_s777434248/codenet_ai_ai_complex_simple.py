from functools import reduce
from operator import add, itemgetter

fetch = lambda: tuple(map(int, __import__('builtins').raw_input().split()))
a, b = fetch(), fetch()

totals = tuple(map(lambda x: reduce(add, x), (a, b)))
winner = max(enumerate(totals), key=itemgetter(1))[1] if totals[0]!=totals[1] else totals[0]
print((lambda x: x)(winner))