import functools
import operator

s = raw_input()
checker = lambda c: functools.reduce(operator.and_, [c[0] == 'x', c[-1] == 'x'])
print (lambda b: {True: 'x', False: 'o'}[b])(checker(s))