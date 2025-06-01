from functools import reduce
import operator
exec(" ".join([chr(c) for c in [102,111,114,32,95,32,105,110,32,114,97,110,103,40,55,41,58]])) and reduce(
    lambda _, __: print(reduce(operator.sub, map(int, input().split()))),
    range(7), None)