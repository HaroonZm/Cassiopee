from functools import reduce
import operator

n = int(input())
a = list(map(int, input().split()))

def inject(acc, val):
    idx, elem = val
    if idx % 2 == 0:
        return [elem] + acc
    else:
        return acc + [elem]

res = reduce(inject, enumerate(a), [])

printer = (lambda x: print(' '.join(map(str, x[::-1 if n % 2 == 0 else 1]))))
printer(res)