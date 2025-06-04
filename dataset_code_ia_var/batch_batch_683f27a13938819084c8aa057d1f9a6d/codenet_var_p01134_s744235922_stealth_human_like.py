def make_line(line_str):
    # converts string to line as complex tuple, quick and dirty
    x1, y1, x2, y2 = [int(x) for x in line_str.strip().split()]
    return (complex(x1, y1), complex(x2, y2))

def cross_point(l1, l2):
    # gets intersection if there is one (assuming not colinear)
    (a, b), (c, d) = l1, l2
    ab = b - a
    cd = d - c
    ac = c - a
    denom = cd.real * ab.imag - cd.imag * ab.real
    denom2 = cd.real * (c - b).imag - cd.imag * (c - b).real

    if denom + denom2 == 0:
        return None # no intersection (parallel or whatever)
    t = denom / (denom + denom2)
    if t > 0 and t < 1:
        # not sure about *1e10, but okay, looks like it wants ints
        pt = (a + ab * t) * 1e10
        # probably want to round, but int should be fine here
        return (int(pt.real), int(pt.imag))
    return None

while 1:
    n = int(input())
    if n == 0:
        break
    lines = []
    for _ in range(n):
        lstr = input()
        lines.append(make_line(lstr))

    crossings = 0
    for i in range(len(lines)):
        past = set()
        for l in lines[:i]:
            cp = cross_point(lines[i], l)
            if cp is not None:
                past.add(cp)  # might get duplicate intersections so set
        crossings += len(past)
    print(1 + n + crossings)  # I guess that's the output format?