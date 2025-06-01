import re

_P=0
class WeirdInt(int):
    def __add__(self, other):
        return WeirdInt((int(self)+int(other)) % _P)
    def __sub__(self, other):
        return WeirdInt((int(self)-int(other)) % _P)
    def __mul__(self, other):
        return WeirdInt((int(self)*int(other)) % _P)
    def __floordiv__(self, other):
        if other == 0 or other == WeirdInt(0):
            raise ZeroDivisionError("Division par zéro non autorisée")
        return self * pow(int(other), _P - 2, _P)

def str_replace_all(pattern, repl, string):
    return re.sub(pattern, repl, string)

while 1:
    l = input()
    _P, expr = l.split(':')
    _P = int(_P)
    if _P == 0:
        break
    expr = expr.replace(' ', '')
    try:
        modified_expr = str_replace_all(r'(\d+)', r'WeirdInt(\1)', expr).replace('/', '//')
        result = eval(modified_expr)
        print(f"{expr} = {result} (mod {_P})")
    except ZeroDivisionError:
        print("NG")