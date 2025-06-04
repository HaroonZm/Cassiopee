n, t = map(int, input().split())
an = list(map(int, input().split()))
mi = [an[0]]
i = 1
while i < n:
    mi.append(min(mi[i - 1], an[i]))
    i += 1
ma = 0
num_ma = 0
i = 1
while i < n:
    be = an[i] - mi[i - 1]
    if be > ma:
        ma = be
        num_ma = 1
    elif be == ma:
        num_ma += 1
    i += 1
print(num_ma)