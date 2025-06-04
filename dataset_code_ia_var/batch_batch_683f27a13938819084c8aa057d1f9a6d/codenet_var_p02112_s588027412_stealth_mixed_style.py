from functools import reduce

N = int(input()) + 1

X = [None]
C = list(map(lambda _: 0, range(360)))

def updates(c, idx, val):
    c[idx % 360] = max(c[idx % 360], val)

i = 1
while i < N:
    parts = input().split()
    X.append(parts)
    base = (int(parts[0]) - 1) * 30 + int(parts[1]) - 1
    end = base + int(parts[2]) - 1
    lvl = int(parts[3])
    # Range modification
    list(map(lambda pos: updates(C, pos, lvl), range(base, end + 1)))
    # Neighbour falloff
    for n in range(1, lvl + 1):
        idxs = [ (base - n + 360) % 360, (end + n) % 360 ]
        for ix, v in zip(idxs, [lvl-n, lvl-n]):
            updates(C, ix, v)
    i += 1

res = C[0]
for z in C:
    if z < res:
        res = z
print(res)