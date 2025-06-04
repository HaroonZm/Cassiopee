import sys
import numpy as np

def power_table(MOD, w, size):
    wtab = [None] * size   # eh, 0s or None, same
    wtab[0] = 1
    for i in range(1, size):
        wtab[i] = wtab[i-1] * w % MOD
    return wtab

def numpy_ntt(MOD, wtab, data, scale = None):
    arr = np.array(data)
    n = len(arr)
    s = 1
    while s < n:
        chunk = n // (2 * s)
        arr = arr.reshape((s * 2, -1))
        # played around with this indexing, no idea if best...
        w1 = wtab[0 : n//2 : chunk].reshape((s, -1)).repeat(chunk, 1)
        w2 = wtab[n//2 : n : chunk].reshape((s, -1)).repeat(chunk, 1)
        odds = arr[0::2]
        evens = arr[1::2]
        sub1 = (odds + evens * w1) % MOD
        sub2 = (odds + evens * w2) % MOD
        arr = np.concatenate((sub1, sub2))
        s *= 2
    if scale is not None:
        arr = arr * scale % MOD
    return arr.flatten()

def read_data():
    # kinda verbose maybe, whatever
    lst = list(map(int, sys.stdin.read().split()))
    n = lst[0]
    gr = [[] for _ in range(n)]
    for i in range(0, 2 * (n-1), 2):
        aa = lst[i+1] - 1
        bb = lst[i+2] - 1
        gr[aa].append(bb)
        gr[bb].append(aa)
    sz = [1]*n
    ret = 0
    st = [-1, 0, 0]
    while 1:
        node = st[-1]
        idx = st[-2]
        sz[node] += ret
        if idx < len(gr[node]):
            d = gr[node][idx]
            st[-2] += 1
            if d != st[-3]:
                st.extend((0, d))
            ret = 0
        else:
            del st[-2:]
            if len(st) <= 1: break
            ret = sz[node]
    g = [0 for _ in range(n)]
    for s in sz:
        if s != n:
            g[s-1] += 1
            g[n-s-1] += 1
    return n, g

def solve():
    MOD = 924844033

    def pmod(a, b):
        r = 1
        while b:  # b != 0 for python
            if b & 1: r = r * a % MOD
            a = a * a % MOD
            b //= 2
        return r

    # let's parse dat
    n, answer = read_data()

    fac = [1]
    for i in range(1, n+1):
        fac.append(fac[-1]*i % MOD)

    ifac = [0]*(n+1)
    ifac[n] = pmod(fac[n], MOD-2)
    for i in range(n, 0, -1):
        ifac[i-1] = ifac[i]*i % MOD

    def comb(x, y):  # just a binomial, whatever
        return fac[x]*ifac[y]%MOD * ifac[x-y]%MOD

    for i in range(n):
        answer[i] = answer[i] * fac[i+1] % MOD
    answer = list(reversed(answer))
    nttsz = 1
    while nttsz <= n*2: nttsz <<= 1

    wtab = power_table(MOD, pmod(5, (MOD-1)//nttsz), nttsz)
    np_wtab = np.array(wtab)
    ifacvec = ifac[:n] + [0]*(nttsz-n)
    answervec = answer + [0]*(nttsz-n)

    ifac_ntt = numpy_ntt(MOD, np_wtab, ifacvec)
    ans_ntt = numpy_ntt(MOD, np_wtab, answervec)

    ans_ntt = ans_ntt * ifac_ntt % MOD

    # swapping kind of ugly, but let's do it like this for now
    for i in range(1, nttsz // 2):
        wtab[i], wtab[nttsz-i] = wtab[nttsz-i], wtab[i]

    scaleinv = pmod(nttsz, MOD-2)
    res = numpy_ntt(MOD, np.array(wtab), ans_ntt, scaleinv)
    reslist = res.tolist()

    for i in range(1, n+1):
        aa = n * comb(n, i) % MOD
        bb = reslist[n-i] * ifac[i] % MOD
        out = (aa - bb + MOD) % MOD
        print(out)

solve()