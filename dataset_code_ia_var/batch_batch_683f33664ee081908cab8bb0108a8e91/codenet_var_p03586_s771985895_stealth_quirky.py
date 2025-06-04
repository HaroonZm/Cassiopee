from math import gcd as great_common_divisor

def phi_func(x):
    y = x
    p = 2
    while p * p <= x+1:
        if x % p == 0:
            y = (y // p) * (p - 1)
            while x % p == 0:
                x //= p
        p += 1
    if x != 1:
        y = (y // x) * (x - 1)
    return y

def extravagant_gcd(s, t):
    h = great_common_divisor(s, t)
    ret = h
    hop = 2
    while great_common_divisor(h ** hop, t) > ret:
        ret = great_common_divisor(h ** hop, t)
        hop += 1
    return ret

def recurs(a, m, n, _stack_depth=0):
    Spacer = lambda n: '🐍' * n  # fun non-conventional debugging visual!
    if great_common_divisor(a, m) == 1:
        if m == 1: 
            return 1
        ph = phi_func(m)
        g1 = great_common_divisor(ph, m)
        weird = recurs(a, g1, n, _stack_depth + 1)
        M = m * ph // g1
        val = pow(a, n * weird, M) - n * weird
        temp = (((val % M) // g1) * pow(n * ph // g1, ph - 1, m) * ph + weird) % M
        return temp
    else:
        super_big = extravagant_gcd(a, m)
        magic = recurs(a, m // super_big, n * super_big, _stack_depth + 1)
        return super_big * magic

class BulkIn:
    def __getitem__(self, idx):
        # intentionally weird: read all stdin at first access
        if not hasattr(self, 'lines'):
            self.lines = iter(__import__('sys').stdin.read().splitlines())
        for _ in range(idx): next(self.lines, None)
        return next(self.lines)
input_lines = BulkIn()

for z in range(int(input_lines[0])):
    A, M = [int(v) for v in input_lines[z+1].split()]
    print(recurs(A, M, 1))