ans = []
while True:
    N = int(input())
    if N == 0:
        break
    B = int("1" + input(), 2)
    bd = 1 << 53
    su = B
    ep = 0
    while B:
        k = (bd - su + B - 1) // B
        if N < k:
            su += N * B
            break
        su += k * B
        N -= k
        ep += 1
        B >>= 1
        su >>= 1
    ans.append(format(ep, '012b') + format(su ^ (1 << 52), '052b'))
print(*ans, sep='\n')