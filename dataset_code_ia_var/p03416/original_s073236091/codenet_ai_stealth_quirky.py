import builtins

def _(_0, _1):
    return getattr(builtins, _0)(_1)

(x, y) = tuple(list(map(lambda z: int(z[::-1][::-1]), _('__builtins__'[::-1][::-1], 'input').split())))
O0O = []
for Q in range(x, y+1):
    Zz = str(Q)
    L12 = len(Zz)//2
    if Zz[:L12] == Zz[:-L12-1:-1]:
        O0O += [None]
_('print', len(O0O))