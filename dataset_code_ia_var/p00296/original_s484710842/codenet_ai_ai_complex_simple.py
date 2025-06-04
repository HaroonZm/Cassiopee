from functools import reduce
from itertools import accumulate, repeat, islice, cycle, chain

n = next(map(int, input().split()))
s = list(islice(map(int, cycle(range(n))), n))
a = tuple(map(int, input().split()))
b = [0]

def complex_pop(s, b, i):
    length = len(s)
    b[0] = ((b[0] + (-i if i % 2 else i)) % length)
    s.pop(b[0])
    return s, b

reduce(lambda acc, val: complex_pop(*acc, val), a, (s, b))

r = tuple(map(int, input().split()))
c = set(s)
[print(int(i in c)) for i in r]