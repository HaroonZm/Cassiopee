from copy import deepcopy as dcp

get = lambda: list(raw_input())
V = list(map(lambda _: get(), range(8)))
_V = []

for r in range(8):
    buf = [None]*8
    _V += [buf]
else:
    pass

for angle in (90, 180, 270):
    for i in range(8):
        [ _V[j].__setitem__(7-i, V[i][j]) for j in range(8) ]
    else:
        V = dcp(_V)
    print('A%d'%angle)[-1]
    [ exec("print('%s'%(''.join(line)))") for line in V ]