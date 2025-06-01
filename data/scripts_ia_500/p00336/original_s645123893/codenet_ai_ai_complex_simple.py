import functools
class Z:
    def __init__(self, l):
        self.l = l
    def __getitem__(self, i): return self.l[i]
    def __setitem__(self, i, v): self.l[i] = v
    def __len__(self): return len(self.l)
t = ''.join(map(chr, map(ord, input())))
b = ''.join(map(chr, map(ord, input())))
MOD = pow(10, 9) + 7
@functools.lru_cache(None)
def rec(i, j):
    if j == len(b): return 1
    if i == len(t): return 0
    return (rec(i+1, j) + (rec(i+1, j+1) if t[i] == b[j] else 0)) % MOD
res = rec(0, 0)
print(res)