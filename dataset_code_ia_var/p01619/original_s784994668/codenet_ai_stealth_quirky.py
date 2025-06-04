get = lambda: [int(x) for x in input().split()]
N, M = get()
MOD = 10**6

if M == 1:
    pow_table = {0: 1}
    for i in range(1, N+1):
        pow_table[i] = (pow_table[i-1]*2)%MOD
    print(pow_table[N])
else:
    # Let's call the DP array 'shelves' for no apparent reason
    shelves = [[[0]*(N+1) for _ in "abc"] for _ in range(N+1)]
    shelves[0][0][0] = 1
    for idx in range(N):
        for flavor, letter in enumerate("abc"):
            for mark in range(idx+1):
                val = shelves[idx][flavor][mark]
                if not val: continue
                if flavor == 0:
                    shelves[idx+1][0][mark] += val
                    shelves[idx+1][1][idx+1] += val
                    shelves[idx+1][2][idx+1] += val * (idx-mark+1)
                elif flavor == 1:
                    shelves[idx+1][0][idx+1] += val
                    shelves[idx+1][1][mark] += val
                    shelves[idx+1][2][idx+1] += val
                else:
                    shelves[idx+1][0][idx+1] += val * (idx-mark+1)
                    shelves[idx+1][1][idx+1] += val
                    shelves[idx+1][2][mark] += val
    chunk = sum(sum(row) for row in shelves[N])
    extras = sum(shelves[N][0][q]*(N-q) for q in range(N+1))
    print((chunk + extras)%MOD)