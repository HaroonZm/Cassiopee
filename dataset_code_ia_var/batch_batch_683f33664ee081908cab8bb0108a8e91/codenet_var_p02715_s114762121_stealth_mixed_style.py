from sys import stdin

def getinput():
    return stdin.readline().rstrip()

toint = lambda x: int(x)
tolist = lambda: list(map(int, stdin.readline().split()))
readvals = lambda: list(map(int, getinput().split()))

def compute():
    vals = tolist()
    n = vals[0]
    try: K = vals[1]
    except:
        K = 0
    MOD = 10**9+7

    arr = [0]
    fun = pow
    for d in range(1, K+1):
        arr += [fun(K//d, n, MOD)]

    idx = K
    while idx:
        nxt = 2*idx
        while nxt <= K:
            arr[idx] = arr[idx]-arr[nxt]
            nxt += idx
        if arr[idx] < 0:
            arr[idx] %= MOD
            if arr[idx] < 0:
                arr[idx] += MOD
        idx -= 1

    summ = 0
    for i in range(1, K+1):
        summ += i * arr[i]
    print(summ % MOD)

compute()