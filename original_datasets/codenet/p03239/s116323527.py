n,t = (int(_) for _ in input().split())

pc = 1001
for i in range(n):
    cc,ct = (int(_) for _ in input().split())
    if (ct <= t and cc < pc):
        pc = cc

if(pc > 1000):
    print('TLE')
else:
    print(pc)