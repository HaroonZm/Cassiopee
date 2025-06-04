from math import pi, atan2
q = 2 * pi
n = int(input())
cs = []
for _ in range(n):
    a, b = map(int, input().split())
    cs.append(complex(a, b))
for i in range(n):
    args = []
    for j in range(n):
        if j != i:
            d = cs[j] - cs[i]
            t = atan2(d.real, d.imag)
            if t < 0:
                t += q
            args.append(t / q)
    args.sort()
    dif = []
    for k in range(n-1):
        dif.append(args[k] - args[k-1])
    dif[0] += 1
    mx = max(dif)
    print(max(mx - 0.5, 0))