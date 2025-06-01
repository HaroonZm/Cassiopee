from functools import reduce
import operator
print('\n'.join(map(str, map(lambda x: reduce(operator.sub, x), [[*map(int, input().split())] for _ in range(7)]))))