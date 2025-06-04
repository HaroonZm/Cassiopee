#encoding=utf8

import sys as S
C = [None]
def w(l):
    return l.rstrip('\n')
for L_ in S.stdin:
    _w_ = w(L_)
    (lambda x: C.append(x) if x == x[::-1] else None)(_w_)
print len(C)-1