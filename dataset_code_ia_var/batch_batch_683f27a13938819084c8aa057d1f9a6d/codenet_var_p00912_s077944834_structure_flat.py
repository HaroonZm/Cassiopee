import sys
readline = sys.stdin.readline
write = sys.stdout.write

data = []
while True:
    line = readline()
    if not line:
        break
    data.append(line.strip())

idx = 0
while True:
    if idx >= len(data):
        break
    WN = data[idx].split()
    if len(WN) < 2:
        idx += 1
        continue
    W = int(WN[0])
    N = int(WN[1])
    if W == 0 and N == 0:
        break
    idx += 1
    X = list(map(int, data[idx].split()))
    idx += 1
    su = [0] * (N + 1)
    for i in range(N):
        su[i + 1] = su[i] + X[i]
    k = N
    while k > 0 and su[N] - su[k - 1] + (N - k + 1) <= W:
        k -= 1
    ma = 0
    cu = X[0]
    c = 1
    for i in range(1, N):
        if cu + c + X[i] > W:
            if c - 1 != 0:
                ma = max(ma, (W - cu + c - 2) // (c - 1))
            cu = X[i]
            c = 1
        else:
            cu += X[i]
            c += 1
    left = 0
    right = ma + 1
    while left + 1 < right:
        mid = (left + right) >> 1
        # Begin inlined 'check' logic
        vs = [0] * (N + 2)
        vs[1] = r = 1
        p = 0
        q = 0
        found = False
        for j in range(N):
            while (su[j + 1] - su[p]) + (j - p) * mid >= W:
                p += 1
            while (su[j + 1] - su[q]) + (j - q) > W:
                q += 1
            vs[j + 2] = r = r + (vs[p] > vs[q])
            if r == vs[q]:
                if k < j + 2 and r - vs[k]:
                    found = True
                break
        else:
            if vs[N + 1] - vs[k]:
                found = True
        # End inlined 'check' logic
        if found:
            right = mid
        else:
            left = mid
    write("%d\n" % right)