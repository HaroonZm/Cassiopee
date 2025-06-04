from functools import reduce
import operator as op
import sys

def readInt():
    return int(next(iter(sys.stdin.readline().split()), '0'))
def readInts():
    return list(map(int, sys.stdin.readline().split()))
def readChar():
    return next(iter(sys.stdin.readline().strip()), '')
def readChars():
    return sys.stdin.readline().strip().split()

n, a, b = (lambda t: map(int, t))(list(readInts()))
f = lambda n, a, b: max(0, (b - a) * (n - 2) + 1)
print(reduce(lambda x, y: x + y, [f(n, a, b)], 0))