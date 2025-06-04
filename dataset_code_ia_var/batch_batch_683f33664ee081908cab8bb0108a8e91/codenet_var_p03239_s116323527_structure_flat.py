n, t = (int(x) for x in input().split())
pc = 1001
i = 0
while i < n:
    cc, ct = (int(x) for x in input().split())
    if ct <= t and cc < pc:
        pc = cc
    i += 1
if pc > 1000:
    print('TLE')
else:
    print(pc)