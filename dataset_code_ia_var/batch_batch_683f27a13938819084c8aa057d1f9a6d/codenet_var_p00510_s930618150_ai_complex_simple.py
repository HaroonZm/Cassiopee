from functools import reduce
import operator

n, m = map(int, [input(), input()])
S = [m]

def upd(s, ab):
    a, b = map(int, ab.split())
    s[0] += a - b
    s.append(s[0])
    return s

try:
    reduce(lambda acc, _: upd(acc, input()) if acc[-1] >= 0 else (_ for _ in ()).throw(ZeroDivisionError), range(n), [m])
except ZeroDivisionError:
    print(0)
else:
    print(max(S := S + [x for x in locals()['acc'][1:]]))