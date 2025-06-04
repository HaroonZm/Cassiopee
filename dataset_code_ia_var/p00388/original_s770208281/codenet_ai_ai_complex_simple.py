from functools import reduce
from itertools import starmap

h, a, b = map(int, input().split())

def is_divisor(x):
    return not h % x

ans = sum(starmap(lambda x, y: is_divisor(x) and y, zip(range(a, b+1), [1]*(b-a+1))))
print(ans)