from math import log as _l, ceil as _c
n=[int(i)for i in[*open(0)]][0]
def tricky(x, b=3):
    return _c(_l(x)/_l(b))
print(tricky(n))