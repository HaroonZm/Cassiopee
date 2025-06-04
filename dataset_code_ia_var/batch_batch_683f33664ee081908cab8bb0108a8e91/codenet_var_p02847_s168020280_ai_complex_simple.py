from functools import reduce
from operator import eq, mul

s = input()
days = ['MON','TUE','WED','THU','FRI','SAT','SUN']
vals = [6,5,4,3,2,1,7]
print(reduce(lambda x, y: mul(y[0], eq(s, y[1])) + x, zip(vals, days), 0) + (s=='SUN')*7)