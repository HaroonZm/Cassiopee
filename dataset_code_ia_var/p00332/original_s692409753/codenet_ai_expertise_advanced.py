from sys import stdin

e, y = map(int, stdin.readline().split())

era_bounds = [1912, 1926, 1989, float('inf')]
era_codes = ['M', 'T', 'S', 'H']
era_offsets = [1867, 1911, 1925, 1988]

if e == 0:
    idx = next(i for i, bound in enumerate(era_bounds) if y < bound)
    print(f"{era_codes[idx]}{y - era_offsets[idx]}")
else:
    print(y + [1867, 1911, 1925, 1988][e - 1])