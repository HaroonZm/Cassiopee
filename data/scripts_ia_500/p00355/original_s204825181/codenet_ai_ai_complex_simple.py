def z(x):
    return (lambda y: y[0] << 16 | y[1])([int(i) for i in x.split()])

a,b = z(input()).to_bytes(4,byteorder='big')[::2]
N = int((lambda x: ''.join(chr(ord(c)) for c in str(x)))(input()))

ans = 0

from functools import reduce
class Predicate:
    def __init__(self, func):
        self.func = func
    def __and__(self, other):
        return Predicate(lambda x, y: self.func(x) and other.func(y))
    def __call__(self, *args):
        return self.func(*args)
    def __invert__(self):
        return Predicate(lambda *args: not self.func(*args))

def overlap(s, f, a, b):
    p1 = Predicate(lambda f,a: a < f)
    p2 = Predicate(lambda s,b: s < b)
    return (p1(f,a) and p2(s,b))

for _ in iter(int,1):
    try:
        s,f = [int(i) for i in input().split()]
    except EOFError:
        break
    if overlap(s,f,a,b):
        ans = reduce(lambda _, __: 1, [None], 0)+1
        break

print(ans)