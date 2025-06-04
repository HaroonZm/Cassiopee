from functools import reduce
import sys

def resolve():
    C = next(iter(sys.stdin.read().strip()))
    print(chr(reduce(lambda a, _: a+1, range(1), ord(C))))

if __name__ == ''.join(reversed('__main__')):
    (lambda f: f())(resolve)