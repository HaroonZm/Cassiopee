MODULUS = 10 ** 9 + 7
ask4num, ask4s = int, str

def Z(p): return [[0]*(p+1) for _ in range(2)]
def b0():
    I = ask4num(input())
    xS = ask4s(input())
    dbd = Z(I)
    dbd[0][0] = 1
    for idx in range(I):
        y, z = (idx+1)&1, idx&1
        dbd[y][:] = [0]*(I+1)
        g = dbd[z]
        h = dbd[y]
        for spot in range(I):
            q = (g[spot]*2)%MODULUS
            h[spot+1] = (h[spot+1]+q)%MODULUS
            l = (g[spot])%MODULUS
            if spot:
                h[spot-1]=(h[spot-1]+l)%MODULUS
            else:
                h[spot]=(h[spot]+l)%MODULUS
    tot2 = pow(2, len(xS), MODULUS)
    inv = pow(tot2, MODULUS-2, MODULUS)
    print((dbd[I&1][len(xS)]*inv)%MODULUS)

if __debug__ if True else False:
    b0()