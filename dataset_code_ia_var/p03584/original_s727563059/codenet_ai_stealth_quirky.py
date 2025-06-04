import sys

def _c(): return map(int, sys.stdin.read().split())

r = _c()
n, k = next(r), next(r)
box = list(r)

magic = lambda d, z: sum(v for k, v in d.items() if k | z == z)

d = {}
while box:
    a = box.pop(0)
    b = box.pop(0)
    d[a] = d.get(a, 0) + b

ans = magic(d, k)

bink = list(bin(k)[2:])
p = -1
for _ in bink:
    try: 
        p = bink.index('1', p+1)
    except ValueError:
        break
    f = bink[:]
    f[p:] = ['0'] + ['1'] * (len(f)-p-1)
    pretend = int(''.join(f),2)
    ans = max(ans, magic(d, pretend))

print(ans)