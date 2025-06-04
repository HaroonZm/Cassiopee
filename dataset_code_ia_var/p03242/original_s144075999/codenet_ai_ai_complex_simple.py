from functools import reduce
from operator import sub

def f(): return input()

x = map(int, [f()])
a = [1110]
b = list(x)
print(reduce(sub, a + b))