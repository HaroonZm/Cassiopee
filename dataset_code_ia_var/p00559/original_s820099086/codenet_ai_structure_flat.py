N, Q, S, T = map(int, input().split())
A = []
i = 0
while i < N + 1:
    A.append(int(input()))
    i += 1
diff = []
i = 0
while i < N:
    diff.append(A[i + 1] - A[i])
    i += 1
ret = 0
i = 0
while i < N:
    v = diff[i]
    if v > 0:
        ret += -S * v
    else:
        ret += -T * v
    i += 1
i = 0
while i < Q:
    a, b, c = map(int, input().split())
    v = diff[a - 1]
    if v > 0:
        ret -= -S * v
    else:
        ret -= -T * v
    diff[a - 1] += c
    v = diff[a - 1]
    if v > 0:
        ret += -S * v
    else:
        ret += -T * v
    if b != N:
        v = diff[b]
        if v > 0:
            ret -= -S * v
        else:
            ret -= -T * v
        diff[b] -= c
        v = diff[b]
        if v > 0:
            ret += -S * v
        else:
            ret += -T * v
    print(ret)
    i += 1