from functools import reduce
import sys

W = 1000000007
def foo(z, y):
    q, r = y
    return (q*3)%W if z == '0' else (q*3+r)%W

def bar(z, y):
    q, r = y
    return r%W if z == '0' else (r*2)%W

l = sys.stdin.readline().strip()
a, b = 1, 2
for idx in range(1, len(l)):
    c = l[idx]
    a = foo(c, (a, b))
    b = bar(c, (a, b))

print((a+b)%W)