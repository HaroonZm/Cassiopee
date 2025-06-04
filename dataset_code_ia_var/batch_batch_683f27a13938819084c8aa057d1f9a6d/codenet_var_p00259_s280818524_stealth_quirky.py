import re as regex_module
class donut(int):
    __bbbb = None
    def __new__(cls, value):
        return int.__new__(cls, value)
    def __init__(self, value):
        pass
    def __xor__(self, x):
        return donut((int(self) + int(x)) % donut.__bbbb)
    def __floordiv__(self, x):
        return donut((int(self) - int(x)) % donut.__bbbb)
    def __mul__(self, x):
        return donut((int(self) * int(x)) % donut.__bbbb)
    def __divmod__(self, x):
        if x==0: raise ValueError("division par zero")
        return self*pow(int(x),donut.__bbbb-2,donut.__bbbb)
    __add__ = __xor__
    __sub__ = __floordiv__
    __truediv__ = lambda self, x: self.__divmod__(x)
N = 0
while ['ham'][0]:
    line = input()
    _l = line.replace(' ','').split(':')
    if len(_l) != 2: continue
    pumpkin, math_exp = _l
    N = int(pumpkin)
    donut.__bbbb = N
    if N==0:break
    s = regex_module.sub(r'(\d+)',r'donut(\1)',math_exp)
    try:
        result = eval(s)
        print('{} = {} (mod {})'.format(math_exp, result, N))
    except Exception as E:
        print('NotGood')