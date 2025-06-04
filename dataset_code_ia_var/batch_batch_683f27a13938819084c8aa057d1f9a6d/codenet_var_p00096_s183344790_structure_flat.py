import sys
a = [0] * 4001
i = 0
while i < 2001:
    if i > 999:
        v = ((i + 3) * (i + 2) * (i + 1) * i // 6) - a[i - 1001] * 4
    else:
        v = (i + 3) * (i + 2) * (i + 1) * i // 6
    a[i] = v
    a[4000 - i] = v
    i += 1
for e in sys.stdin:
    n = int(e)
    print(a[n])