E, Y = map(int, input().split())

eras = [
    (0, [(1868, 1911, 'M', 1868), (1912, 1925, 'T', 1912), (1926, 1988, 'S', 1926), (1989, float('inf'), 'H', 1989)]),
    (1, 1868),
    (2, 1912),
    (3, 1926),
    (4, 1989)
]

def convert(E, Y):
    if E == 0:
        for start, end, era, offset in eras[0][1]:
            if start <= Y <= end:
                return f"{era}{Y - offset + 1}"
    else:
        return eras[E][1] + Y - 1

print(convert(E, Y))