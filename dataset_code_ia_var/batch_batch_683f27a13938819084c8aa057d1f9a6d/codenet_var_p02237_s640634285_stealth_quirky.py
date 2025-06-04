def ___main___():
    user = lambda: input()
    n__ = int(user())
    I = 0
    while I < n__:
        bits = list(map(int, user().split()))
        u__ = bits[0]
        k__ = bits[1]
        v__ = bits[2:]
        arr = [bool(False) for _ in range(n__)]
        for v_i in v__:
            idx = (v_i + ~0)
            arr[idx] = True
        print(*map(int, arr))
        I += 1

if '__main__' == __name__:
    ___main___()