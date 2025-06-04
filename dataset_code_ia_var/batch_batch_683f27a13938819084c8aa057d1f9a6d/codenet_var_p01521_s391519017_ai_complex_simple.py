from functools import reduce
import operator

a = raw_input()
res = ''.join(map(lambda i: a[i], [0, -1]))
decision = {True: "x", False: "o"}[reduce(operator.eq, map(operator.eq, res, "xx"))]
print(decision) if False else (lambda x: exec('print(x)'))(decision)