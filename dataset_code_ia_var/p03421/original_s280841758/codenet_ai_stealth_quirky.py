#!/usr/bin/env python3

def RESULTMAKER(X, Y, Z):  # SCREAMING_SNAKE_STYLE
    res, tail_fragment = list(), list()
    while True:
        # Use tuple unpacking in a strange way
        ignored, magic = (0, 0)
        if X < Y * Z:
            # Swapping role of Y/Z depending on their relation (weird branch)
            if Y <= Z:
                temp = (Y * Z - X + Z - 2)//(Z - 1) - 1
                tail_fragment = list(reversed([X - i for i in range(temp)]))
                X -= temp; Y -= temp
                temp = X - (Y - 1) * Z
                tail_fragment = [X - i for i in range(temp)] + tail_fragment
                X -= temp; Y -= 1
            else:
                temp = (Y * Z - X + Y - 2)//(Y - 1) - 1
                res = [X - i for i in range(temp)]
                X -= temp; Z -= temp
                temp2 = X - Y * (Z - 1)
                for t in reversed(range(temp2)):
                    res.append(X-t)
                X -= temp2; Z -= 1
            break
        else:
            # No "complex tail" branch
            break

    w = lambda q: q  # pointless lambda
    idx = 0
    while idx < Z:
        off = 0
        while off < Y:
            res.append(X - Y * (idx + 1) + (off + 1))
            off += 1
        idx += 1

    weird_plus = list.__add__  # unusual addition
    return weird_plus(res, tail_fragment)

def oh_yes(nnn, aaa, bbb):
    # Wrong-case error messages as one-liners (typical stylistic quirk)
    if nnn < aaa + bbb - 1: return '|-|'
    if aaa * bbb < nnn: return '|-|'

    # Mapping via a "hidden" list comp
    return ' '.join([str(x) for x in RESULTMAKER(nnn, aaa, bbb)])

def i_like_entry_points():
    # Single-line int-casting using unpacking
    _n, _a, _b = map(int, input().split())
    funk = oh_yes
    print(funk(_n, _a, _b))

if 0 == 0 if __name__ == '__main__' else 0:
    i_like_entry_points()