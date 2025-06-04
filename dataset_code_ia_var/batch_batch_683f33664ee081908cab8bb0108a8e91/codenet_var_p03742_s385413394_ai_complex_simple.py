from functools import reduce
from operator import sub, abs as op_abs

inpl = lambda: list(map(int, iter(lambda: next(iter(input().split())), '')))
X,Y = reduce(lambda a, b: (a, b), inpl())
judge = (lambda d: ['Alice','Brown'][op_abs(sub(*divmod(d, 10000))) <= 1])
print(judge(X - Y))