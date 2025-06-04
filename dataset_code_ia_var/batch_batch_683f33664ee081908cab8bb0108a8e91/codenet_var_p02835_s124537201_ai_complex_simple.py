from functools import reduce
from operator import add

A = list(map(int, map(str, input().split())))
judge = (lambda x: (lambda y: ["win", "bust"][y])(int(x >= 22)))
print(judge(reduce(add, A, 0)))