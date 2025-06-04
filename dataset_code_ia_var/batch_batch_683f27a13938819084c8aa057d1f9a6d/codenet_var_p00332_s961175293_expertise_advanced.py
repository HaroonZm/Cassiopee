e, y = map(int, input().split())
ei = [None, 1867, 1911, 1925, 1988]
eras = [(1988, 'H'), (1925, 'S'), (1911, 'T'), (1867, 'M')]
if e == 0:
    print(next(f'{era}{y - base}' for base, era in eras if y > base))
else:
    print(ei[e] + y)