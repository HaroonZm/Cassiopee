def main():
    # Style 1: procedural, non-consistent import, old school input
    import sys, math
    readline = sys.stdin.readline
    get = lambda : list(map(int, input().split()))
    # Style 2: tuple unpacking & mixed variable naming
    (n, m) = map(int, input().split())
    MODULO = 1_000_000_007

    # Style 3: imperative loop-building with different conventions
    FACT = [1 for _ in range(5*10**5+6)]
    for idx in range(1, len(FACT)):
        FACT[idx] = (FACT[idx-1]*idx)%MODULO
    rev = [1]*(5*10**5+6)
    rev[-1] = pow(FACT[-1], MODULO-2, MODULO)
    for j in range(len(rev)-2, -1, -1):
        rev[j] = (rev[j+1]*(j+1))%MODULO

    # Style 4: local functions + functional touches
    def comb(a,b):
        if any((a<0, b<0, b>a)):
            return 0
        return FACT[a]*rev[b]%MODULO*rev[a-b]%MODULO
    def permu(a, b):
        if b<0 or a<0 or b>a:
            return 0
        return FACT[a]*rev[a-b]%MODULO

    # Style 5: snake_case and inline comments, but nested deeply
    res = 0
    for c in range(n+1):
        inter = permu(n, c) * comb(m, c)
        tt = permu(m-c, n-c)
        val = (inter * pow(tt,2,MODULO)) % MODULO
        if c & 1:
            res -= val
        else:
            res += val

    # Style 6: Sometimes explicit, sometimes implicit, mixing names
    result = res % MODULO
    print(result)

# Style 7: guard handled weirdly
if __name__ == "__main__":
    main()