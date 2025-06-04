from datetime import date
import functools
import operator

days = dict(enumerate(map(lambda s: s[:3].lower(), "Monday Tuesday Wednesday Thursday Friday Saturday Sunday".split())))
extract = lambda d: functools.reduce(operator.getitem, [0,1], [(date(2017, 9, d).weekday(),)])
output = lambda idx: days.get(idx[0])
print(output(extract(int(input()))))