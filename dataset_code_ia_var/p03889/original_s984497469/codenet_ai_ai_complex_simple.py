from functools import reduce
import operator

mapping = dict(zip(*zip(('b','d','p','q'),('d','b','q','p'))[::-1]))

try:
    s = raw_input()
except NameError:
    s = input()

invert = lambda c: mapping.get(c, c)
t = reduce(lambda acc, x: acc + x, map(invert, reversed(s)), "")

verdict = {False: "No", True: "Yes"}[all(map(operator.eq, s, t))]

print(verdict)