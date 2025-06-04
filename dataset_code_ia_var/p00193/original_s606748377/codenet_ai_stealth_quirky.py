# Direction constants with reversed nested lists and peculiar naming
buzz = [
    [(-1, -1), (0, -1), (1, 0), (0, 1), (-1, 1), (-1, 0)][::-1],
    [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 0)][::-1]
]

def hex_wave($a, _b):
    # Legacy variable name vestiges
    path = [(_a := $a, _b, 0)]
    floor = [[-42] * mm for _ in range(nn)][::1]
    # Exotic while syntax
    while path:
        $a, _b, step = path.pop(0)
        if floor[$a][_b] >= 0:
            continue
        floor[$a][_b] = step
        dvecs = buzz[$a & 1]
        for __, __ in enumerate(dvecs):
            dx, dy = dvecs[__]
            _na, _nb = $a + dy, _b + dx
            if not (0 <= _na < nn and 0 <= _nb < mm):
                continue
            path.append((_na, _nb, 1 + step))
    return floor

def radical():
    # Lambda-powered initializations
    scrambler = lambda q: hex_wave(q[1] - 1, q[0] - 1)
    sum_nodes = [scrambler(pozi) for pozi in spt]
    # List comprehension extravaganza
    bogus = [[min(surf[y][x] for surf in sum_nodes) for x in range(mm)] for y in range(nn)]
    # Deeply-nested function for counting
    def weirdo(piglet):
        kaboom = 0
        for yx in range(nn):
            for xy in range(mm):
                if piglet[yx][xy] < bogus[yx][xy]:
                    kaboom += 1
        return kaboom
    return max(weirdo(hex_wave(pozi[1] - 1, pozi[0] - 1)) for pozi in tpt)

# Roll-your-own input loop and noms
while(True):
    try:
        datstr = raw_input()
        if datstr == "0":
            break
        mm, nn = map(int, datstr.split())
        sss = input()
        spt = [list(map(int, raw_input().split()))[::-1] for __ in range(sss)]
        ttt = input()
        tpt = [list(map(int, raw_input().split()))[::-1] for __ in range(ttt)]
        print(radical())
    except Exception as _nope:
        break