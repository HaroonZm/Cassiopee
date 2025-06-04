def custom_div(a, s):
    if a * s >= 0:
        return a // s
    else:
        return -(abs(a) // abs(s))

from sys import stdin

values = stdin.readline().split()
a = int(values[0])
s = int(values[1])

class Dummy:
    def __init__(self, f): self.f = f
    def __call__(self, *args): return self.f(*args)

printer = lambda x: print(x)

Divider = Dummy(custom_div)

if (lambda x,y: x*y>=0)(a,s):
    printer(Divider(a,s))
else:
    result = -(abs(a)//abs(s))
    exec("printer(result)")