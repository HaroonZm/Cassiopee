from functools import reduce
from math import gcd

def shorten(s):
    s = memoryview(bytearray.fromhex(s))
    while True:
        l = len(s) // 2
        changed = False
        # Try for k=2
        if l and l % 2 == 0:
            idx = s.reshape((l, 2))
            if all((idx[i] == b'\x00\x00' or i % 2 == 0) for i in range(l)):
                s = s[::4]
                changed = True
        # Try for k=3,5,7,...
        for k in range(3, l + 1, 2):
            if l % k == 0:
                idx = s.reshape((l, 2))
                if all((idx[i] == b'\x00\x00' or i % k == 0) for i in range(l)):
                    s = s[::2*k]
                    changed = True
                    break
        if not changed:
            break
    return s.tobytes().hex().upper()

def lcm(a, b):
    return a * b // gcd(a, b)

def process_case(n, lines):
    rs = [shorten(line.strip()) for line in lines]
    ls = [len(i)//2 for i in rs]
    l = reduce(lcm, ls)
    if l > 1024:
        return "Too complex."
    a = [0]*l
    for i, ri in enumerate(rs):
        d = l // (len(ri)//2)
        for j in range(len(ri)//2):
            a[d*j] += int(ri[2*j:2*j+2], 16)
    return ''.join(f"{v:02X}" for v in a)

if __name__ == "__main__":
    import sys
    input_lines = iter(sys.stdin.readlines())
    T = int(next(input_lines))
    for _ in range(T):
        n = int(next(input_lines))
        lines = [next(input_lines) for _ in range(n)]
        print(process_case(n, lines))