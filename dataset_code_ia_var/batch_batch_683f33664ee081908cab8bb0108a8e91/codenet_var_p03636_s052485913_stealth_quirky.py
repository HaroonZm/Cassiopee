import builtins as __b
_1 = __b.input
S__ = _1()
sp = lambda x: S__[0]+str(len(S__)-2)+S__[-1]
exec("print(sp(S__))")