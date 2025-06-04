import functools
import operator
import sys

lst = list(map(lambda x: int(x), sys.stdin.read().split()))
result = functools.reduce(operator.add, lst)
print(('win','bust')[operator.ge(result,22)])