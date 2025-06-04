def solve():
    N, K = map(int, input().split())
    As = list(map(int, input().split()))
    As.sort()
    # Get Bs: numbers strictly less than K
    Bs = []
    for a in As:
        if a < K:
            Bs.append(a)
        else:
            break
    M = len(Bs)

    # Make bitsets (possible sums)
    bitsets = []
    bit = 0
    bit = 1 << (K-1)
    bitsets.append(bit)
    for i in range(M):
        b = Bs[i]
        bit = bit | (bit >> b)
        bitsets.append(bit)

    rev_bitsets = []
    bit = 1 << (K-1)
    rev_bitsets.append(bit)
    for i in range(M-1, -1, -1):
        b = Bs[i]
        bit = bit | (bit >> b)
        rev_bitsets.append(bit)
    rev_bitsets.reverse()

    def isOK(x):
        B = Bs[x]
        numRevs = []
        bit = rev_bitsets[x+1]
        for i in range(K):
            if bit & (1 << (K-1-i)):
                numRevs.append(1)
            else:
                numRevs.append(0)
        acc = [0]
        for v in numRevs:
            acc.append(acc[-1] + v)
        bit = bitsets[x]
        for i in range(K):
            if bit & (1 << (K-1-i)):
                right = K - i
                left = max(0, right - B)
                if acc[right] - acc[left] > 0:
                    return True
        return False

    ng = -1
    ok = M
    while abs(ok - ng) > 1:
        mid = (ng + ok) // 2
        if isOK(mid):
            ok = mid
        else:
            ng = mid
    print(ok)

solve()