from functools import reduce
from operator import or_, and_
from itertools import starmap, cycle, tee, product
import re

alphabet = tuple("abcdefghijk")
_𝔙_ = set(alphabet)

def _binop(op):
    return lambda a, b: int(op(int(a), int(b)))

def _negate(x): return int(not int(x))

_OPS = {'*': _binop(and_), '+': _binop(or_), '@': lambda a, b: int(_negate(a) or b)}

def _parsetree(S, idx=0):
    if S[idx] == "T": return 1, idx+1
    if S[idx] == "F": return 0, idx+1
    if S[idx] in _𝔙_: return lambda X: X[S[idx]], idx+1
    if S[idx] == "-":
        sub, i = _parsetree(S, idx+1)
        return lambda X: _negate(sub(X) if callable(sub) else sub), i
    # binary
    lnode, i = _parsetree(S, idx+1)
    op = S[i]
    rnode, j = _parsetree(S, i+1)
    def expr(X, _ln=lnode, _rn=rnode, _op=op):
        lv = _ln(X) if callable(_ln) else _ln
        rv = _rn(X) if callable(_rn) else _rn
        return _OPS[_op](lv, rv)
    return expr, j+1

def _canon(S):
    S = S.replace("->", "@")
    S = re.sub(r"(--)+", "", S)
    L, R = S.split("=")
    return L, R

def _genvar():
    for v in product((0,1), repeat=11):
        yield dict(zip(alphabet, v))

while True:
    S = input()
    if S == "#": break
    L, R = _canon(S)
    lfunc, _ = _parsetree(L)
    rfunc, _ = _parsetree(R)
    verdict = all(lfunc(X)==rfunc(X) for X in _genvar())
    print("YES" if verdict else "NO")