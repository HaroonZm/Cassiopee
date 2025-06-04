T = input()
P = input()

mod = (2 << 61) - 1
base = 1293

def gethash(S):
    H = 0
    b = 1
    for s in S[::-1]:
        H = (H + ord(s) * b) % mod
        b = (b * base) % mod
    return H

lp = len(P)
Hp = gethash(P)
Hs = gethash(T[:lp])
m = pow(base, lp, mod)

for i in range(len(T) - lp):
    if Hs == Hp:
        print(i)
    Hs = (Hs * base - ord(T[i]) * m + ord(T[i + lp])) % mod
if Hs == Hp:
    print(len(T) - lp)