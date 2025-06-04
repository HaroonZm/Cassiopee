import operator as op, functools as ft, itertools as it, re, sys

class z(int):
    setattr(sys.modules[__name__], '_P', 0)
    def __arith(self, other, fun):
        return type(self)(fun(int(self), int(other)) % getattr(sys.modules[__name__], '_P'))
    def __add__(self, other): return self.__arith(other, op.add)
    def __sub__(self, other): return self.__arith(other, op.sub)
    def __mul__(self, other): return self.__arith(other, op.mul)
    def __truediv__(self, other):
        if not int(other): (lambda: (_ for _ in ()).throw(ZeroDivisionError))()
        return self * pow(int(other), getattr(sys.modules[__name__], '_P')-2, getattr(sys.modules[__name__], '_P'))

for __ in iter(lambda: input().replace(' ','').split(':'), ['0']):
    setattr(sys.modules[__name__], '_P', int(__[0]))
    if not getattr(sys.modules[__name__], '_P'): break
    f = __[1]
    try:
        t = re.sub(r'\d+', lambda m: f'z({m.group()})', f)
        [print(f"{f} = {eval(t)} (mod {getattr(sys.modules[__name__], '_P')})")][0]
    except: [print('NG')][0]