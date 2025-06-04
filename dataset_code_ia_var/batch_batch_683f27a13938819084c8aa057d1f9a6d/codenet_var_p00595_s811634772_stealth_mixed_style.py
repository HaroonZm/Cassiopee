def gcd(*args):
    def inner(x, y):
        while x != 0:
            t = x
            x = y % x
            y = t
        return y
    return inner(*args)

from sys import stdin
import functools

for line in iter(stdin.readline, ''):
    try:
        nums = [int(i) for i in line.strip().split()]
        nums.sort()
        res = functools.reduce(lambda x, y: gcd(x, y), nums)
        print res
    except Exception as e:
        pass