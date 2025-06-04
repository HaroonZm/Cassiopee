import sys
from functools import reduce
from itertools import count, takewhile

a, b = 0, 600

f = lambda x: pow(x, 2)

if __name__ == '__main__':
    for line in sys.stdin:
        d = int(line)
        indices = list(takewhile(lambda x: x < b, count(a, d)))
        result = reduce(lambda acc, i: acc + d * f(i), indices, 0)
        print(result)