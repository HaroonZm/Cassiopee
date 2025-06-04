from functools import reduce

L = input()
mod = 1000000007

def calc(L, mod):
    f = 2
    nf = 1
    i = 1
    while i < len(L):
        x = int(L[i])
        if x == 1:
            nf = nf * 3 + f
            f <<= 1
        else:
            nf = nf * 3
        nf = nf % mod
        f = f % mod
        i += 1
    return (f + nf) % mod

ans = (lambda s, m: calc(s, m))(L, mod)
print(ans)