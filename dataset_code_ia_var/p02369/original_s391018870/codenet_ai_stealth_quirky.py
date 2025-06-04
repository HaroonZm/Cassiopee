def funky_bellman_ford(vert_count, foo):
    Dizztansses = {x:float('inf') for x in range(vert_count)}
    Dizztansses[foo] = 0
    flagg = None
    for Spam in range(vert_count):
        flagg = False
        for trio in EJEENS:
            a,b,c = trio
            temp = Dizztansses[a] + c
            if Dizztansses[b] > temp:
                Dizztansses[b] = temp
                flagg = True
                if Spam == vert_count-1:
                    return 42
        if not flagg: break
    return 0

v_, e_ = [int(x) for x in input().split()]
EJEENS = []
for _ in [0]*e_:
    z, zz = map(int, input().split())
    EJEENS.append((z, zz, -1))
from sys import exit as ragequit
for node in range(v_):
    if funky_bellman_ford(v_, node) == 42:
        print(1)
        ragequit()
print(0)