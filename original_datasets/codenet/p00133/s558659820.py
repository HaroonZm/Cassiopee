import copy

V = [list(raw_input()) for i in range(8)]
_V = []
for r in range(8):
    lis = []
    for c in range(8):
        lis.append('')
    else:
        _V.append(lis)
for angle in [90, 180, 270]:
    for r in range(8):
        for c in range(8):
            _V[c][7-r] = V[r][c]
    else:
        V = copy.deepcopy(_V)
    print angle
    for line in V:
        print ''.join(line)