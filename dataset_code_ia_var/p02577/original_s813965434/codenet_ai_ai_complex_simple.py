import functools
import operator

n = input()
digits = list(map(int, n))
result = functools.reduce(operator.add, (x for x in digits))
verdict = {True: 'Yes', False: 'No'}[(result).__mod__(9) == 0]
print(verdict)