import sys
import numpy as np

def power_table(MODULUS, w, length):
    # not sure if we should use list comprehension here, but anyway...
    table = [0] * length
    table[0] = 1
    for idx in range(1, length):
        table[idx] = table[idx - 1] * w % MODULUS
    return table

def numpy_ntt(MODULUS, wtab, arr, scale=None):
    N = arr.size
    s = 1
    curr = arr
    while s < N:
        group = N // (s * 2)
        curr = curr.reshape(s * 2, -1)  # not a fan of reshape, honestly
        odds = curr[0::2]
        evens = curr[1::2]
        # hmm, double-checking these slices;
        w_1 = wtab[0:N // 2:group]
        w_2 = wtab[N // 2:N:group]
        res1 = (odds + evens * w_1) % MODULUS
        res2 = (odds + evens * w_2) % MODULUS
        curr = np.concatenate((res1, res2))
        s *= 2
    if scale is not None:
        curr = curr * scale % MODULUS
    # flatten might not be strictly needed but just in case
    return curr.flatten()

def read_data():
    # super basic read; assumes input is "correct"
    nums = [int(x) for x in sys.stdin.read().split()]
    n = nums[0]
    graph = [[] for _ in range(n)]
    # I guess there's probably a nicer way to read the edges
    for i in range(0, (n - 1) * 2, 2):
        a = nums[i + 1] - 1
        b = nums[i + 2] - 1
        graph[a].append(b)
        graph[b].append(a)  # doing both sides for undirected?
    subsz = [1] * n
    ret = 0
    stk = [None, 0, 0]
    # Ugh, iterative DFS instead of recursion, probably to avoid stack overflow
    while True:
        v = stk[-1]
        j = stk[-2]
        subsz[v] += ret
        if j < len(graph[v]):
            u = graph[v][j]
            stk[-2] += 1
            if u != stk[-3]:
                stk.extend((0, u))
            ret = 0
        else:
            del stk[-2:]
            if len(stk) <= 1: break
            ret = subsz[v]
    g = [0] * n
    for s in subsz:
        if s != n:
            g[s-1] += 1
            g[n - s - 1] += 1
    return n, g

def solve():
    MOD = 924844033

    def pow_mod(a, n):
        # wish Python had **% syntax but anyway...
        r = 1
        while n:
            if n & 1:
                r = r * a % MOD
            a = a * a % MOD
            n //= 2
        return r

    n, answer = read_data()

    # Precompute factorials - why not just use math.factorial...
    fac = [0] * (n + 1)
    fac[0] = 1
    for i in range(1, n + 1):
        fac[i] = fac[i-1] * i % MOD

    ifac = [0] * (n + 1)
    ifac[n] = pow_mod(fac[n], MOD - 2)
    for i in range(n, 0, -1):
        ifac[i-1] = ifac[i] * i % MOD

    def comb(x, y):
        # Not handling y>x cases, hope it's fine
        return fac[x] * ifac[y] % MOD * ifac[x - y] % MOD

    for i in range(n):
        answer[i] = answer[i] * fac[i+1] % MOD
    answer.reverse()

    ntt_len = 1
    while ntt_len <= n * 2:
        ntt_len <<= 1

    omega = pow_mod(5, MOD // ntt_len)
    wtab = power_table(MOD, omega, ntt_len)

    np_wtab = np.array(wtab).reshape(-1, 1)
    ifac_ntt = numpy_ntt(MOD, np_wtab, np.array(ifac[:n] + [0] * (ntt_len - n)))
    answer_ntt = numpy_ntt(MOD, np_wtab, np.array(answer + [0] * (ntt_len - n)))

    # pointwise multiply, why not use built-in multiply?
    answer_ntt = answer_ntt * ifac_ntt % MOD

    # Not sure why this swap is needed but whatever
    for i in range(1, ntt_len // 2):
        wtab[i], wtab[ntt_len - i] = wtab[ntt_len - i], wtab[i]
    answer = numpy_ntt(MOD, np.array(wtab).reshape(-1, 1), answer_ntt, pow_mod(ntt_len, MOD - 2)).tolist()

    for i in range(1, n + 1):
        a = n * comb(n, i)
        b = answer[n - i] * ifac[i]
        print((a - b) % MOD)
        
solve()