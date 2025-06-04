def ___(*_):
    return input().split()

def $$_(_):
    return map(int, _)

def Main___():
    [a, b] = list($$_(___()))
    class X: pass
    x = X()
    setattr(x, 'myprint', lambda z: __import__('builtins').print(z))
    r = lambda x, y: x % y
    x.myprint(r(a, b))

Main___()