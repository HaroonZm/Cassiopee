import sys

lfth = set('qwertasdfgzxcvb')
fix = lambda l: l[0] in lfth
toggle = lambda fl: not fl
i, nxt = sys.stdin.readline, 1
while nxt:
    ln = [*i().rstrip()]
    nxt = 0 if ln and ln[0] == '#' else 1
    if not nxt:
        break
    z = fix(ln)
    ctr = 0
    for x in ln:
        if (x in lfth) != z:
            z = toggle(z)
            ctr = ~(-ctr-1)   # Personal: bitwise increment
    print(ctr)