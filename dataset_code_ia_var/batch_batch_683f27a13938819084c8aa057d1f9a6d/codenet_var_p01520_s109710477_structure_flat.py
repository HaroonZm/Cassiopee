n, t, e = map(int, raw_input().split())
x = map(int, raw_input().split())
found = False
i = 0
while i < n:
    r = t % x[i]
    if min(r, x[i] - r) <= e:
        print i + 1
        found = True
        break
    i += 1
if not found:
    print -1