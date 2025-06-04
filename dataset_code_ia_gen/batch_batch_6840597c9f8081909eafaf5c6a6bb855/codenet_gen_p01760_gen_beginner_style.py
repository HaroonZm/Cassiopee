T, D = map(int, input().split())
tA, tB = map(int, input().split())
dA, dB = map(int, input().split())

min_diff = 10**9

for vA_mult in range(D // dA + 1):
    vA = vA_mult * dA
    for vB_mult in range(D // dB + 1):
        vB = vB_mult * dB
        total = vA + vB
        if total < 1 or total > D:
            continue
        temp = (tA * vA + tB * vB) / total
        diff = abs(temp - T)
        if diff < min_diff:
            min_diff = diff

print("{0:.10f}".format(min_diff))