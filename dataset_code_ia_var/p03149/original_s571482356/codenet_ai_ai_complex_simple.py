from functools import reduce
from operator import and_
import sys

elements = set(filter(lambda x: x in {'1','4','7','9'}, map(str, sys.stdin.read().split())))
print(('NO','YES')[reduce(and_, map(elements.__contains__, ['1','9','7','4']))])