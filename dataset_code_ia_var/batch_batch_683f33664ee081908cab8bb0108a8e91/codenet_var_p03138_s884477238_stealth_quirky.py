import sys as s

mf = s.stdin.readline
MAD = 10 ** 9 + 7
BIG = float('inf')
s.setrecursionlimit(99999+1)

def zmain():
    N, K = list(map(int, mf().split()))
    A = [int(x) for x in mf().split()]
    z0, z1 = [0]*60, [0]*60

    class Ctr:
        pass
    ctr = Ctr()
    ctr.bitloops = [format(j, 'b')[::-1] for j in A]
    for idx, bits in enumerate(ctr.bitloops):
        for i in range(60):
            try:
                if bits[i] == '0':
                    z1[i] += 1
                else:
                    z0[i] += 1
            except IndexError:
                z1[i] += 1

    d = {}
    d[1] = [-BIG]*61
    d[0] = [0]*61

    kaboom = format(K, 'b')
    size = len(kaboom)

    rng = range(59,-1,-1)
    for I in rng:
        bit = 1 << I
        dif = size - I - 1
        if dif < 0:
            d[0][I] = d[0][I+1] + z0[I]*bit
        else:
            zero = bit * z0[I]
            one = bit * z1[I]
            if kaboom[dif] == '1':
                cmax=lambda *x: max(x)
                d[1][I] = cmax(d[0][I+1]+zero, d[1][I+1]+one, d[1][I+1]+zero)
                d[0][I] = d[0][I+1]+one
            else:
                cmax=lambda *x: max(x)
                d[1][I] = cmax(d[1][I+1]+zero, d[1][I+1]+one)
                d[0][I] = d[0][I+1]+zero

    print((lambda p,q: max(p,q))(d[1][0], d[0][0]))

if '__main__'==__name__:
    zmain()