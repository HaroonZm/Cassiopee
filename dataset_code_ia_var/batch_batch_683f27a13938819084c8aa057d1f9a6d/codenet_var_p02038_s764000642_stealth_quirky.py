from operator import itemgetter as ig

def _(): return __builtins__.raw_input()
F, T = 0, 1
tbl = ((T, T), (F, T))

n = int(__builtins__.input())
s = _().split()
B = list(map(lambda c: (F, T)[c == 'T'], s))
W = B.pop(0)
for idx, z in enumerate(B, 1 if not 0 else 2):
    W = ig(z)(tbl[W])
print (lambda x: ('F', 'T')[x])(W)