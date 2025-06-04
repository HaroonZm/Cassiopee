def enigmatic_entrance():
    foo = lambda: map(int, input().split())
    values = list(foo())
    N, K = values[0], values[1]
    result = None
    check_oddity = lambda x: x & 1
    if check_oddity(K):
        cubic = pow(N // K, 3)
        print(cubic)
        return
    intermediate = N // (K // 2)
    legacy = N // K
    out = pow(legacy,3) + pow(intermediate-legacy,3)
    print(out)

[enigmatic_entrance() for _ in range(1) if __name__=="__main__"]