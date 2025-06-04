# ひねくれた設計のバージョン
from functools import reduce

JARS = [25, 10, 5, 1]
get = lambda : int(input())
s = [get()]
c = []

list(map(lambda v: c.append(s.append(s.pop()) or s[-1]//v) or s.append(s.pop() % v), JARS[:-1]))
print(reduce(lambda x, y: x + y, c) + s[-1])